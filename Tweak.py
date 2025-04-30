
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
dark_violet = "\033[38;5;91m"
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
import requests
import requests
import random
import string
import os
try:
    with open("/sdcard/boostphere/generated_code.txt", "r") as file:
        code = file.read().strip()
except FileNotFoundError:
    code = "[red]File not found[/red]"
except Exception as e:
    code = f"[red]Error: {e}[/red]"
CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def ensure_file_exists():
    """Ensure that the code file exists by creating it if it doesn't exist."""
    open(CODE_FILE, 'a').write('')  # This will create the file if it doesn't exist, but won't modify it.

def generate_code():
    """Generate a unique code in the format BOOSTPHERE-XXX-XXXXX."""
    prefix = "TWEAK"
    number_part = ''.join(random.choices(string.digits, k=3))  # 3 random digits
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # 5 alphanumeric characters
    code = f"{prefix}-{number_part}-{letters_part}"
    return code

def save_code(code):
    """Save the generated code to a file."""
    with open(CODE_FILE, 'w') as file:
        file.write(code)

def load_code():
    """Load the code from the file, if it exists."""
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    """Check if the generated code is approved by fetching the approval list."""
    try:
        response = requests.get("https://pastebin.com/raw/UE9bGHU2")
        response.raise_for_status()  # Raise an error for bad responses
        approved_codes = response.text.splitlines()  # Split the response into lines
        
        # Remove comments and strip whitespace, then check for the code
        approved_codes = [line.split('#')[0].strip() for line in approved_codes if line]
        return code in approved_codes  # Check if the code is in the approved list
    except requests.RequestException as e:
        pass
        return False


def generate_and_check_code():
    """Generate a code if not existing, check if it's approved, then run main()."""
    ensure_file_exists()  # Ensure the code file exists before proceeding
    
    code = load_code()
    
    if code is None or code == '':
        code = generate_code()
        save_code(code)
        console.clear()
        banner()
        
        msg = Text.assemble(
            (f"YOUR GENERATED CODE: ", "yellow"),
            (f"{code}", "red")
        )
        console.log(Panel(msg, border_style="cyan", title="🔐 Generated Code"))
    else:
        
        banner()
        
        msg = Text.assemble(
            (f"YOUR CODE: ", yellow),
            (f"{code}", red)
        )
        console.log(Panel(msg, border_style="yellow", title="🔐 Loaded Code"))

    if is_code_approved(code):
        banner()
    else:
        
        warn_msg = Text.assemble(


           ("CODE IS NOT APPROVED! ", "red"),
           ("PLEASE SEND IT TO: ", "white"),
           ("https://www.facebook.com/profile.php?id=100078043222260", "green")
)
        console.log(Panel(warn_msg, border_style="red", title="🚫 Access Denied"))


console = Console()

def get_user_info():
    try:
        response = requests.get("http://ip-api.com/json/")
        return response.json()
    except Exception as e:
        return {"status": "fail", "message": str(e)}

def create_layout(user_data):
    layout = Layout()

    # Split for banner + body
    layout.split(
        Layout(name="header", size=11),  # Fixed header size
        Layout(name="body", ratio=1)  # Body takes up the rest of the space
    )

    # Create a landscape layout by splitting the body into two equal parts
    layout["body"].split_row(
        Layout(name="left", ratio=1),  # Left side
        Layout(name="right", ratio=1)  # Right side
    )

    # Banner with Dark Violet color
    banner_text = f"""[bold dark_violet]
████████╗██╗    ██╗███████╗ █████╗ ██╗  ██╗
╚══██╔══╝██║    ██║██╔════╝██╔══██╗██║ ██╔╝
   ██║   ██║ █╗ ██║█████╗  ███████║█████╔╝ 
   ██║   ██║███╗██║██╔══╝  ██╔══██║██╔═██╗ 
   ██║   ╚███╔███╔╝███████╗██║  ██║██║  ██╗
   ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

          [red]SESSION KEY [white]: [green]{code}

[/bold dark_violet]"""

    layout["header"].update(
        Panel(
            Align.center(banner_text),

            border_style="dark_violet",
            padding=(0, 2)
        )
    )

    # LEFT PANEL - User Info (with reduced box height)
    if user_data.get("status") == "success":
        user_info = f"""
[bold cyan] IP:[/] {user_data.get("query", "N/A")}  
[bold cyan] Country:[/] {user_data.get("country", "N/A")}  
[bold cyan] Region:[/] {user_data.get("regionName", "N/A")}  
[bold cyan] City:[/] {user_data.get("city", "N/A")}  
[bold cyan] ZIP:[/] {user_data.get("zip", "N/A")}  
[bold cyan] Timezone:[/] {user_data.get("timezone", "N/A")}
"""
    else:
        user_info = "[red]Failed to fetch IP info.[/]"

    # Set padding to 0 and make the box smaller in height
    layout["body"]["left"].update(
        Panel(user_info, title="🌐 User Info", border_style="bold cyan", padding=(0, 0), height=10)  # Limit the height to 6 lines
    )

    # RIGHT PANEL - Tool Info (with reduced box height)
    tool_info = f"""
[bold cyan] Owner:[/] JOVAN C. REGUYA  
[bold cyan] Tool:[/] BOOSTING SOCIAL MEDIA SERVICES  
[bold cyan] Version:[/] 5.0  
[bold cyan] Type:[/] PAID  
[bold cyant] Facebook:[/] (not set)  
[bold cyan] Page:[/] (not set)
"""
    # Set padding to 0 and limit the box height
    layout["body"]["right"].update(
        Panel(tool_info, title="🌊 Tool Credentials", border_style="bold cyan", padding=(0, 0), height=10)  # Limit the height to 6 lines
    )

    return layout

def banner():
    user_data = get_user_info()
    layout = create_layout(user_data)

    console.clear()
    console.print(layout)
generate_and_check_code()



