import radon.metrics
import sys
file_name= sys.argv[0]
download_dir = "C:\\Users\\Sai\\Desktop\\pybugs\\result.html"
num_lines=sum(1 for line in open(file_name))
result= open(download_dir, 'w')
file_iterator=open(file_name,'r')
code=""
for iter in file_iterator.read():
	code=code+iter
cc=radon.metrics.mi_parameters(code)

LLOC=cc[1]
CC=cc[3]
checker=None
if (CC> abs((CC-LLOC)/num_lines)):
	checker=True
else:
	checker=False
if (checker):
	message=""" <html>
<body>
<img src="playground.png" alt="Playground" width="451" height="203" style="margin-left: 50px" >
<div class="row">
  	<div class="column2">
		<a href="javascript:metric(x)">
  		<img src="result.png" width="300" height="300" style="margin-left: 150px; margin-top: 30px"></a>
  		<script type="text/javascript" language="javascript">
  			var x = document.getElementById("myFile");
			
		</script>
		<a href="javascript:metric_display(x)">
		<img src="arrow.png" width="199" height="278" style="margin-left: 150px; margin-top: 20px">
		</a>
  	
  		<img src="bug.png" width="222" height="170" style="margin-left: 100px; margin-bottom: 50px">
		</div>
</div>
</body>
</html>"""
else:
	message=""" <html>
<body>
<img src="playground.png" alt="Playground" width="451" height="203" style="margin-left: 50px" >
<div class="row">
  	<div class="column2">
		<a href="javascript:metric(x)">
  		<img src="result.png" width="300" height="300" style="margin-left: 150px; margin-top: 30px"></a>
  		<script type="text/javascript" language="javascript">
  			var x = document.getElementById("myFile");
			
		</script>
		<a href="javascript:metric_display(x)">
		<img src="arrow.png" width="199" height="278" style="margin-left: 150px; margin-top: 20px">
		</a>
  	
  	
  		<img src="nonbug.png" width="336" height="166" style="margin-left: 100px; margin-bottom: 50px">
  	</div>
</div>
</body>
</html>"""
result.write(message)