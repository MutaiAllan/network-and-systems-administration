## Allan Kiprop Mutai
## sct212-0170/2022

# Difference between the 7-layer OSI reference model and the TCP/IP model.

The OSI (Open Systems Interconnection) model and the TCP/IP model are basic frameworks describing how information is transmitted between two devices across a network. Both models define a set of layers, each of which performs a specific set of functions to enable the transmission of data. They guide the design and operation of computer networks. The following are the differences and similarities between them:

1.  Focus and Design: The OSI Model was designed as a general-purpose model, which led to its more detailed and granular seven-layered structure. Each layer has a clearly defined function.  TCP/IP Model was designed specifically around the TCP and IP protocols. As such, its layers reflect the practical needs of those protocols, making it less granular but more aligned with real-world implementation.

2. Layer Structure: OSI comprises seven layers, each with specific tasks. These levels are, from top to bottom: Application, Presentation, Session, Transport, Network, Data Link, and Physical. TCP/IP features a more simple four-layer model: Application, Transport, Internet, and Link.

3. Specific Protocols: OSI is primarily theoretical and doesn't set specific protocols. Instead, it outlines duties and responsibilities for each layer. TCP/IP is highly practical and provides specific protocols, such as HTTP, FTP, SMTP at the Application layer, and TCP and UDP at the Transport layer.

4. Modularity: OSI emphasizes modularity and layer independence, aiming to provide more flexibility in adapting to different network environments. TCP/IP favors a more integrated approach, where functionalities may overlap across layers, simplifying implementation but possibly limiting flexibility.

5. End-to-End Communication: Both models support end-to-end communication. Data travels through multiple layers from the source to the destination, with each layer adding its header or encapsulation, and then the process is reversed at the receiving end. This ensures that the data reaches its intended recipient intact.

6. Standardization: OSI was originally meant as a comprehensive and universally applicable reference model, but it saw limited practical adoption. TCP/IP evolved as a de facto standard for the development and operation of the Internet, having widespread real-world implementation.