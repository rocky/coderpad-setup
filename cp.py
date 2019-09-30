import os; import sys; import requests
# import requests; exec(requests.get("https://raw.githubusercontent.com/rocky/coderpad-setup/master/cp.py").content)
sh=os.system
lp=lambda program="solution.py": exec(open(program).read())
sh("pip3 install trepan3k")
sys.path.append(".local/lib/python3.6/site-packages")
exec(requests.get("https://raw.github.com/rocky/ipython-trepan/master/trepanmagic.py").content)
print("Rocky's coderpad setup added.")
