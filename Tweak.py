
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
import platform 
import os
import time
from datetime import datetime
from rich.panel import Panel
from rich.text import Text
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

try:
    with open("/sdcard/boostphere/generated_code.txt", "r") as file:
        code = file.read().strip()
except FileNotFoundError:
    code = "[red]File not found[/red]"
except Exception as e:
    code = f"[red]Error: {e}[/red]"
CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

# Define colors
lightblue = "[bold cyan]"
lavender = "[magenta]"
yellow = "[yellow]"
green = "[green]"
red = "[red]"
violet_chu = "[blue]"
purple = "[purple]"
white = "[white]"
hotpink = "[bold magenta]"

console = Console()

def count_tokens(accounts_file, pages_file):
    """Count the number of accounts and pages stored in the respective files."""
    total_accounts = 0
    total_pages = 0

    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())
    except FileNotFoundError:
        console.print(f"[red]Account file not found: {accounts_file}[/]")

    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())
    except FileNotFoundError:
        console.print(f"[red]Page file not found: {pages_file}[/]")

    return total_accounts, total_pages



# You can call main() to see the box:
# main()

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
        main()
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
def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

def create_layout(user_data):
    # Ensure files exist and are cleared if necessary
    files_to_clear = [
        '/sdcard/boostphere/FRAACCOUNT.txt',
        '/sdcard/boostphere/FRAPAGES.txt',
        '/sdcard/boostphere/RPWACCOUNT.txt',
        '/sdcard/boostphere/RPWACCOUNT.txt',  # Note: same file listed twice
    ]
    
    for file_path in files_to_clear:
        with open(file_path, 'a') as file:
            pass  # This ensures the file exists without overwriting any data
    
    # Assuming count_tokens is defined elsewhere
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'

    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts, rpwpages)

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
    
    # Assign a value to code
    code = "1234-ABC"  # You can assign the actual session key here

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

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if user_data.get("status") == "success":
        user_info = f"""
[bold cyan] IP:[/] {user_data.get("query", "N/A")}  
[bold cyan] Country:[/] {user_data.get("country", "N/A")}  
[bold cyan] Region:[/] {user_data.get("regionName", "N/A")}  
[bold cyan] City:[/] {user_data.get("city", "N/A")}  
[bold cyan] ZIP:[/] {user_data.get("zip", "N/A")}  
[bold cyan] Timezone:[/] {user_data.get("timezone", "N/A")} 
[bold cyan] Current Time:[/] {current_time}

"""
    else:
        user_info = "[red]Failed to fetch IP info.[/]"

    layout["body"]["left"].update(
        Panel(user_info, title="🌐 User Info", border_style="bold cyan", padding=(0, 0), height=10)
    )

    # Now, let's add the Toolbox below the "User Info" panel in the left column
    toolbox_content = f"""
{lightblue}OVERVIEW OF STORED ACCOUNT & PAGES💫

    {lavender}FRA ACCOUNT{yellow} : {green}{total_accounts}
    {lavender}FRA PAGES  {yellow} : {green}{total_pages}
    {lavender}RPW ACCOUNT{yellow} : {green}{total_account_rpw}
    {lavender}RPW PAGES  {yellow} : {green}{total_pages_rpw}

                   {green} Services We Offer✨

  {green}[01]  {red}START
  {violet_chu}[02]  {purple}REACT TO POST             {white}- {green}[PAGE & ACCOUNT]
  {violet_chu}[03]  {purple}REACT TO REELS            {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[04]  {purple}REACT TO GROUP POST       {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[05]  {purple}REACT TO POST[VID & PHOTO]{yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[06]  {purple}AUTO FOLLOW               {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[07]  {purple}AUTO REACT TO DP & POST   {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[08]  {purple}AUTO COMMENT              {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[09]  {purple}AUTO LIKE & FOLLOW PAGE   {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[10]  {purple}AUTO SHARE [VIA COOKIE]   {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[11]  {purple}AUTO REACT COMMENT        {yellow}- {green}[PAGE & ACCOUNT]
  {violet_chu}[12]  {purple}AUTO REPLY COMMENT       {yellow} - {green}[PAGE & ACCOUNT]
  {violet_chu}[13]  {purple}REACT TO POST (W CARE)   {yellow} - {green}[PAGE & ACCOUNT]
  {violet_chu}[14]  {purple}AUTO GROUP JOIN           {yellow}- {green}[PAGE & ACCOUNT]
  {green}[15]  {red}RESET

                     {green} ADDITIONALS 👒

  {violet_chu}[16] {purple}AUTO CREATE PAGE          {yellow}- {green}[PHB NAMES]
  {violet_chu}[17] {purple}AUTO SET PFP              {yellow}- {green}[RANDOM]
  {violet_chu}[18] {purple}CREATE FILE               {yellow}- {green}[RANDOM]
  {violet_chu}[19] {purple}REMOVE DUPLICATES         {yellow}- {green}[ACCURATE]

                    {green} ACCOUNT CHECKER ✅

  {violet_chu}[20] {purple}ACCOUNT CHECKER           {yellow}- {green}[ACCURATE]
  {violet_chu}[21] {purple}VALIDATE TOKENS           {yellow}- {green}[ACCURATE]
  {violet_chu}[22] {purple}REEDEM ACCOUNTS           {yellow}- {green}[ACCURATE]
  {violet_chu}[25] {purple}AUTO SHARE               {yellow} - {green}[maxspeed]
"""

    # Increase the size of the toolbox panel to ensure content is fully visible
    layout["body"]["left"].split(
        Layout(name="user_info", size=12),  # User Info takes up 12 lines
        Layout(name="toolbox", ratio=2)  # Increase the ratio for the toolbox panel
    )

    layout["body"]["left"]["user_info"].update(
        Panel(user_info, title="🌐 User Info", border_style="bold cyan", padding=(0, 0), height=10)
    )

    layout["body"]["left"]["toolbox"].update(
    Panel(toolbox_content, title="🌐 Toolbox", border_style="bright_magenta")
)
    


    # Tool Info panel (Right panel remains unchanged)
    tool_info = f"""
[bold cyan] Owner:[/] JOVAN C. REGUYA  
[bold cyan] Tool:[/] BOOSTING SOCIAL MEDIA SERVICES  
[bold cyan] Version:[/] 5.0  
[bold cyan] Type:[/] PAID  
[bold cyan] Facebook:[/] (not set)  
[bold cyan] Page:[/] (not set)
"""
    layout["body"]["right"].update(
        Panel(tool_info, title="🌊 Tool Credentials", border_style="bold cyan", padding=(0, 0), height=10 )
    )

    return layout



def banner():
    user_data = get_user_info()
    layout = create_layout(user_data)
    clear_screen()
    console.print(layout)
def standby(): 
    banner()
    generate_and_check_code()
    
def main(): 
    clear_screen()
    banner()
    
    
    

main()


