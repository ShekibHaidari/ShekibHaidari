import datetime
import re

# Fetch current time
current_time = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S UTC")

# Terminal UI format
terminal_ui = f"""<!-- TIME_START -->
<pre><code>[root@shekib-core-server ~]# systemctl status ai-brain
● Active: online & computing
[root@shekib-core-server ~]# date
{current_time}
</code></pre>
<!-- TIME_END -->"""

with open('README.md', 'r', encoding='utf-8') as file:
    readme = file.read()

# Replace old time with the new terminal UI
readme = re.sub(r'<!-- TIME_START -->.*<!-- TIME_END -->', terminal_ui, readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(readme)
