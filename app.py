from django.http import HttpResponse
import os
import subprocess
import datetime

def htop(request):
    name = "Pragati  Yadav"
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    top_output = subprocess.getoutput("top -b -n 1")
    
    response = f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time} IST</h2>
    <pre>{top_output}</pre>
    """
    
    return HttpResponse(response)
