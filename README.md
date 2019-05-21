# Data Monitoring Program for CPU/GPU Water Cooling Unit

_<h4>A Python program implemented to monitor a CPU/GPU Water Cooling Unit with sensors connected with a Raspberry Pi Model 3 B+.</h4>_

### <u>Goal</u>
To develop a program that collects live data from temperature and water flow rate sensors installed in a central processing unit (CPU) / graphics processing unit (GPU) water cooling system. The program will output the collected data in a comma-separated values text file and in graph format that is live updated as long as the program is running.

### <u>Implementation</u>
The data monitoring program for the CPU/GPU Water Cooling Unit is implemented with a Python program, a Raspberry Pi Model 3 B+, DS18B20 digital temperature sensors, and Seeed G1/2" water flow sensors. The diagram for the prototype environment is shown in _Figure 1_.

<center><img src="https://github.com/amar-sinha/cpu-gpu-python-monitoring/blob/master/images/prototype_diagram.jpg?raw=true" alt="prototype_drawing" width="500"/>
</br><em>Figure 1: The prototype environment used to test the CPU/GPU Water Cooling Unit.</em>
</center>

The python program, which is run from the command line, is broken into two parts. The initial program connects to the Raspberry Pi and sensors to collect data and store the data in a comma-separated values text file. The second program reads the text file and separates the comma-separated rows of data and graphs each set of statistics against the timestamp.

The programs implement the following important Python packages: matplotlib and RPi.GPIO. The matplotlib library allows the final graph output to be generated, and the RPi.GPIO package allows for the ability to control the general purpose input output (GPIO) pins on the Raspberry Pi.

### <u>Package Installation</u>
Install matplotlib

    $ pip install matplotlib

Install RPi.GPIO

    $ pip install RPi.GPIO

