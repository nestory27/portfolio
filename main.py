import flet as ft
import webbrowser
import os
import pathlib

from websockets import route

# =========================
# BASIC INFO
# =========================
NAME = "SHIKONGO NESTORY IIYAMBO"
PROGRAMME = "Electrical Engineering"
MODULE = "Computer Programming I"
PROJECT = "PAVEMENT WATCH"
STUDENT_ID = "225056186"
GROUP = "GROUP 9"

GITHUB_URL = "https://github.com/flow141/UNAM-I3691CP-GROUP9-PAVEMENT_WATCH.git"
COMMITS_IMAGE_PATH = "Assets/Github/Commits.png"

# =========================
# MATLAB DATA - WITH .png EXTENSIONS
# =========================
MATLAB_COURSES = [
    {
        "id": "matlab-onramp",
        "title": "MATLAB Onramp",
        "certificate": "Assets/Matlab/MATLAB Onramp certificate.png",
        "report": "Assets/Matlab/MATLAB Onramp report.png",
    },
    {
        "id": "simulink-onramp",
        "title": "Simulink Onramp",
        "certificate": "Assets/Matlab/Simulink Onramp certificate.png",
        "report": "Assets/Matlab/Simulink Onramp report.png",
    },
    {
        "id": "vector-matrices",
        "title": "Calculations with Vectors and Matrices",
        "certificate": "Assets/Matlab/Calculations with Vectors and Matrices certificate.png",
        "report": "Assets/Matlab/Calculations with Vectors and Matrices report.png",
    },
    {
        "id": "explore-data",
        "title": "Explore Data with MATLAB Plots",
        "certificate": "Assets/Matlab/Explore Data with MATLAB Plots  certificate.png",
        "report": "Assets/Matlab/Explore Data with MATLAB Plots report.png",
    },
    {
        "id": "machine-learning",
        "title": "Machine Learning Onramp",
        "certificate": "Assets/Matlab/Machine Learning Onramp certificate.png",
        "report": "Assets/Matlab/Machine Learning Onramp report.png",
    },
    {
        "id": "writing-functions",
        "title": "The How and Why of Writing Functions",
        "certificate": "Assets/Matlab/The How and Why of Writing Functions certificate.png",
        "report": "Assets/Matlab/The How and Why of Writing Functions report.png",
    },
    {
        "id": "make-matrices",
        "title": "Make and Manipulate Matrices",
        "certificate": "Assets/Matlab/Make and Manipulate Matrices certificate.png",
        "report": "Assets/Matlab/Make and Manipulate Matrices report.png",
    },
]
# =========================
# NAV ITEM
# =========================
def nav_item(page, icon, label, route):
    return ft.Container(
        content=ft.Row(
            [
                ft.Icon(icon, size=18, color="#1f2937"),
                ft.Text(label, size=14, color="#1f2937"),
            ],
            spacing=12,
        ),
        padding=12,
        border_radius=12,
        bgcolor="#ffffff",
        on_click=lambda e: page.go(route),
    )




# =========================
# SIDEBAR
# =========================
def sidebar(page):
    return ft.Container(
        width=180,
        bgcolor="#0ce61e",
        padding=5,
        content=ft.Column(
            [
                nav_item(page, ft.Icons.HOME, "Home", "/"),
                nav_item(page, ft.Icons.SCHOOL, "MATLAB", "/matlab"),
                nav_item(page, ft.Icons.CODE, "GitHub", "/github"),
                nav_item(page, ft.Icons.ARTICLE, "Blog", "/blog"),
                nav_item(page, ft.Icons.TIMELINE, "Timeline", "/timeline"),
                nav_item(page, ft.Icons.PERSON, "About", "/about"),
            ],
            spacing=5,
        ),
    )

# =========================
# SHELL
# =========================
def page_shell(page, body):
    page.clean()
    
    # Set page scroll to OFF - we'll handle scrolling manually
    page.scroll = None
    
    # Create main layout with fixed sidebar and top bar
    main_layout = ft.Container(
        content=ft.Row(
            [
                # Fixed Sidebar - will not scroll
                ft.Container(
                    content=sidebar(page),
                    width=180,
                ),
                # Scrollable Content Area
                ft.Container(
                    content=ft.Column(
                        [
                            # Scrollable body
                            ft.Container(
                                content=body,
                                padding=20,
                                expand=True,
                            ),
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                    ),
                    expand=True,
                    bgcolor="#f8fafc",
                ),
            ],
            expand=True,
            spacing=0,
        ),
        expand=True,
    )
    
    # Create responsive top bar - text will shrink or wrap
    top = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    f"{NAME} | Portfolio", 
                    size=14,  # Smaller base size
                    weight="bold",
                    color="white",
                    overflow=ft.TextOverflow.ELLIPSIS,  # Add ... if too long
                ),
                ft.Container(expand=True),
                ft.Text(MODULE, size=10, color="white"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=10,  # Reduced padding
        bgcolor="#0ce61e",
    )
    
    # Add top bar and main layout
    page.add(
        ft.Column(
            [
                top,
                main_layout,
            ],
            expand=True,
            spacing=0,
        )
    )
    page.update()

