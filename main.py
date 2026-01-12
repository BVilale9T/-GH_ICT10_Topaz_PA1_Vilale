from pyscript import document

def convert_to_celcius():
fahrenheit = float(document.getElementById("fahrenheit").value)

celcius = (fahrenheit - 32) * 5 / 9

if celcius >= 37.8:
    status = "You have a fever!"
else:
     status = "You don't have a fever."

document.getElementById("output").innerText
