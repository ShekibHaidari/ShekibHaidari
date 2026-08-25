import datetime
import re

current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
time_string = f"<!-- TIME_START -->\n⏳ **آخرین آپدیت:** {current_time}\n<!-- TIME_END -->"

with open('README.md', 'r', encoding='utf-8') as file:
    readme = file.read()

   
readme = re.sub(r'<!-- TIME_START -->.*<!-- TIME_END -->', time_string, readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(readme)
