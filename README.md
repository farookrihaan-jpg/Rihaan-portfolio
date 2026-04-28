# Mohammed Rihaan M - Portfolio Website

## Overview
A professional Django-based portfolio website showcasing skills, projects, education, and contact information.

## Tech Stack
- **Framework**: Django 5.2.12
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with professional dark theme
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)

## Features

### 1. Hero Section
- Professional introduction with name and role
- Call-to-action buttons
- Smooth scroll indicator
- Gradient text effects

### 2. About Section
- Detailed professional summary
- Skills overview
- Career journey

### 3. Skills Section
- Visual skill bars with percentages
- Animated progress bars
- Skills: HTML (90%), CSS (85%), JavaScript (80%), React (85%), Python (95%), Django (90%), SQL (85%)

### 4. Projects Section
- **Diamond Academy**: Tuition centre management system
- **CSI Church Website**: Church website with event management
- Technology badges for each project

### 5. Education Section
- B.E Mechanical and Automation Engineering - Sri Sairam Engineering College
- Python Full Stack Developer Certification - SLA Institute
- Timeline-style layout with icons

### 6. Contact Section
- Contact information display
- Working contact form
- Social media links (LinkedIn, GitHub, Email)
- Form stores messages in database

### 7. Footer
- Professional branding
- Social media links
- Copyright information

## Project Structure

```
/app/backend/
├── portfolio_site/          # Django project settings
│   ├── settings.py         # Main settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── portfolio/              # Main app
│   ├── models.py          # ContactMessage model
│   ├── views.py           # View logic
│   ├── forms.py           # Contact form
│   ├── urls.py            # App URLs
│   ├── admin.py           # Admin configuration
│   └── templates/         # HTML templates
│       └── portfolio/
│           ├── base.html  # Base template
│           └── home.html  # Homepage
├── static/                # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── main.js       # JavaScript functionality
├── db.sqlite3            # Database
└── manage.py             # Django management script
```

## Installation & Setup

### Prerequisites
- Python 3.11+
- Django 5.2.12
- pip

### Installation Steps

1. **Install dependencies**:
```bash
cd /app/backend
pip install -r requirements.txt
```

2. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create superuser** (optional, for admin access):
```bash
python manage.py createsuperuser
```

4. **Collect static files**:
```bash
python manage.py collectstatic --noinput
```

5. **Run the development server**:
```bash
python manage.py runserver 0.0.0.0:3000
```

## Running the Application

The application is configured to run via Supervisor:

```bash
# Start Django
sudo supervisorctl start django

# Stop Django
sudo supervisorctl stop django

# Restart Django
sudo supervisorctl restart django

# Check status
sudo supervisorctl status
```

## Access Points

- **Website**: https://71f55c5c-3e12-4252-af3c-34c9bafeafd4.preview.emergentagent.com
- **Admin Panel**: https://71f55c5c-3e12-4252-af3c-34c9bafeafd4.preview.emergentagent.com/admin/
- **Local Access**: http://localhost:3000

## Contact Form

When users submit the contact form, messages are stored in the database under the `ContactMessage` model. You can view these messages via:

1. **Django Admin Panel**:
   - Create a superuser: `python manage.py createsuperuser`
   - Login at `/admin/`
   - Navigate to "Portfolio" → "Contact Messages"

2. **Database**:
   - Messages are stored in `db.sqlite3`
   - Model: `portfolio.ContactMessage`
   - Fields: name, email, subject, message, created_at

## Design Features

### Color Scheme (Professional Dark Theme)
- Primary Black: `#0a0a0a`
- Secondary Black: `#121212`
- Dark Grey: `#1a1a1a`
- Medium Grey: `#2a2a2a`
- Light Grey: `#3a3a3a`
- Text Primary: `#ffffff`
- Text Secondary: `#a0a0a0`
- Accent Color: `#4a4a4a`

### Typography
- Font Family: Inter (Google Fonts)
- Weights: 300, 400, 500, 600, 700, 800

### Animations
- Smooth scroll navigation
- Hover effects on cards and buttons
- Animated skill bars on scroll
- Fade-in animations for sections
- Bounce animation for scroll indicator

### Responsive Design
- Mobile-first approach
- Breakpoints:
  - Desktop: 1200px+
  - Tablet: 968px
  - Mobile: 640px and below
- Hamburger menu for mobile navigation
- Responsive grid layouts

## Customization

### Updating Content

Edit `/app/backend/portfolio/views.py` to update:
- Name and role
- Skills and percentages
- Projects and descriptions
- Education details
- Contact information

### Styling

Edit `/app/backend/static/css/style.css` to modify:
- Colors and theme
- Typography
- Spacing and layout
- Animations

### Adding New Sections

1. Add HTML to `/app/backend/portfolio/templates/portfolio/home.html`
2. Add styles to `/app/backend/static/css/style.css`
3. Add navigation link in the navbar
4. Update JavaScript in `/app/backend/static/js/main.js` if needed

## Database Models

### ContactMessage
```python
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

## Key Files Explained

### settings.py
- Django configuration
- Database settings (SQLite3)
- Static files configuration
- Installed apps
- Middleware settings

### views.py
- `home()`: Renders the homepage with all content
- `contact()`: Handles contact form submissions

### forms.py
- `ContactForm`: ModelForm for contact submissions

### main.js
- Smooth scroll navigation
- Mobile menu toggle
- Navbar background on scroll
- Skill bar animations
- Section fade-in effects
- Active nav link highlighting

## Troubleshooting

### Issue: Static files not loading
```bash
python manage.py collectstatic --noinput
sudo supervisorctl restart django
```

### Issue: Database errors
```bash
python manage.py migrate
```

### Issue: Server not starting
```bash
# Check logs
tail -f /var/log/supervisor/django.err.log

# Restart supervisor
sudo supervisorctl restart django
```

## Performance Optimizations

1. **Static Files**: Collected and served efficiently
2. **CSS**: Minified and optimized
3. **Images**: Optimized with Font Awesome icons (no heavy images)
4. **JavaScript**: Vanilla JS (no heavy libraries)
5. **Animations**: CSS transitions and transforms for smooth performance

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Security Features

- CSRF protection enabled
- XSS protection
- Secure headers configured
- Email validation on forms
- SQL injection protection via Django ORM

## Future Enhancements (Optional)

1. Add email notification when contact form is submitted
2. Add portfolio project detail pages
3. Add blog section
4. Add dark/light theme toggle
5. Add downloadable resume/CV
6. Add animations using AOS library
7. Add project images/screenshots
8. Add testimonials section

## Support & Maintenance

For updates or modifications:
1. Edit content in `views.py`
2. Update styles in `style.css`
3. Run `collectstatic` after CSS/JS changes
4. Restart Django server

## License

Personal portfolio website for Mohammed Rihaan M.

---

**Built with Django & deployed on Emergent Platform**
**Last Updated**: April 2026
