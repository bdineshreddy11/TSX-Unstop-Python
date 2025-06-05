document.addEventListener("DOMContentLoaded", () => {
  // Enhanced Mobile Navigation Toggle
  const navToggle = document.querySelector(".nav-toggle")
  const navMenu = document.querySelector(".nav-menu")
  const header = document.querySelector(".header")

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      navMenu.classList.toggle("active")

      // Enhanced hamburger animation
      const hamburger = this.querySelector(".hamburger")
      if (hamburger) {
        hamburger.classList.toggle("active")
      }
    })

    // Close menu when clicking on a link
    document.querySelectorAll(".nav-link").forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active")
        const hamburger = navToggle.querySelector(".hamburger")
        if (hamburger) {
          hamburger.classList.remove("active")
        }
      })
    })
  }

  // Enhanced scroll effects
  const handleScroll = () => {
    const scrolled = window.pageYOffset

    // Header background change on scroll
    if (header) {
      if (scrolled > 100) {
        header.classList.add("scrolled")
      } else {
        header.classList.remove("scrolled")
      }
    }

    // Parallax effect for hero section
    const hero = document.querySelector(".hero")
    if (hero) {
      const heroOffset = hero.offsetTop
      const heroHeight = hero.offsetHeight
      const windowHeight = window.innerHeight

      if (scrolled > heroOffset - windowHeight && scrolled < heroOffset + heroHeight) {
        const rate = (scrolled - heroOffset + windowHeight) / (heroHeight + windowHeight)
        hero.style.transform = `translateY(${rate * 50}px)`
      }
    }
  }

  window.addEventListener("scroll", handleScroll)

  // Enhanced animate on scroll
  const animateOnScroll = () => {
    const elements = document.querySelectorAll(".animate-on-scroll")

    elements.forEach((element) => {
      const elementPosition = element.getBoundingClientRect().top
      const windowHeight = window.innerHeight

      if (elementPosition < windowHeight - 100) {
        element.classList.add("animated")
      }
    })
  }

  // Add animate-on-scroll class to elements
  const elementsToAnimate = document.querySelectorAll(".skill-card, .project-card, .timeline-item, .contact-card")

  elementsToAnimate.forEach((element, index) => {
    element.classList.add("animate-on-scroll")
    element.style.transitionDelay = `${index * 0.1}s`
  })

  // Run animation check on load and scroll
  animateOnScroll()
  window.addEventListener("scroll", animateOnScroll)

  // Enhanced skill progress animation
  const animateSkillBars = () => {
    const skillBars = document.querySelectorAll(".skill-progress")

    skillBars.forEach((bar) => {
      const barPosition = bar.getBoundingClientRect().top
      const windowHeight = window.innerHeight

      if (barPosition < windowHeight - 100 && !bar.classList.contains("animated")) {
        const width = bar.getAttribute("data-width") || bar.style.width
        bar.style.width = "0"
        bar.classList.add("animated")

        setTimeout(() => {
          bar.style.width = width
        }, 200)
      }
    })
  }

  window.addEventListener("scroll", animateSkillBars)
  animateSkillBars() // Run on load

  // Enhanced typing effect for hero title
  const typeWriter = (element, text, speed = 100) => {
    let i = 0
    element.innerHTML = ""

    const timer = setInterval(() => {
      if (i < text.length) {
        element.innerHTML += text.charAt(i)
        i++
      } else {
        clearInterval(timer)
        element.classList.add("typing-complete")
      }
    }, speed)
  }

  // Apply typing effect to hero title
  const heroTitle = document.querySelector(".hero-title")
  if (heroTitle) {
    const originalText = heroTitle.textContent
    setTimeout(() => {
      typeWriter(heroTitle, originalText, 80)
    }, 500)
  }

  // Enhanced form validation with animations
  const contactForm = document.querySelector(".contact-form")

  if (contactForm) {
    const inputs = contactForm.querySelectorAll(".form-control")

    // Add focus animations
    inputs.forEach((input) => {
      input.addEventListener("focus", function () {
        this.parentElement.classList.add("focused")
      })

      input.addEventListener("blur", function () {
        if (!this.value) {
          this.parentElement.classList.remove("focused")
        }
      })
    })

    contactForm.addEventListener("submit", (e) => {
      let isValid = true
      const nameInput = document.querySelector('input[name="name"]')
      const emailInput = document.querySelector('input[name="email"]')
      const messageInput = document.querySelector('textarea[name="message"]')

      // Enhanced validation with animations
      if (nameInput && nameInput.value.trim() === "") {
        isValid = false
        showError(nameInput, "Name is required")
      } else if (nameInput) {
        clearError(nameInput)
      }

      if (emailInput) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (emailInput.value.trim() === "") {
          isValid = false
          showError(emailInput, "Email is required")
        } else if (!emailRegex.test(emailInput.value.trim())) {
          isValid = false
          showError(emailInput, "Please enter a valid email")
        } else {
          clearError(emailInput)
        }
      }

      if (messageInput && messageInput.value.trim() === "") {
        isValid = false
        showError(messageInput, "Message is required")
      } else if (messageInput) {
        clearError(messageInput)
      }

      if (!isValid) {
        e.preventDefault()
        // Shake animation for form
        contactForm.classList.add("shake")
        setTimeout(() => {
          contactForm.classList.remove("shake")
        }, 500)
      }
    })
  }

  function showError(input, message) {
    const formGroup = input.closest(".form-group")
    let errorDiv = formGroup.querySelector(".form-error")

    if (!errorDiv) {
      errorDiv = document.createElement("div")
      errorDiv.className = "form-error"
      formGroup.appendChild(errorDiv)
    }

    errorDiv.textContent = message
    errorDiv.style.animation = "fadeInUp 0.3s ease-out"
    input.classList.add("is-invalid")
  }

  function clearError(input) {
    const formGroup = input.closest(".form-group")
    const errorDiv = formGroup.querySelector(".form-error")

    if (errorDiv) {
      errorDiv.style.animation = "fadeOut 0.3s ease-out"
      setTimeout(() => {
        errorDiv.remove()
      }, 300)
    }

    input.classList.remove("is-invalid")
  }

  // Enhanced smooth scrolling
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const target = document.querySelector(this.getAttribute("href"))

      if (target) {
        e.preventDefault()

        const headerHeight = header ? header.offsetHeight : 0
        const targetPosition = target.offsetTop - headerHeight - 20

        window.scrollTo({
          top: targetPosition,
          behavior: "smooth",
        })
      }
    })
  })

  // Intersection Observer for better performance
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animated")
        observer.unobserve(entry.target)
      }
    })
  }, observerOptions)

  // Observe elements for animation
  document.querySelectorAll(".animate-on-scroll").forEach((el) => {
    observer.observe(el)
  })

  // Enhanced loading states
  const images = document.querySelectorAll("img")
  images.forEach((img) => {
    img.addEventListener("load", function () {
      this.classList.add("loaded")
    })

    if (img.complete) {
      img.classList.add("loaded")
    }
  })

  // Add current year to footer
  const currentYearElement = document.getElementById("current-year")
  if (currentYearElement) {
    currentYearElement.textContent = new Date().getFullYear()
  }

  // Enhanced project filter functionality (for projects page)
  const filterButtons = document.querySelectorAll(".filter-btn")
  const projectCards = document.querySelectorAll(".project-card")

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const filter = this.getAttribute("data-filter")

      // Update active button with animation
      filterButtons.forEach((btn) => {
        btn.classList.remove("active")
        btn.style.transform = "scale(1)"
      })
      this.classList.add("active")
      this.style.transform = "scale(1.05)"

      // Filter projects with stagger animation
      projectCards.forEach((card, index) => {
        card.style.transition = "all 0.3s ease-out"
        card.style.transitionDelay = `${index * 0.1}s`

        if (filter === "all") {
          card.style.display = "block"
          setTimeout(() => {
            card.style.opacity = "1"
            card.style.transform = "translateY(0)"
          }, index * 100)
        } else {
          const categories = card.getAttribute("data-categories")
          if (categories && categories.includes(filter)) {
            card.style.display = "block"
            setTimeout(() => {
              card.style.opacity = "1"
              card.style.transform = "translateY(0)"
            }, index * 100)
          } else {
            card.style.opacity = "0"
            card.style.transform = "translateY(20px)"
            setTimeout(() => {
              card.style.display = "none"
            }, 300)
          }
        }
      })
    })
  })

  // Add CSS for shake animation
  const style = document.createElement("style")
  style.textContent = `
    .shake {
      animation: shake 0.5s ease-in-out;
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-5px); }
      75% { transform: translateX(5px); }
    }

    @keyframes fadeOut {
      from { opacity: 1; transform: translateY(0); }
      to { opacity: 0; transform: translateY(-10px); }
    }

    .form-group.focused .form-label {
      color: var(--primary-color);
      transform: translateY(-2px);
    }

    .form-control.is-invalid {
      border-color: var(--error-color);
      box-shadow: 0 0 0 2px rgba(245, 101, 101, 0.2);
    }

    img {
      opacity: 0;
      transition: opacity 0.3s ease-out;
    }

    img.loaded {
      opacity: 1;
    }

    .typing-complete::after {
      content: "|";
      animation: blink 1s infinite;
    }

    @keyframes blink {
      0%, 50% { opacity: 1; }
      51%, 100% { opacity: 0; }
    }
  `
  document.head.appendChild(style)
})
