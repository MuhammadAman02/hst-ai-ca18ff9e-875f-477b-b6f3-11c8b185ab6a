from nicegui import ui, app
import os

# Configure the app
app.title = "ML Engineer Portfolio"
app.favicon = "🧠"

# Sample ML projects data
ml_projects = [
    {
        "title": "Predictive Maintenance System",
        "description": "Developed a machine learning model to predict equipment failures before they occur, reducing downtime by 37% and maintenance costs by $2.1M annually.",
        "technologies": ["Python", "TensorFlow", "Time Series Analysis", "Random Forest"],
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
        "github": "https://github.com/username/predictive-maintenance"
    },
    {
        "title": "Customer Churn Prediction",
        "description": "Built an end-to-end ML pipeline to identify customers at risk of churning, enabling targeted retention campaigns that improved customer retention by 24%.",
        "technologies": ["Scikit-learn", "XGBoost", "Feature Engineering", "MLflow"],
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
        "github": "https://github.com/username/churn-prediction"
    },
    {
        "title": "Computer Vision for Quality Control",
        "description": "Implemented a CNN-based computer vision system for manufacturing quality control, reducing defect escape rate by 92% and inspection costs by 65%.",
        "technologies": ["PyTorch", "OpenCV", "CNN", "Transfer Learning"],
        "image": "https://images.unsplash.com/photo-1581092921461-eab62e97a780?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
        "github": "https://github.com/username/cv-quality-control"
    },
    {
        "title": "NLP for Customer Support Automation",
        "description": "Developed an NLP system to automatically categorize and route customer support tickets, reducing response time by 74% and improving customer satisfaction scores.",
        "technologies": ["BERT", "Transformers", "Hugging Face", "FastAPI"],
        "image": "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
        "github": "https://github.com/username/nlp-support-automation"
    }
]

# Skills data
skills = {
    "Machine Learning": 95,
    "Python": 90,
    "Deep Learning": 85,
    "Data Preprocessing": 92,
    "TensorFlow/PyTorch": 88,
    "MLOps": 80,
    "Computer Vision": 82,
    "NLP": 78,
    "Time Series Analysis": 85,
    "SQL": 75,
    "Cloud (AWS/GCP)": 80,
    "Docker/Kubernetes": 75
}

# Experience data
experiences = [
    {
        "role": "Senior ML Engineer",
        "company": "TechInnovate AI",
        "period": "2021 - Present",
        "description": "Lead ML engineer for predictive analytics solutions across multiple industries. Designed and implemented end-to-end ML pipelines and deployed models to production."
    },
    {
        "role": "Machine Learning Engineer",
        "company": "DataDriven Solutions",
        "period": "2018 - 2021",
        "description": "Developed and deployed machine learning models for customer segmentation, recommendation systems, and demand forecasting."
    },
    {
        "role": "Data Scientist",
        "company": "AnalyticsFirst",
        "period": "2016 - 2018",
        "description": "Conducted exploratory data analysis, feature engineering, and model development for various business problems."
    }
]

# Education data
education = [
    {
        "degree": "M.S. in Computer Science, Machine Learning Specialization",
        "institution": "Stanford University",
        "year": "2016"
    },
    {
        "degree": "B.S. in Mathematics and Statistics",
        "institution": "University of California, Berkeley",
        "year": "2014"
    }
]

# Custom CSS for the portfolio
custom_css = """
<style>
    .header {
        background: linear-gradient(135deg, #4568dc, #b06ab3);
        color: white;
        padding: 2rem 0;
        border-radius: 0 0 20px 20px;
    }
    .section-title {
        border-left: 5px solid #4568dc;
        padding-left: 15px;
        margin: 30px 0 20px 0;
    }
    .project-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-radius: 10px;
        overflow: hidden;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .skill-bar {
        height: 10px;
        border-radius: 5px;
        background: linear-gradient(90deg, #4568dc, #b06ab3);
    }
    .contact-form {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
    }
    .nav-link {
        cursor: pointer;
        transition: color 0.3s ease;
    }
    .nav-link:hover {
        color: #b06ab3;
    }
    .footer {
        background-color: #343a40;
        color: white;
        padding: 20px 0;
        margin-top: 50px;
    }
    .social-icon {
        font-size: 1.5rem;
        margin: 0 10px;
        color: white;
        transition: color 0.3s ease;
    }
    .social-icon:hover {
        color: #b06ab3;
    }
    .experience-card {
        border-left: 3px solid #4568dc;
        padding-left: 20px;
        margin-bottom: 20px;
    }
    .profile-image {
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
</style>
"""

