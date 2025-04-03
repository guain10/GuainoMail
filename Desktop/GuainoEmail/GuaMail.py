import smtplib
from tkinter import *
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Función para enviar el correo
def enviar_correo():
    # Obtención de los datos del formulario
    remitente = entry_remitente.get()  # Obtiene el correo del remitente
    destinatario = entry_destinatario.get()  # Obtiene el correo del destinatario
    asunto = entry_asunto.get()  # Obtiene el asunto
    mensaje = entry_mensaje.get("1.0", "end-1c")  # Obtiene el mensaje del cuerpo del correo
    
    # Verificar que todos los campos estén completos
    if not remitente or not destinatario or not asunto or not mensaje:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    # Crear el mensaje MIME
    mensaje_mime = MIMEMultipart()
    mensaje_mime['From'] = remitente  # Remitente del correo
    mensaje_mime['To'] = destinatario  # Destinatario del correo
    mensaje_mime['Subject'] = asunto  # Asunto del correo
    mensaje_mime.attach(MIMEText(mensaje, 'plain'))  # Cuerpo del correo como texto plano
    
    try:
        # Configuración del servidor SMTP de Gmail
        servidor_smtp = 'smtp.gmail.com'  # Servidor SMTP de Gmail
        puerto = 587  # Puerto utilizado para la conexión TLS
        usuario = 'tucorreo@gmail.com'  # Cambia esto por tu correo de Gmail
        contrasena = 'tucontraseña'  # Cambia esto por tu contraseña o contraseña de aplicación
        
        # Conectar al servidor SMTP
        server = smtplib.SMTP(servidor_smtp, puerto)  # Conexión al servidor SMTP
        server.starttls()  # Inicia la seguridad TLS
        server.login(usuario, contrasena)  # Realiza el login en el servidor SMTP
        
        # Enviar el correo
        server.sendmail(remitente, destinatario, mensaje_mime.as_string())
        server.quit()  # Cerrar la conexión con el servidor

        # Notificación de éxito
        messagebox.showinfo("Éxito", "Correo enviado correctamente.")
    except Exception as e:
        # Notificación de error
        messagebox.showerror("Error", f"Hubo un error al enviar el correo: {e}")

# Crear la ventana principal de la interfaz gráfica
ventana = Tk()
ventana.title("GuainoraMail - Envío de Correo Electrónico")  # Título de la ventana
ventana.geometry("400x400")  # Tamaño de la ventana

# Etiquetas y campos de texto para ingresar los datos
Label(ventana, text="Remitente:").pack()
entry_remitente = Entry(ventana, width=40)
entry_remitente.pack()

Label(ventana, text="Destinatario:").pack()
entry_destinatario = Entry(ventana, width=40)
entry_destinatario.pack()

Label(ventana, text="Asunto:").pack()
entry_asunto = Entry(ventana, width=40)
entry_asunto.pack()

Label(ventana, text="Mensaje:").pack()
entry_mensaje = Text(ventana, height=8, width=40)
entry_mensaje.pack()

# Botón para enviar el correo
Button(ventana, text="Enviar Correo", command=enviar_correo).pack()

# Iniciar la aplicación
ventana.mainloop()