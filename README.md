# Plotting Email domain data
Simple email domain-name extractor

This simple script extracts email domain extentions (.com,.ip,.gov etc) and plots them on a graph for frequency analysis.
The essential component for extracting email-domain name and the domain-extention is the Regex used.
<ul>
<li>For extracting Email Domain name use: "(?<=@)[\w+.-]+"</li>
<li>For extracting Email-Domain extention use: "[.].*"</li>
</ul>

Graph for the above dataset:

<p align="center">
  <img src="Figure_1.png" width="550">
</p>