## =========================
# HOME
# =========================
def home_view(page):
    import os

    page.scroll = "auto"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    profile_image_path = "Assets/profile/me1.jpeg"
    background_image_path = "Assets/profile/me3.jpeg"
    full_path = os.path.join(script_dir, profile_image_path)

    # Load image as bytes
    profile_image_bytes = None
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            profile_image_bytes = f.read()
        print(f"Profile image loaded, size: {len(profile_image_bytes)} bytes")
    else:
        print(f"Image not found at: {full_path}")
    # Load image as bytes
    background_image_bytes = None
    if os.path.exists(os.path.join(script_dir, background_image_path)):
        with open(os.path.join(script_dir, background_image_path), "rb") as f:
            background_image_bytes = f.read()
        print(f"Background image loaded, size: {len(background_image_bytes)} bytes")
    else:
        print(f"Image not found at: {os.path.join(script_dir, background_image_path)}")

    # Also load the same image for background
    background_bytes = background_image_bytes  

    page.clean()

    # Create circular profile picture container
    if profile_image_bytes:
        profile_display = ft.Container(
            content=ft.Image(
                src=profile_image_bytes,
                width=200,
                height=200,
                fit="cover",
            ),
            width=200,
            height=200,
            border_radius=100,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            bgcolor="#e0e0e0",
        )
    else:
        profile_display = ft.Container(
            content=ft.Text("📸", size=50),
            width=200,
            height=200,
            border_radius=100,
            bgcolor="#E61515",
            alignment=ft.alignment.center,
        )
    
    # Main content
    content = ft.Column(
        [
             # Top navigation bar
            ft.Container(
                content=ft.Row(
                    [
                        ft.Text(f"{NAME} | Portfolio", size=20, weight="bold", color="white"),
                        ft.Container(expand=True),
                        ft.Row(
                            [
                                ft.TextButton("MATLAB", on_click=lambda e: page.go("/matlab"), style=ft.ButtonStyle(color="white")),
                                ft.TextButton("Blog", on_click=lambda e: page.go("/blog"), style=ft.ButtonStyle(color="white")),
                                ft.TextButton("Timeline", on_click=lambda e: page.go("/timeline"), style=ft.ButtonStyle(color="white")),
                                ft.TextButton("GitHub", on_click=lambda e: page.go("/github"), style=ft.ButtonStyle(color="white")),
                                ft.TextButton("About", on_click=lambda e: page.go("/about"), style=ft.ButtonStyle(color="white")),
                            ],
                            spacing=5,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=15,
                bgcolor="#06d84c",
            ),
            
            # Main content area with padding
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                profile_display,
                                ft.Column(
                                    [
                                        ft.Text(
                                            NAME,
                                            size=38,
                                            weight=ft.FontWeight.BOLD,
                                            color="#F6F9FFFF",
                                        ),
                                        ft.Text(
                                            PROGRAMME,
                                            size=30,
                                            color="#1affba",
                                            weight=ft.FontWeight.W_500,
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ],
                            spacing=25,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        
                        ft.Divider(height=20, color="transparent"),
                        
                        ft.Column(
                            [
                                ft.Text(
                                    f"📚 Student ID: {STUDENT_ID}",
                                    size=25,
                                    color="#960424",
                                ),
                                ft.Text(
                                    f"📖 Module: {MODULE}",
                                    size=25,
                                    color="#c40010",
                                ),
                                ft.Text(
                                    f"🚀 Project: {PROJECT}",
                                    size=25,
                                    color="#0065f3",
                                ),
                                ft.Text(
                                    f"👥 Group: {GROUP}",
                                    size=25,
                                    color="#0f69cf",
                                ),
                            ],
                            spacing=8,
                        ),
                        
                        ft.Divider(height=20, color="transparent"),
                        
                        ft.Text(
                            "Electrical Engineering student passionate about UI design, "
                            "programming, and developing innovative solutions using MATLAB and Python.",
                            size=25,
                            color="#0717f7",
                        ),
                        
                        ft.Divider(height=20, color="transparent"),
                        
                        ft.Row(
                            [
                                ft.TextButton(
                                    "🎯 Skills",
                                    on_click=lambda e: page.go("/skills"),
                                    style=ft.ButtonStyle(
                                        color="#06d84c",
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                ),
                                ft.TextButton(
                                    "📋 Goals",
                                    on_click=lambda e: page.go("/goals"),
                                    style=ft.ButtonStyle(
                                        color="#06d84c",
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                ),
                                ft.TextButton(
                                    "📞 Contact",
                                    on_click=lambda e: page.go("/about"),
                                    style=ft.ButtonStyle(
                                        color="#06d84c",
                                        text_style=ft.TextStyle(size=25)
                                    ),
                                ),
                            ],
                            spacing=20,
                        ),
                    ],
                    spacing=2,
                ),
                padding=30,
                expand=True,
            ),
        ],
        expand=True,
        spacing=0,
    )
    
    # Method 1: Try using page.bgcolor with image bytes (if supported)
    try:
        page.bgcolor = ft.Colors.TRANSPARENT
        # Some versions support this
        page.decoration = ft.BoxDecoration(
            image=ft.DecorationImage(
                src=background_bytes,
                fit="cover",
            ),
        )
    except:
        # Method 2: If that fails, just use a gradient background
        try:
            page.decoration = ft.BoxDecoration(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#1a1a2e", "#16213e", "#0f3460"],
                ),
            )
        except:
            # Method 3: Simple color background
            page.bgcolor = "#1a1a2e"
    
    page.add(content)
    page.update()
# =========================
# SKILLS PAGE
# =========================
def skills_view(page):
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Home",
                        on_click=lambda e: page.go("/"),
                        style=ft.ButtonStyle(color="#00db54"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text(
                "My Skills",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#0A42BB",
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("💻 Programming Languages", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Python", size=16, color="#4b5563"),
                                ft.Text("• MATLAB", size=16, color="#4b5563"),
                                ft.Text("• C/C++", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=300,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("🛠️ Tools & Technologies", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Git & GitHub", size=16, color="#4b5563"),
                                ft.Text("• Simulink", size=16, color="#4b5563"),
                                ft.Text("• Flet Framework", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=300,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                wrap=True,
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("📊 Soft Skills", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Problem Solving", size=16, color="#4b5563"),
                                ft.Text("• Critical Thinking", size=16, color="#4b5563"),
                                ft.Text("• Team Collaboration", size=16, color="#4b5563"),
                                ft.Text("• Communication", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=300,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page_shell(page, body)


# =========================
# GOALS PAGE
# =========================
def goals_view(page):
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Home",
                        on_click=lambda e: page.go("/"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text(
                "My Portfolio Goals",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#111827",
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("📚 Academic Goals", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Complete MATLAB certifications", size=16, color="#4b5563"),
                                ft.Text("• Master Python programming", size=16, color="#4b5563"),
                                ft.Text("• Graduate with honors", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=350,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("💼 Career Goals", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Become a Software Engineer", size=16, color="#4b5563"),
                                ft.Text("• Work on innovative projects", size=16, color="#4b5563"),
                                ft.Text("• Contribute to open source", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=350,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                wrap=True,
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("🎯 Project Goals", size=20, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                                ft.Text("• Complete PAVEMENT WATCH project", size=16, color="#4b5563"),
                                ft.Text("• Build more engineering tools", size=16, color="#4b5563"),
                                ft.Text("• Create a strong portfolio", size=16, color="#4b5563"),
                            ],
                            spacing=10,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=10,
                        width=350,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page_shell(page, body)

# =========================
# ABOUT
# =========================
def about_view(page):
    import webbrowser
    import requests  # Add this import
    
    # Create input fields
    email_input = ft.TextField(
        hint_text="Your Email Address",
        label="Email",
        width=400,
        bgcolor="white",
        border_radius=5,
    )
    
    message_input = ft.TextField(
        hint_text="Your Message",
        label="Message",
        width=400,
        height=100,
        multiline=True,
        bgcolor="white",
        border_radius=5,
    )
    
    # Create the send button reference
    send_btn = ft.ElevatedButton(
        "Send Message",
        bgcolor="#159a73",
        color="white",
        width=200,
    )
    
    # Function to handle email sending via Formspree
    def send_email(e):
        email = email_input.value
        message = message_input.value
        
        if not email or not message:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please fill in both email and message fields"),
                bgcolor="red",
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # Disable button while sending
        send_btn.disabled = True
        page.update()
        
        try:
            # Send to Formspree
            response = requests.post(
                "https://formspree.io/f/xvzndqzz",  # Your Formspree endpoint
                data={
                    "email": email,
                    "message": message,
                },
                timeout=10
            )
            
            if response.status_code == 200:
                email_input.value = ""
                message_input.value = ""
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("✅ Message sent successfully!"),
                    bgcolor="#159a73",
                )
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"❌ Error {response.status_code}. Please try again."),
                    bgcolor="red",
                )
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"❌ Connection error: Check your internet"),
                bgcolor="red",
            )
        finally:
            send_btn.disabled = False
            page.snack_bar.open = True
            page.update()
    
    # Update the button's on_click
    send_btn.on_click = send_email
    
    body = ft.Column(
        [
            ft.Text("About Me", size=32, weight=ft.FontWeight.BOLD, color="#111827"),
            ft.Divider(height=10, color="transparent"),
            
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("👨‍🎓 Who I Am", size=22, weight=ft.FontWeight.BOLD, color="#159a73"),
                        ft.Text(
                            f"I am {NAME}, an {PROGRAMME} student at the University of Namibia.",
                            size=15, color="#4b5563",
                        ),
                    ],
                    spacing=10,
                ),
                padding=20,
                bgcolor="#f8fafc",
                border_radius=10,
            ),
            
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("📞 Contact Information", size=22, weight=ft.FontWeight.BOLD, color="#0A42BB"),
                        
                        ft.Row(
                            [
                                ft.Text("📱 WhatsApp:", size=15, weight=ft.FontWeight.BOLD, color="#0cb0e2"),
                                ft.TextButton(
                                    "+264 81 402 4415 (Tap to WhatsApp)",
                                    on_click=lambda e: webbrowser.open("https://wa.me/264814024415"),
                                    style=ft.ButtonStyle(color="#25D366"),
                                ),
                            ],
                            spacing=10,
                        ),
                        
                        ft.Row(
                            [
                                ft.Text("✉️ Email:", size=15, weight=ft.FontWeight.BOLD, color="#ffffff"),
                                ft.Text("nestoryshikongo27@gmail.com", size=15, color="#159a73"),
                            ],
                            spacing=10,
                        ),
                        
                        ft.Row(
                            [
                                ft.Text("🐙 GitHub:", size=15, weight=ft.FontWeight.BOLD, color="#4b5563"),
                                ft.TextButton(
                                    "github.com/flow141",
                                    on_click=lambda e: webbrowser.open("https://github.com/flow141"),
                                    style=ft.ButtonStyle(color="#159a73"),
                                ),
                            ],
                            spacing=10,
                        ),
                    ],
                    spacing=15,
                ),
                padding=20,
                bgcolor="#f8fafc",
                border_radius=10,
            ),
            
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("✉️ Send Me a Message", size=22, weight=ft.FontWeight.BOLD, color="#159a73"),
                        ft.Text("I'll get back to you as soon as possible!", size=14, color="#6b7280"),
                        ft.Divider(height=10, color="transparent"),
                        email_input,
                        message_input,
                        send_btn,
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                bgcolor="#f8fafc",
                border_radius=10,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page_shell(page, body)


# =========================
# BLOG
# =========================

def blog_view(page: ft.Page):
    """Blog view with technical articles and video links"""
    
    # Helper function to get icon with consistent color
    def get_icon(icon_name, color="#159a73"):
        # Use ft.icons.ICON_NAME or pass icon name as first argument
        # Get the icon constant from ft.icons if it exists, otherwise use string
        try:
            # Try to get the icon constant (e.g., ft.icons.CODE)
            icon_constant = getattr(ft.icons, icon_name.upper())
            return ft.Icon(icon_constant, size=38, color=color)
        except AttributeError:
            # Fallback to emoji if icon constant not found
            emoji_map = {
                "code": "💻",
                "storage": "🗄️", 
                "play_circle": "▶️",
                "functions": "📐"
            }
            return ft.Text(emoji_map.get(icon_name.lower(), "📄"), size=38)
        
        # Function to open ScreenPal video
    def open_video_player(e):
        # Your ScreenPal video link
        video_url = "https://go.screenpal.com/watch/cO12ltnu4vt"
        webbrowser.open(video_url)
    
    # Create the blog content
    blog_content = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Home",
                        on_click=lambda e: page.go("/"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Text("Technical Blog", size=42, weight=ft.FontWeight.BOLD, color="#111827"),
            ft.Text(
                "Confidence in Concepts — written technical explanations with video inserts.",
                size=16, 
                color="#6b7280"
            ),
            ft.Divider(height=20, color="transparent"),
            
            # Blog Post 1: Backend Development
            ft.Container(
                bgcolor="white",
                border_radius=12,
                padding=28,
                content=ft.Column(
                    spacing=14,
                    controls=[
                        get_icon("code", "#159a73"),
                        ft.Text("Understanding Backend Development with Wirebass", size=22,
                                weight=ft.FontWeight.BOLD, color="#111827"),
                        ft.Text(
                            "Wirebass is a lightweight backend framework that helps developers build "
                            "RESTful APIs quickly and efficiently. It handles routing, middleware, and "
                            "request/response processing, allowing you to focus on your application logic. "
                            "In our group project, I used Wirebass to create the backend endpoints that serve "
                            "data to the frontend.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text(
                            "The key concepts I learned include route definition, request validation, "
                            "authentication middleware, and database integration. Wirebass uses a simple "
                            "decorator-based syntax that makes API development intuitive and maintainable. "
                            "I implemented endpoints for user authentication, data retrieval, and file uploads.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text("Watch: Backend Development Explained", size=13,
                                color="#159a73", italic=True),
                        ft.ElevatedButton(
                            "▶ Watch Video",
                            bgcolor="#159a73",
                            color="white",
                            on_click=lambda _: webbrowser.open(
                                "https://www.youtube.com/watch?v=JeznW_7DlB0"
                            ),
                        ),
                    ],
                ),
            ),
            
            ft.Divider(height=10, color="transparent"),
            
            # Blog Post 2: API Design
            ft.Container(
                bgcolor="white",
                border_radius=12,
                padding=28,
                content=ft.Column(
                    spacing=14,
                    controls=[
                        get_icon("storage", "#159a73"),
                        ft.Text("API Design Best Practices", size=22,
                                weight=ft.FontWeight.BOLD, color="#111827"),
                        ft.Text(
                            "API design is crucial for building scalable and maintainable applications. "
                            "RESTful principles guide how we structure endpoints, use HTTP methods, "
                            "and handle responses. A well-designed API uses proper status codes, "
                            "consistent naming conventions, and clear documentation.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text(
                            "In our project, I designed endpoints following REST conventions: "
                            "GET for retrieving data, POST for creating resources, PUT/PATCH for updates, "
                            "and DELETE for removal. I also implemented proper error handling with "
                            "meaningful status codes (200 OK, 201 Created, 400 Bad Request, 404 Not Found) "
                            "to help frontend developers integrate smoothly.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text("Watch: API Design Fundamentals", size=13,
                                color="#159a73", italic=True),
                        ft.ElevatedButton(
                            "▶ Watch Video",
                            bgcolor="#159a73",
                            color="white",
                            on_click=lambda _: webbrowser.open(
                                "https://www.youtube.com/watch?v=pkYVOmU3MgA"
                            ),
                        ),
                    ],
                ),
            ),
            
            ft.Divider(height=10, color="transparent"),
            
            # Blog Post 3: Git and GitHub
            ft.Container(
                bgcolor="white",
                border_radius=12,
                padding=28,
                content=ft.Column(
                    spacing=14,
                    controls=[
                        get_icon("play_circle", "#159a73"),
                        ft.Text("Version Control with Git and GitHub", size=22,
                                weight=ft.FontWeight.BOLD, color="#111827"),
                        ft.Text(
                            "Version control is essential for collaborative software development. "
                            "Git allows teams to track changes, work on features in isolation using branches, "
                            "and merge code safely through pull requests. In Group 8, we used GitHub to "
                            "manage our codebase and coordinate our work.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text(
                            "I learned how to create branches for new features, commit changes with "
                            "meaningful messages, push to remote repositories, and submit pull requests "
                            "for code review. This workflow ensures that all code is reviewed before "
                            "being merged into the main branch, maintaining code quality and preventing conflicts.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Text("Watch: Git and GitHub Tutorial", size=13,
                                color="#159a73", italic=True),
                        ft.ElevatedButton(
                            "▶ Watch Video",
                            bgcolor="#159a73",
                            color="white",
                            on_click=lambda _: webbrowser.open(
                                "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"  # Replace with actual video ID
                            ),
                        ),
                    ],
                ),
            ),
            
            ft.Divider(height=10, color="transparent"),
            
            # Blog Post 4: Mathematical Notation
            ft.Container(
                bgcolor="#f0fdf4",  # Light green background for emphasis
                border_radius=12,
                padding=28,
                content=ft.Column(
                    spacing=12,
                    controls=[
                        get_icon("functions", "#159a73"),
                        ft.Text("Mathematical Notation in Engineering", size=30,
                                weight=ft.FontWeight.BOLD, color="#159a73"),
                        ft.Text(
                            "In engineering applications, mathematical formulas are essential for calculations. "
                            "Here's the formula for calculating the efficiency of a system:",
                            size=15, color="#e3e6eb",
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Efficiency = (Output Energy / Input Energy) × 100%",
                                size=26, 
                                color="#000000", 
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            padding=20,
                            bgcolor="white",
                            border_radius=10,
                        ),
                        ft.Text(
                            "Where Output Energy is the useful energy delivered by the system, "
                            "and Input Energy is the total energy supplied to the system. "
                            "Efficiency is expressed as a percentage between 0% and 100%.",
                            size=15, color="#e3e6eb",
                        ),
                    ],
                ),
            ),
            
            # NEW: Local Video Button - Added at the bottom
            ft.Divider(height=20, color="transparent"),
            ft.Container(
                bgcolor="white",
                border_radius=12,
                padding=28,
                content=ft.Column(
                    spacing=14,
                    controls=[
                        ft.Text("🎬", size=38),
                        ft.Text("Watch Project Self-Reflection video", size=22,
                                weight=ft.FontWeight.BOLD, color="#000000"),
                        ft.Text(
                            "Click the button below to watch the local video file from your Assets/Blog folder.",
                            size=15, color="#e3e6eb",
                        ),
                        ft.ElevatedButton(
                            "▶ Play Local Video",
                            bgcolor="#159a73",
                            color="white",
                            on_click=open_video_player,
                        ),
                    ],
                ),
            ),
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    # Use page_shell to maintain consistent layout with sidebar
    page_shell(page, blog_content)


# =========================
# VIDEO PLAYER VIEW
# =========================
def video_player_view(page: ft.Page, video_url):
    """View to play video using ScreenPal link"""
    
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Blog",
                        on_click=lambda e: page.go("/blog"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Text(
                "Video Player",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#000000",
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("🎬", size=80),
                        ft.Text(
                            "Click the button below to watch the video",
                            size=18,
                            color="#000000",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Divider(height=20, color="transparent"),
                        ft.ElevatedButton(
                            "▶ Play Video",
                            bgcolor="#159a73",
                            color="white",
                            on_click=lambda _: webbrowser.open(video_url),
                            width=250,
                        ),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=40,
                bgcolor="white",
                border_radius=12,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
    page_shell(page, body)
# =========================
# GITHUB HELPER FUNCTIONS
# =========================
def open_url(url):
    """Open URL in default browser"""
    webbrowser.open(url)


def load_image_bytes(path):
    abs_path = os.path.abspath(path)
    if os.path.exists(abs_path):
        with open(abs_path, "rb") as f:
            return f.read()
    return None


# =========================
# GITHUB VIEW
# =========================
def github_view(page):
    # GitHub profile image path
    profile_image_path = "Assets/Github/profile.png"
    profile_full_path = os.path.abspath(profile_image_path)
    
    # Load image as bytes
    profile_image_bytes = None
    if os.path.exists(profile_full_path):
        with open(profile_full_path, "rb") as f:
            profile_image_bytes = f.read()
        print(f"Loaded profile image, size: {len(profile_image_bytes)} bytes")
    else:
        print(f"Profile image not found at: {profile_full_path}")
    
    # List files in directory for debugging
    github_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Assets", "Github")
    if os.path.exists(github_dir):
        print(f"Files in {github_dir}:")
        for file in os.listdir(github_dir):
            print(f"  - {file}")
    
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Home",
                        on_click=lambda e: page.go("/"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            
            # GitHub Profile Section
            ft.Row(
                [
                    ft.Column(
                        [
                            # Profile Image - Using bytes for reliability
                            ft.Container(
                                content=ft.Image(
                                    src=profile_image_bytes if profile_image_bytes else None,
                                    width=100,
                                    height=100,
                                    fit="contain",
                                    error_content=ft.Text("👤", size=50),
                                ),
                                width=100,
                                height=100,
                                border_radius=50,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                bgcolor="#e0e0e0",
                            ),
                            ft.Text(
                                "nestory27",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color="#111827",
                            ),
                            ft.Text(
                                "GitHub Profile",
                                size=14,
                                color="#6b7280",
                            ),
                        ],
                        spacing=10,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.Divider(height=10, color="transparent"),
            
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("GitHub", size=32, weight=ft.FontWeight.BOLD, color="#111827"),
                            ft.Text("Project Repository", size=16, color="#6b7280"),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.Divider(height=20, color="transparent"),
            
            # Open Repository Button
            ft.Row(
                [
                    ft.ElevatedButton(
                        "🔗 Open Repository on GitHub",
                        on_click=lambda e: open_url(GITHUB_URL),
                        bgcolor="#159a73",
                        color="white",
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.Divider(height=30, color="transparent"),
            
            # Title for documentation section
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "Documentation & Activity",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#111827",
                            ),
                            ft.Text(
                                "View commits, pull requests, and push history",
                                size=14,
                                color="#6b7280",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.Divider(height=20, color="transparent"),
            
            # Buttons Row for different sections
            ft.Row(
                [
                    # Commits Button
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("📝", size=40),
                                ft.Text("Commits", size=16, weight=ft.FontWeight.BOLD, color="#24292e"),
                                ft.Text("View commit history", size=12, color="#6b7280"),
                            ],
                            spacing=8,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=12,
                        ink=True,
                        on_click=lambda e: page.go("/github/commits"),
                        width=180,
                        height=140,
                    ),
                    
                    # Pull Requests Button
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("🔄", size=40),
                                ft.Text("Pull Requests", size=16, weight=ft.FontWeight.BOLD, color="#6f42c1"),
                                ft.Text("View PR history", size=12, color="#6b7280"),
                            ],
                            spacing=8,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=12,
                        ink=True,
                        on_click=lambda e: page.go("/github/pull-requests"),
                        width=180,
                        height=140,
                    ),
                    
                    # Push Request Button
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("📤", size=40),
                                ft.Text("Push History", size=16, weight=ft.FontWeight.BOLD, color="#cb2431"),
                                ft.Text("View push activity", size=12, color="#6b7280"),
                            ],
                            spacing=8,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        bgcolor="#f8fafc",
                        border_radius=12,
                        ink=True,
                        on_click=lambda e: page.go("/github/push"),
                        width=180,
                        height=140,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30,
                wrap=True,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    page_shell(page, body)


# =========================
# GITHUB COMMITS VIEW
# =========================
def github_commits_view(page):
    # Define image paths for commits
    commits_images = [
        {"path": "Assets/Github/commits.png", "title": "Commits Overview"},
        {"path": "Assets/Github/commits 1.png", "title": "Commits Details"},
    ]
    
    # Filter to only existing images and load bytes (works in web & desktop)
    existing_images = []
    for img in commits_images:
        full_path = os.path.abspath(img["path"])
        if os.path.exists(full_path):
            image_data = load_image_bytes(full_path)
            if image_data is not None:
                img["data"] = image_data
                existing_images.append(img)
    
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to GitHub",
                        on_click=lambda e: page.go("/github"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "GitHub Commits History",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color="#111827",
                            ),
                            ft.Text(
                                "View all commit activity and history",
                                size=14,
                                color="#6b7280",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Divider(height=20, color="transparent"),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    # Add image containers
    for img in existing_images:
        body.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(img["title"], size=20, weight=ft.FontWeight.BOLD, color="#159a73"),
                        ft.Container(
                            content=ft.Image(
                                src=img.get("data"),
                                width=800,
                                height=500,
                                fit="contain",
                                error_content=ft.Text("Image failed to load", color="red"),
                            ),
                            padding=20,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor="white",
                border_radius=12,
                padding=20,
                margin=10,
            )
        )
    
    if not existing_images:
        body.controls.append(
            ft.Text("No commit images found in Assets/Github/", size=16, color="red")
        )
    
    page_shell(page, body)


# =========================
# GITHUB PULL REQUESTS VIEW
# =========================
def github_pull_requests_view(page):
    # Define image paths for pull requests
    pr_images = [
        {"path": "Assets/Github/pull request.png", "title": "Pull Requests Overview"},
        {"path": "Assets/Github/pull request 1.png", "title": "Pull Requests Details"},
    ]
    
    # Filter to only existing images and load bytes
    existing_images = []
    for img in pr_images:
        full_path = os.path.abspath(img["path"])
        if os.path.exists(full_path):
            image_data = load_image_bytes(full_path)
            if image_data is not None:
                img["data"] = image_data
                existing_images.append(img)
    
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to GitHub",
                        on_click=lambda e: page.go("/github"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "GitHub Pull Requests",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color="#111827",
                            ),
                            ft.Text(
                                "View all pull request activity",
                                size=14,
                                color="#6b7280",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Divider(height=20, color="transparent"),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    # Add image containers
    for img in existing_images:
        body.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(img["title"], size=20, weight=ft.FontWeight.BOLD, color="#6f42c1"),
                        ft.Container(
                            content=ft.Image(
                                src=img.get("data"),
                                width=800,
                                height=500,
                                fit="contain",
                                error_content=ft.Text("Image failed to load", color="red"),
                            ),
                            padding=20,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor="white",
                border_radius=12,
                padding=20,
                margin=10,
            )
        )
    
    if not existing_images:
        body.controls.append(
            ft.Text("No pull request images found in Assets/Github/", size=16, color="red")
        )
    
    page_shell(page, body)



# =========================
# GITHUB PUSH VIEW
# =========================
def github_push_view(page):
    # Define image paths for push
    push_images = [
        {"path": "Assets/Github/push request.png", "title": "Push History"},
    ]
    
    # Filter to only existing images
    existing_images = []
    for img in push_images:
        full_path = os.path.abspath(img["path"])
        if os.path.exists(full_path):
            image_data = load_image_bytes(full_path)
            if image_data is not None:
                img["data"] = image_data
                existing_images.append(img)
    
    # Create body FIRST before using it
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to GitHub",
                        on_click=lambda e: page.go("/github"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                "GitHub Push History",
                                size=32,
                                weight=ft.FontWeight.BOLD,
                                color="#111827",
                            ),
                            ft.Text(
                                "View push activity to repository",
                                size=14,
                                color="#6b7280",
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Divider(height=20, color="transparent"),
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    # Add image containers
    for img in existing_images:
        body.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(img["title"], size=20, weight=ft.FontWeight.BOLD, color="#cb2431"),
                        ft.Container(
                            content=ft.Image(
                                src=img.get("data"),
                                width=800,
                                height=500,
                                fit="contain",
                                error_content=ft.Text("Image failed to load", color="red"),
                            ),
                            padding=20,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor="white",
                border_radius=12,
                padding=20,
                margin=10,
            )
        )
    
    if not existing_images:
        body.controls.append(
            ft.Text("No push request images found in Assets/Github/", size=16, color="red")
        )
    
    page_shell(page, body)
# =========================
# TIMELINE
# =========================
def timeline_view(page):
    timeline_items = [
        ("Week 1", "Project planning, team discussions on requirements and design and role assignment"),
        ("Week 2", "Designed UI and implemented core features"),
        ("Week 3", "Integrated backend and frontend components"),
        ("Week 4", "Testing, debugging, and documentation"),
        ("Week 5", "Final touches and project submission and Presentation"),
    ]
    
    timeline_controls = []
    for i, (week, description) in enumerate(timeline_items):
        timeline_controls.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(str(i+1), size=18, weight=ft.FontWeight.BOLD, color="white"),
                            width=40,
                            height=40,
                            bgcolor="#0f766e",
                            border_radius=20,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(week, size=18, weight=ft.FontWeight.BOLD, color="#0f766e"),
                                ft.Text(description, size=14, color="#4b5563"),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=15,
                ),
                padding=15,
                bgcolor="#f0fdf4",
                border_radius=10,
            )
        )
        if i < len(timeline_items) - 1:
            timeline_controls.append(
                ft.Container(
                    content=ft.Icon(ft.Icons.ARROW_DOWNWARD, color="#0f766e", size=20),
                    padding=5,
                )
            )
    
    content = ft.Column(
        controls=[
            ft.Text(
                "Project Timeline",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#0f766e",
            ),
            ft.Text(
                "Development journey and milestones",
                size=16,
                color="#6b7280",
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Column(
                timeline_controls,
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page_shell(page, content)

# =========================
# MATLAB PAGE - SINGLE VERSION
# =========================
def matlab_view(page):
    items = []

    for course in MATLAB_COURSES:
        def make_click_handler(c):
            return lambda e: page.go(f"/matlab/{c['id']}")
        
        items.append(
            ft.Container(
                bgcolor="white",
                padding=20,
                border_radius=10,
                width=300,
                ink=True,
                on_click=make_click_handler(course),  # Different approach to avoid lambda issues
                content=ft.Column(
                    [
                        ft.Text(
                            "📘",
                            size=48,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            course["title"],
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="#111827",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Certificate & Report available",
                            size=13,
                            color="#6b7280",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Text(
                            "Click to View Course",
                            size=14,
                            weight=ft.FontWeight.W_500,
                            color="#0072BD",
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    spacing=12,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        )

    body = ft.Column(
        [
            ft.Text(
                "MATLAB Achievement Hub",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="#111827",
            ),
            ft.Text(
                "Click any course to view certificates and reports.",
                size=16,
                color="#6b7280",
            ),
            ft.Row(
                items,
                wrap=True,
                spacing=20,
                run_spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page_shell(page, body)


# =========================
# MATLAB COURSE DETAIL VIEW
# =========================
def matlab_course_view(page, course_id):
    """Display certificate and report for a specific course"""
    
    # Find the course data
    course_data = None
    for course in MATLAB_COURSES:
        if course["id"] == course_id:
            course_data = course
            break
    
    if not course_data:
        page.go("/matlab")
        return
    
    # Load certificate image as bytes
    cert_path = os.path.abspath(course_data["certificate"])
    report_path = os.path.abspath(course_data["report"])
    
    cert_bytes = None
    report_bytes = None
    
    if os.path.exists(cert_path):
        with open(cert_path, "rb") as f:
            cert_bytes = f.read()
        print(f"Loaded certificate: {cert_path}, size: {len(cert_bytes)} bytes")
    else:
        print(f"Certificate not found at: {cert_path}")
    
    if os.path.exists(report_path):
        with open(report_path, "rb") as f:
            report_bytes = f.read()
        print(f"Loaded report: {report_path}, size: {len(report_bytes)} bytes")
    else:
        print(f"Report not found at: {report_path}")
    
    body = ft.Column(
        [
            ft.Row(
                [
                    ft.TextButton(
                        "← Back to Courses",
                        on_click=lambda e: page.go("/matlab"),
                        style=ft.ButtonStyle(color="#159a73"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Divider(height=10, color="transparent"),
            ft.Text(
                course_data["title"],
                size=28,
                weight=ft.FontWeight.BOLD,
                color="#111827",
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text(
                "Your Achievements",
                size=20,
                weight=ft.FontWeight.W_600,
                color="#111827",
            ),
            ft.Text(
                f"View your {course_data['title']} certificate and progress report below.",
                size=14,
                color="#6b7280",
            ),
            
            # Certificate Section
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Certificate", 
                            size=18, 
                            weight=ft.FontWeight.BOLD,
                            color="#159a73",
                        ),
                        ft.Container(
                            content=ft.Image(
                                src=cert_bytes if cert_bytes else None,
                                width=700,
                                height=500,
                                fit="contain",
                                error_content=ft.Text(
                                    "❌ Certificate image not found\nPlease check file path", 
                                    size=14, 
                                    color="red",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                            padding=20,
                            bgcolor="#f8fafc",
                            border_radius=10,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
            ),
            
            # Progress Report Section
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Progress Report", 
                            size=18, 
                            weight=ft.FontWeight.BOLD,
                            color="#159a73",
                        ),
                        ft.Container(
                            content=ft.Image(
                                src=report_bytes if report_bytes else None,
                                width=700,
                                height=500,
                                fit="contain",
                                error_content=ft.Text(
                                    "❌ Report image not found\nPlease check file path", 
                                    size=14, 
                                    color="red",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                            padding=20,
                            bgcolor="#f8fafc",
                            border_radius=10,
                        ),
                    ],
                    spacing=10,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
            ),
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    
    page_shell(page, body)


# =========================
# ROUTING
# =========================
def main(page: ft.Page):
    page.title = "Engineering Portfolio"
    page.scroll = "auto"

    def route_change(e=None):
        current_route = page.route  # Changed variable name to avoid conflict

        if current_route == "/":
            home_view(page)
        elif current_route == "/about":
            about_view(page)
        elif current_route == "/blog":
            blog_view(page)
        elif current_route == "/github":
            github_view(page)
        elif current_route == "/github/commits":
            github_commits_view(page)
        elif current_route == "/github/pull-requests":
            github_pull_requests_view(page)
        elif current_route == "/github/push":
            github_push_view(page)
        elif current_route == "/video-player":
            # Open the ScreenPal video in browser
            webbrowser.open("https://go.screenpal.com/watch/cO12ltnu4vt")
            page.go("/blog")  # Go back to blog after opening 
        elif current_route == "/timeline":
            timeline_view(page)
        elif current_route == "/matlab":
            matlab_view(page)
        elif current_route.startswith("/matlab/") and current_route != "/matlab":
            course_id = current_route.split("/")[-1]
            matlab_course_view(page, course_id)
        elif current_route == "/skills": 
            skills_view(page)
        elif current_route == "/goals":
            goals_view(page)
        else:
            page.go("/")

    page.on_route_change = route_change
    
    # Initial route handling
    if page.route in ("/", ""):
        route_change()
    else:
        page.go(page.route)


if __name__ == "__main__":
    import os

    # Use the PORT provided by Render (or default to 8501 locally)
    port = int(os.environ.get("PORT", 8501))
    host = "0.0.0.0"

    # For server deployment use the web browser view and bind to host/port
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host=host, port=port)