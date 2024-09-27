# **WannaCry-Ransomware-Analysis**

**A personal case study analyzing the WannaCry ransomware using static and dynamic malware analysis techniques.**

---

## **Overview**

This project aims to analyze the infamous **WannaCry ransomware attack**, which affected over 200,000 machines globally in 2017. Using both static and dynamic analysis, I investigated the malware's behavior, identified the tools used to carry out the attack, and explored ways to mitigate such threats in the future.

This case study serves as a hands-on exploration of malware analysis techniques, including file examination, hashing, and sandboxing, to better understand the lifecycle of ransomware attacks and how to protect against them.

---

## **Objective**

The primary objective of this project was to:
1. **Identify the key behaviors and characteristics** of WannaCry ransomware through forensic tools.
2. **Analyze the static properties** of the malware.
3. **Execute a dynamic analysis** to observe how the ransomware behaves in real-time within a controlled environment.
4. **Provide recommendations** on preventing and mitigating similar attacks.

---

## **Tools Used**
- **HxD (Hex Editor)**: For binary analysis of the ransomware file.
- **pestudio**: For further confirmation of the file type.
- **HashCalc**: For creating a hash of the ransomware file to verify its integrity.
- **VirusTotal**: For uploading and analyzing the file’s hash to identify its malware signature.
- **Process Hacker**: For monitoring the ransomware’s processes during execution.
- **Virtual Machine (VM)**: A controlled environment for dynamic analysis.

---

## **1. Static Analysis**

In the static analysis, I investigated the file structure of the ransomware without executing it to understand its properties.

### **Step 1: Identifying File Type**
Using **HxD**, I identified the file's header as `MZ`, confirming that it was an executable (EXE) file.

![HxD Screenshot](screenshots/HxD%20Editor%20Screenshot.PNG)

### **Step 2: Confirming File Type with pestudio**
I used **pestudio** to cross-check the file type. The tool confirmed the presence of the `MZ` header, indicating an executable file.

![pestudio Screenshot](screenshots/pestudio%20Screenshot.PNG)

### **Step 3: Generating Hash Value**
To automate part of the static analysis process, I created a Python script to generate the SHA256 hash of the file. This eliminates the need to manually generate the hash.

![Hash Script Screenshot](screenshots/Hash%20Script%20Screenshot.PNG)

![Hash Output Screenshot](screenshots/Hash%20Output%20Screenshot.PNG)

### **Step 4: Verifying with VirusTotal**
I uploaded the hash to **VirusTotal**, where it was flagged as malicious by 67 out of 71 antivirus engines. VirusTotal classified it under the **"ransomware.wannacryptor"** tag.

![VirusTotal Screenshot](screenshots/VirusTotal%20Screenshot.PNG)

---

## **2. Dynamic Analysis**

Dynamic analysis was conducted by running the malware in a controlled environment (VM) to observe its runtime behavior.

### **Step 1: Executing the Ransomware in a VM**
Upon execution, the ransomware displayed a pop-up window, demanding a ransom to decrypt the affected files. The message identified itself as **"Wanna Decrypt0r 2.0"**.

![WannaCry.exe Screenshot](screenshots/WannaCry.exe%20Screenshot.PNG)

### **Step 2: Monitoring Processes**
Using **Process Hacker**, I monitored the malware’s behavior. It spawned several processes, including `wanadecryptor` and `DiskPart`, which were consistent with the malware signatures detected earlier.

![ProcessHacker Screenshot](screenshots/ProcessHacker%20Screenshot.PNG)

### **Step 3: Analysing Strings**
Process Hacker revealed the ransom demand, which instructed victims to send **£300 worth of Bitcoin** to a specific address.

![ProcessHacker Strings Screenshot](screenshots/Strings%20Analysis%20Screenshot.PNG)

---

## **Findings and Insights**

The WannaCry ransomware is a highly destructive piece of malware, utilizing a Windows vulnerability (EternalBlue) to spread rapidly across networks. The static and dynamic analyses revealed the following key behaviors:

- The executable file spreads by exploiting vulnerabilities in unpatched systems.
- It encrypts user files, demanding ransom in Bitcoin for their recovery.
- It operates under multiple aliases, such as `diskpart.exe`, to disguise its malicious nature.

---

## **Recommendations**

To mitigate similar ransomware threats, I recommend the following strategies:

1. **Regularly Apply Security Patches**: The vulnerability exploited by WannaCry (EternalBlue) had already been patched by Microsoft. Ensuring systems are up to date is critical in preventing such exploits.
2. **Implement Backup Solutions**: Regular backups can help organizations recover quickly in case of an attack without needing to pay a ransom.
3. **Employee Training**: Educating staff about phishing emails and safe computing practices can reduce the likelihood of ransomware infection.
4. **Use Robust Antivirus and Firewalls**: Comprehensive protection with antivirus and firewalls can detect and block ransomware before it executes.

---

## **Conclusion**

The WannaCry ransomware attack demonstrates the devastating impact that unpatched vulnerabilities can have on organizations. Through static and dynamic analysis, I gained insights into how the malware operates and how it can be mitigated. This case study serves as a foundational exploration of malware analysis, providing valuable lessons for protecting against future ransomware attacks.
