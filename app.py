from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import json
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# Admin credentials (in production, use proper authentication)
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'  # Change this in production

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Load resume data from JSON file
def load_resume_data():
    try:
        with open('static/data/resume.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Create directory if it doesn't exist
        os.makedirs('static/data', exist_ok=True)
        os.makedirs('static/images', exist_ok=True)
        
        # Create a sample resume data file with Dinesh's information
        sample_data = {
            "basics": {
                "name": "Dinesh Reddy",
                "label": "Full Stack Developer & Data Analytics Enthusiast",
                "email": "bellamdinesh1123@gmail.com",
                "phone": "+91 9494950344",
                "website": "https://dineshreddy.dev",
                "summary": "Passionate Computer Science Engineering student with hands-on experience in full-stack development and data analytics. Specialized in React.js, Node.js, and modern web technologies. Currently pursuing Bachelor of Technology with a focus on creating innovative solutions and scalable applications.",
                "location": {
                    "city": "Hyderabad",
                    "region": "Telangana",
                    "countryCode": "IN"
                },
                "profiles": [
                    {
                        "network": "LinkedIn",
                        "username": "dinesh-reddy",
                        "url": "https://linkedin.com/in/dinesh-reddy"
                    },
                    {
                        "network": "GitHub",
                        "username": "dineshreddy",
                        "url": "https://github.com/dineshreddy"
                    }
                ]
            },
            "work": [
                {
                    "company": "AWS APAC Solutions Architecture",
                    "position": "Virtual Experience Participant",
                    "website": "https://aws.amazon.com",
                    "startDate": "2025-02-01",
                    "endDate": "2025-02-28",
                    "summary": "Completed virtual experience program focusing on cloud architecture solutions",
                    "highlights": [
                        "Designed simple and scalable hosting architecture based on Elastic Beanstalk",
                        "Optimized application performance and response times",
                        "Described proposed architecture in plain language for client understanding",
                        "Calculated hosting costs and performance metrics"
                    ]
                }
            ],
            "education": [
                {
                    "institution": "CVR College of Engineering",
                    "area": "Computer Science and Engineering",
                    "studyType": "Bachelor of Technology",
                    "startDate": "2022-06-01",
                    "endDate": "2026-04-30",
                    "gpa": "8.5",
                    "location": "Hyderabad, India"
                }
            ],
            "skills": [
                {
                    "name": "Programming Languages",
                    "level": "Advanced",
                    "keywords": ["Java", "Python", "C", "JavaScript"]
                },
                {
                    "name": "Full Stack Development",
                    "level": "Advanced",
                    "keywords": ["React.js", "Node.js", "Express.js", "HTML5", "CSS3"]
                },
                {
                    "name": "Database & Cloud",
                    "level": "Intermediate",
                    "keywords": ["MongoDB", "MySQL", "AWS", "Cloud Architecture"]
                }
            ],
            "projects": [
                {
                    "id": 1,
                    "name": "Resume Builder Application",
                    "description": "A comprehensive resume building platform with real-time editing, multiple templates, and email functionality.",
                    "highlights": [
                        "Led feedback sessions and gathered insights from 300+ users",
                        "Achieved a 90% satisfaction rate and built strong user trust",
                        "Implemented real-time user authentication and resume tracking",
                        "Increased engagement by 20% with seamless user experience"
                    ],
                    "keywords": ["Node.js", "Express.js", "React", "MongoDB", "Bootstrap", "SendGrid"],
                    "url": "https://github.com/dineshreddy/resume-builder",
                    "startDate": "2024-06-01",
                    "endDate": "2024-07-31",
                    "status": "completed",
                    "featured": True,
                    "created_at": "2024-06-01",
                    "image": "resume.jpeg"
                },
                {
                    "id": 2,
                    "name": "AWS Cloud Architecture Solution",
                    "description": "Designed and implemented scalable cloud hosting architecture using AWS Elastic Beanstalk for optimal performance and cost-effectiveness.",
                    "highlights": [
                        "Designed simple and scalable hosting architecture based on Elastic Beanstalk",
                        "Optimized for better user experience and response times",
                        "Described proposed architecture in plain language for client understanding",
                        "Calculated hosting costs and performance benefits",
                        "Implemented best practices for cloud security and scalability"
                    ],
                    "keywords": ["AWS", "Elastic Beanstalk", "Cloud Architecture", "Scalability", "Performance Optimization"],
                    "url": "https://github.com/dineshreddy/aws-architecture",
                    "startDate": "2025-02-01",
                    "endDate": "2025-02-28",
                    "status": "completed",
                    "featured": True,
                    "created_at": "2025-02-01",
                    "image": "aws.jpeg"
                },
                {
                    "id": 3,
                    "name": "Data Analytics Dashboard",
                    "description": "Interactive business intelligence dashboard created using Tableau and Excel for comprehensive data analysis and visualization.",
                    "highlights": [
                        "Completed Deloitte job simulation involving data analysis and forensic technology",
                        "Created comprehensive data dashboard using Tableau",
                        "Used Excel to classify data and draw meaningful business conclusions",
                        "Applied statistical analysis techniques for actionable insights",
                        "Presented findings to stakeholders with clear visualizations"
                    ],
                    "keywords": ["Tableau", "Excel", "Data Analysis", "Business Intelligence", "Data Visualization"],
                    "url": "https://github.com/dineshreddy/data-analytics-dashboard",
                    "startDate": "2025-02-01",
                    "endDate": "2025-02-28",
                    "status": "completed",
                    "featured": True,
                    "created_at": "2025-02-01",
                    "image": "data.jpeg"
                }
            ]
        }
        
        with open('static/data/resume.json', 'w') as f:
            json.dump(sample_data, f, indent=2)
        
        return sample_data

def save_resume_data(data):
    with open('static/data/resume.json', 'w') as f:
        json.dump(data, f, indent=2)

# Public Routes
@app.route('/')
def index():
    resume_data = load_resume_data()
    return render_template('index.html', resume=resume_data)

@app.route('/about')
def about():
    resume_data = load_resume_data()
    return render_template('about.html', resume=resume_data)

@app.route('/resume')
def resume():
    resume_data = load_resume_data()
    return render_template('resume.html', resume=resume_data)

@app.route('/resume/pdf')
def resume_pdf():
    return render_template('resume_pdf.html')

@app.route('/projects')
def projects():
    resume_data = load_resume_data()
    projects_list = resume_data.get('projects', [])
    return render_template('projects.html', projects=projects_list)

@app.route('/projects/<project_name>')
def project_detail(project_name):
    resume_data = load_resume_data()
    project = next((p for p in resume_data.get('projects', []) if p['name'] == project_name), None)
    if project:
        return render_template('project_detail.html', project=project)
    return redirect(url_for('projects'))

@app.route('/coffee')
def coffee():
    return render_template('coffee.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            flash('Your message has been sent! Thank you for reaching out.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash('Successfully logged in!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('logged_in', None)
    flash('Successfully logged out!', 'success')
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    resume_data = load_resume_data()
    projects = resume_data.get('projects', [])
    return render_template('admin/dashboard.html', projects=projects)

@app.route('/admin/projects')
@login_required
def admin_projects():
    resume_data = load_resume_data()
    projects = resume_data.get('projects', [])
    return render_template('admin/projects.html', projects=projects)

@app.route('/admin/projects/add', methods=['GET', 'POST'])
@login_required
def admin_add_project():
    if request.method == 'POST':
        resume_data = load_resume_data()
        
        # Generate new project ID
        existing_ids = [p.get('id', 0) for p in resume_data.get('projects', [])]
        new_id = max(existing_ids) + 1 if existing_ids else 1
        
        new_project = {
            'id': new_id,
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'highlights': [h.strip() for h in request.form.get('highlights', '').split('\n') if h.strip()],
            'keywords': [k.strip() for k in request.form.get('keywords', '').split(',') if k.strip()],
            'url': request.form.get('url'),
            'startDate': request.form.get('startDate'),
            'endDate': request.form.get('endDate'),
            'status': request.form.get('status', 'completed'),
            'featured': 'featured' in request.form,
            'created_at': datetime.now().isoformat(),
            'image': request.form.get('image', '')
        }
        
        if 'projects' not in resume_data:
            resume_data['projects'] = []
        
        resume_data['projects'].append(new_project)
        save_resume_data(resume_data)
        
        flash('Project added successfully!', 'success')
        return redirect(url_for('admin_projects'))
    
    return render_template('admin/add_project.html')

@app.route('/admin/projects/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_project(project_id):
    resume_data = load_resume_data()
    project = next((p for p in resume_data.get('projects', []) if p.get('id') == project_id), None)
    
    if not project:
        flash('Project not found!', 'error')
        return redirect(url_for('admin_projects'))
    
    if request.method == 'POST':
        project.update({
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'highlights': [h.strip() for h in request.form.get('highlights', '').split('\n') if h.strip()],
            'keywords': [k.strip() for k in request.form.get('keywords', '').split(',') if k.strip()],
            'url': request.form.get('url'),
            'startDate': request.form.get('startDate'),
            'endDate': request.form.get('endDate'),
            'status': request.form.get('status', 'completed'),
            'featured': 'featured' in request.form,
            'updated_at': datetime.now().isoformat(),
            'image': request.form.get('image', project.get('image', ''))
        })
        
        save_resume_data(resume_data)
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin_projects'))
    
    return render_template('admin/edit_project.html', project=project)

@app.route('/admin/projects/delete/<int:project_id>', methods=['POST'])
@login_required
def admin_delete_project(project_id):
    resume_data = load_resume_data()
    projects = resume_data.get('projects', [])
    
    resume_data['projects'] = [p for p in projects if p.get('id') != project_id]
    save_resume_data(resume_data)
    
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin_projects'))

# API Routes for AJAX operations
@app.route('/api/projects/<int:project_id>/toggle-featured', methods=['POST'])
@login_required
def toggle_project_featured(project_id):
    resume_data = load_resume_data()
    project = next((p for p in resume_data.get('projects', []) if p.get('id') == project_id), None)
    
    if project:
        project['featured'] = not project.get('featured', False)
        save_resume_data(resume_data)
        return jsonify({'success': True, 'featured': project['featured']})
    
    return jsonify({'success': False}), 404

if __name__ == '__main__':
    # For production deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
