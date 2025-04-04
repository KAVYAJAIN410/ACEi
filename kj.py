from graphviz import Digraph

# Create a Digraph object
dot = Digraph(comment='Legal Management System Flowchart')

# Set the image size (width and height)
dot.attr(dpi='300', size='12,12', ratio='fill', nodesep='0.5', ranksep='0.5', rankdir='LR')

# Define major groups and tasks
dot.node('A', 'Case Management', shape='box', style='filled', fillcolor='lightblue')
dot.node('B', 'User Interaction & Role-Based Access', shape='box', style='filled', fillcolor='lightgreen')
dot.node('C', 'Judicial Process', shape='box', style='filled', fillcolor='lightyellow')
dot.node('D', 'Support & Communication', shape='box', style='filled', fillcolor='lightpink')
dot.node('E', 'Audit Logs', shape='box', style='filled', fillcolor='lightgray')

# Define subgroups under Case Management
dot.node('A1', 'Case Registration (Input details, Generate Case ID)', shape='ellipse')
dot.node('A2', 'Case Tracking & Status Updates (Monitor Progress)', shape='ellipse')
dot.node('A3', 'Evidence Management (Upload & Store Docs)', shape='ellipse')

# Define subgroups under User Interaction & Role-Based Access
dot.node('B1', 'User Role Management (Define Roles, Permissions)', shape='ellipse')
dot.node('B2', 'Notifications & Alerts (Email, SMS, Push Notifications)', shape='ellipse')
dot.node('B3', 'Account Management (Permissions, Info)', shape='ellipse')

# Define subgroups under Judicial Process
dot.node('C1', 'Hearing Scheduling & Management (Schedule, Notify)', shape='ellipse')
dot.node('C2', 'Legal Reference Integration (IPC, Precedents)', shape='ellipse')
dot.node('C3', 'Analytics & Reporting (Reports, Insights)', shape='ellipse')

# Define subgroups under Support & Communication
dot.node('D1', 'Help & Documentation (Guides, FAQs)', shape='ellipse')
dot.node('D2', 'Contact Us (Contact Info, Maps)', shape='ellipse')

# Define subgroups under Audit Logs
dot.node('E1', 'Audit Logs (System Activity)', shape='ellipse')

# Create edges to represent relationships between nodes
# Case Management
dot.edge('A', 'A1')
dot.edge('A', 'A2')
dot.edge('A', 'A3')

# User Interaction & Role-Based Access
dot.edge('B', 'B1')
dot.edge('B', 'B2')
dot.edge('B', 'B3')

# Judicial Process
dot.edge('C', 'C1')
dot.edge('C', 'C2')
dot.edge('C', 'C3')

# Support & Communication
dot.edge('D', 'D1')
dot.edge('D', 'D2')

# Audit Logs
dot.edge('E', 'E1')

# Define the relationships between major groups
dot.edge('A1', 'B1')  # Case Registration -> User Role Management
dot.edge('A2', 'B2')  # Case Tracking -> Notifications
dot.edge('A3', 'B3')  # Evidence Management -> Account Management
dot.edge('C1', 'B2')  # Hearing Scheduling -> Notifications
dot.edge('C2', 'C3')  # Legal Reference -> Analytics
dot.edge('D1', 'B3')  # Help & Documentation -> Account Management

# Save the flowchart to a file with more compact layout
dot.render('legal_management_flowchart_compact', format='png', cleanup=True)

print("Flowchart generated and saved as 'legal_management_flowchart_compact.png'")
