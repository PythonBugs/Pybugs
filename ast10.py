import radon
import ast
import os
from radon.raw import analyze
import radon.metrics
import sys
file_name = sys.argv[1]

download_dir = "C:\\Users\\Sai\\Desktop\\pybugs\\metrics.html"
columnTitleRow = "LOC,LLOC,SLOC,comments,multi,blank,single_comments,Halstead Volume,CC,comment %,h1,h2,N1,N2,h,N,calculated_length,difficulty,effort,time,bugs\n"
csv = open(download_dir, 'w')

file_iterator = open(file_name, 'r')
code=""
for iter in file_iterator.read():
	code = code+iter
number_of_lines = radon.raw.analyze(code)
cc = radon.metrics.mi_parameters(code, count_multi=True)
source = ast.parse(code)
halstead = radon.metrics.h_visit_ast(source)
row= str(number_of_lines[0])+","+ str(number_of_lines[1]) +","+ str(number_of_lines[2])+","+str(number_of_lines[3])+","+ str(number_of_lines[4]) +","+ str(number_of_lines[5])+","+str(number_of_lines[6])+","+str(cc[0])+","+str(cc[1])+","+str(cc[3])+","+str(halstead[0])+","+str(halstead[1])+","+str(halstead[2])+","+str(halstead[3])+","+str(halstead[4])+","+str(halstead[5])+","+str(halstead[6])+","+str(halstead[8])+","+str(halstead[9])+","+str(halstead[10])+","+str(halstead[11])+"\n"

message = """
<html>
<head>
	<title>PyBugs PlayGround</title>
	<script type="text/javascript">
		function train(){
			window.open("train.html")
		}
		function test(){
			window.open("test.html")
		}

		}
	</script>

	<style type="text/css">
		
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
	margin-left:100px;
	margin-top:50px;
}

td, th {
    border: 1px solid #dddddd;
    background-color: #F5F5F5;
    text-align: left;
    padding: 8px;
}

td:nth-child(even) {
    background-color: #A8A8A8;
}
td:nth-child(odd) {
    background-color: #D3D3D3;
}
	</style>
</head>
<body>
	<div>
		<img src="playground.png" alt="Playground" width="451" height="203" style="margin-left: 80px" >
		<img src="train.png" alt="train" width="300" height="175" onclick="train()" style="cursor: pointer; margin-left: 100px"  >
		<img src="test.png" alt="test" width="300" height="175" onclick="test()" style="cursor: pointer">
	</div>
	<div>
		<img src="tr.png" alt="tr" width="500" height="500" style="margin-left: 100px">
		<img src="te.png" alt="te" width="500" height="500" style="margin-left: 100px" >
	</div>
	<div>
		<img src="code metrics.png" alt="tr" width="378" height="67" style="margin-left: 100px; margin-top: 50px">
	</div>
	
  	<div>
  	
  		<script type="text/javascript" language="javascript">
  			var x = document.getElementById("myFile");
			
  }
  
</script>
  	

  	</div>
    <div>
	<table>
	<tr>
	<th>LOC</th><th>LLOC</th><th>SLOC</th><th>Comments</th><th>Multi</th><th>Blank</th><th>Single_comments</th><th>Halstead Volume</th><th>CC</th><th>Comment %</th><th>h1</th><th>h2</th><th>N1</th><th>N2</th><th>h</th><th>N</th><th>Calculated_length</th><th>Difficulty</th><th>Effort</th><th>Time</th><th>Bugs</tr>
	</tr>
	<tr><td>
	"""+ str(number_of_lines[0])+"</td><td>"+ str(number_of_lines[1]) +"</td><td>"+ str(number_of_lines[2])+"</td><td>"+str(number_of_lines[3])+"</td><td>"+ str(number_of_lines[4]) +"</td><td>"+ str(number_of_lines[5])+"</td><td>"+str(number_of_lines[6])+"</td><td>"+str(cc[0])+"</td><td>"+str(cc[1])+"</td><td>"+str(cc[3])+"</td><td>"+str(halstead[0])+"</td><td>"+str(halstead[1])+"</td><td>"+str(halstead[2])+"</td><td>"+str(halstead[3])+"</td><td>"+str(halstead[4])+"</td><td>"+str(halstead[5])+"</td><td>"+str(halstead[6])+"</td><td>"+str(halstead[8])+"</td><td>"+str(halstead[9])+"</td><td>"+str(halstead[10])+"</td><td>"+str(halstead[11])+"""</td></tr></table></div>
</div>
<div>
<a href="https://vpyast.appspot.com/"><h3 style="text-align:center;">Click here to check out the Python AST</h3></a>
</div>
</body>
</html>"""

csv.write(message)