# Add custom CSS to the page
@ui.page('/')
def portfolio_page():
    ui.add_head_html(custom_css)
    
    # Navigation bar
    with ui.header().classes('flex justify-between items-center p-4 bg-white shadow-sm'):
        ui.label('ML Engineer Portfolio').classes('text-xl font-bold')
        with ui.row().classes('gap-4'):
            ui.button('Home', on_click=lambda: ui.navigate_to('#home')).classes('nav-link')
            ui.button('Projects', on_click=lambda: ui.navigate_to('#projects')).classes('nav-link')
            ui.button('Skills', on_click=lambda: ui.navigate_to('#skills')).classes('nav-link')
            ui.button('Experience', on_click=lambda: ui.navigate_to('#experience')).classes('nav-link')
            ui.button('Contact', on_click=lambda: ui.navigate_to('#contact')).classes('nav-link')
    
    # Main content
    with ui.column().classes('w-full max-w-screen-xl mx-auto p-4'):
        # Hero section
        with ui.column().classes('header text-center py-16 mb-10').id('home'):
            ui.image('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop').classes('profile-image mx-auto mb-4')
            ui.label('John Doe').classes('text-3xl font-bold mb-2')
            ui.label('Machine Learning Engineer').classes('text-xl mb-4')
            ui.markdown("""
            Passionate ML Engineer with 7+ years of experience building and deploying machine learning solutions 
            that solve real-world problems. Expertise in predictive modeling, computer vision, and NLP.
            """).classes('max-w-2xl mx-auto')
            with ui.row().classes('justify-center gap-4 mt-6'):
                ui.button('View Projects', on_click=lambda: ui.navigate_to('#projects')).classes('bg-white text-purple-700 px-6 py-2 rounded-full')
                ui.button('Contact Me', on_click=lambda: ui.navigate_to('#contact')).classes('bg-transparent border border-white text-white px-6 py-2 rounded-full')
        
        # Projects section
        ui.label('Featured Projects').classes('text-2xl font-bold section-title').id('projects')
        with ui.grid(columns=2).classes('gap-6 my-8'):
            for project in ml_projects:
                with ui.card().classes('project-card'):
                    ui.image(project['image']).classes('w-full h-48 object-cover')
                    with ui.card_section():
                        ui.label(project['title']).classes('text-xl font-bold mb-2')
                        ui.label(project['description']).classes('text-gray-700 mb-4')
                        with ui.row().classes('flex-wrap gap-2 mb-4'):
                            for tech in project['technologies']:
                                ui.badge(tech).classes('bg-purple-100 text-purple-800')
                        with ui.row().classes('justify-between'):
                            ui.link('View Project', project['github']).classes('text-blue-600')
        
        # Skills section
        ui.label('Skills & Expertise').classes('text-2xl font-bold section-title').id('skills')
        with ui.grid(columns=2).classes('gap-6 my-8'):
            for skill, level in skills.items():
                with ui.column().classes('mb-4'):
                    with ui.row().classes('justify-between mb-1'):
                        ui.label(skill).classes('font-medium')
                        ui.label(f"{level}%").classes('text-gray-600')
                    with ui.row().classes('w-full bg-gray-200 rounded-full h-2.5'):
                        ui.element('div').classes(f'skill-bar').style(f'width: {level}%')
        
        # Experience section
        ui.label('Work Experience').classes('text-2xl font-bold section-title').id('experience')
        with ui.column().classes('my-8'):
            for exp in experiences:
                with ui.column().classes('experience-card'):
                    with ui.row().classes('justify-between'):
                        ui.label(exp['role']).classes('text-xl font-bold')
                        ui.label(exp['period']).classes('text-gray-600')
                    ui.label(exp['company']).classes('text-lg text-blue-600 mb-2')
                    ui.label(exp['description']).classes('text-gray-700')
        
        # Education section
        ui.label('Education').classes('text-2xl font-bold section-title')
        with ui.column().classes('my-8'):
            for edu in education:
                with ui.column().classes('mb-6'):
                    ui.label(edu['degree']).classes('text-xl font-bold')
                    with ui.row().classes('justify-between'):
                        ui.label(edu['institution']).classes('text-lg text-blue-600')
                        ui.label(edu['year']).classes('text-gray-600')
        
        # Contact section
        ui.label('Get In Touch').classes('text-2xl font-bold section-title').id('contact')
        with ui.grid(columns=2).classes('gap-6 my-8'):
            with ui.column():
                ui.markdown("""
                I'm always open to discussing new projects, opportunities, or partnerships.
                
                **Email:** john.doe@example.com  
                **Phone:** +1 (123) 456-7890  
                **Location:** San Francisco, CA
                """)
                with ui.row().classes('mt-4'):
                    ui.link('', 'https://github.com').classes('social-icon').style('font-family: "Font Awesome 5 Brands"; content: "\\f09b";')
                    ui.link('', 'https://linkedin.com').classes('social-icon').style('font-family: "Font Awesome 5 Brands"; content: "\\f08c";')
                    ui.link('', 'https://twitter.com').classes('social-icon').style('font-family: "Font Awesome 5 Brands"; content: "\\f099";')
            
            with ui.card().classes('contact-form'):
                ui.input('Name').classes('w-full mb-4')
                ui.input('Email').classes('w-full mb-4')
                ui.input('Subject').classes('w-full mb-4')
                ui.textarea('Message').classes('w-full mb-4').style('min-height: 150px')
                
                def handle_submit():
                    ui.notify('Message sent successfully! I will get back to you soon.', type='positive')
                
                ui.button('Send Message', on_click=handle_submit).classes('bg-blue-600 text-white')
        
        # Footer
        with ui.footer().classes('footer text-center w-full mt-10'):
            ui.label('© 2023 John Doe - ML Engineer Portfolio').classes('mb-2')
            ui.label('Built with Python and NiceGUI').classes('text-sm text-gray-400')

# Run the app
ui.run(title="ML Engineer Portfolio")