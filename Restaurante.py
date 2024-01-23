#Sistema de restaurante en python
from tkinter import*
from tkinter import filedialog,messagebox
import random
import time

def guardar():
    url=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    datos_recibo=textoRecibo.get(1.0,END)
    url.write(datos_recibo)
    url.close()
    messagebox.showinfo("Informacion",message="Recibo almacenado con exito")

def enviar():
    pass
def borrar():
    textoRecibo.delete(1.0,END)
    txtPollo.set('0')
    txtCarne.set('0')
    txtArroz.set('0')
    txtEnsalada.set('0')
    txtPasta.set('0')
    txtPizza.set('0')
    txtSushi.set('0')
    txtTacos.set('0')
    txtPaella.set('0')
    txtLasagna.set('0')

    txtPepsi.set('0')
    txtCoca.set('0')
    txtMirinda.set('0')
    txtGrapete.set('0')
    txtSeven.set('0')
    txtOrange.set('0')
    txtHorchata.set('0')
    txtLimonada.set('0')
    txtNaranjada.set('0')
    txtJamaica.set('0')

    txtchoco.set('0')
    txtbrownie.set('0')
    txtleches.set('0')
    txtzanahoria.set('0')
    txtmanie.set('0')
    txtalmendra.set('0')
    txtmanzana.set('0')
    txtchurro.set('0')
    txtrelleno.set('0')
    txtflan.set('0')

    textpollo.config(state=DISABLED)
    textCarne.config(state=DISABLED)
    textArroz.config(state=DISABLED)
    textCarneEnsalada.config(state=DISABLED)
    textPasta.config(state=DISABLED)
    textPizza.config(state=DISABLED)
    textSushi.config(state=DISABLED)
    textTacos.config(state=DISABLED)
    textPaella.config(state=DISABLED)
    textLasagna.config(state=DISABLED)

    textPepsi.config(state=DISABLED)
    textCocaCola.config(state=DISABLED)
    textSevenUp.config(state=DISABLED)
    textMirinda.config(state=DISABLED)
    textGrapete.config(state=DISABLED)
    textOrange.config(state=DISABLED)
    textLimonada.config(state=DISABLED)
    textNaranjada.config(state=DISABLED)
    textJamaica.config(state=DISABLED)
    textHorchata.config(state=DISABLED)

    textPastelChocolate.config(state=DISABLED)
    textBrownie.config(state=DISABLED)
    textPastelTresLeches.config(state=DISABLED)
    textPastelDeZanahoria.config(state=DISABLED)
    textPastelDeManie.config(state=DISABLED)
    textPastelDeAlmendra.config(state=DISABLED)
    textPastelDeManzana.config(state=DISABLED)
    textChurros.config(state=DISABLED)
    textRellenitos.config(state=DISABLED)
    textFlan.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)


    global varcostocomida, varcostobebida,varcostopostre, varsubtotal, variva, vartotal
    varcostocomida=0
    varcostobebida=0
    varcostopostre=0
    varsubtotal=0
    variva=0
    vartotal=0

    casillaCostoComida.config(state=NORMAL)
    casillaCostoComida.delete(0,END)
    casillaCostoComida.insert(0,varcostocomida)
    casillaCostoComida.config(state=DISABLED)

    casillaCostoPostres.config(state=NORMAL)
    casillaCostoPostres.delete(0,END)
    casillaCostoPostres.insert(0,varcostopostre)
    casillaCostoPostres.config(state=DISABLED)

    casillasCostoBebidas.config(state=NORMAL)
    casillasCostoBebidas.delete(0,END)
    casillasCostoBebidas.insert(0,varcostopostre)
    casillasCostoBebidas.config(state=DISABLED)

    casillasubtotal.config(state=NORMAL)
    casillasubtotal.delete(0,END)
    casillasubtotal.insert(0,varsubtotal)
    casillasubtotal.config(state=DISABLED)

    casillaiva.config(state=NORMAL)
    casillaiva.delete(0,END)
    casillaiva.insert(0,variva)
    casillaiva.config(state=DISABLED)

    casillapagoTotal.config(state=NORMAL)
    casillapagoTotal.delete(0,END)
    casillapagoTotal.insert(0,vartotal)
    casillapagoTotal.config(state=DISABLED)

def recibo():
    textoRecibo.delete(1.0,END)
    x=random.randint(1,10000)
    noRecibo = 'No'+str(x)
    fecha=time.strftime('%d/%m/%y')
    textoRecibo.insert(END, 'Factura->'+ noRecibo+'\t\t\t\ Fecha:'+fecha+'\n')
    textoRecibo.insert(END,'*************************************************************************\n')
    textoRecibo.insert(END, 'Totales \t\t\t Cantidades:\n')
    textoRecibo.insert(END, '************************************************************************\n')
    textoRecibo.insert(END, 'Total de comida  ------------------->Q'+str(varcostocomida)+'.00\n')
    textoRecibo.insert(END, 'Total de bebidas ------------------->Q'+str(varcostobebida)+'.00\n')
    textoRecibo.insert(END, 'Total de postres ------------------->Q'+str(varcostopostre)+'.00\n')
    textoRecibo.insert(END, 'Subtotal ------------------------------->Q'+str(subtotal)+'.00\n')
    textoRecibo.insert(END, 'Impuesto IVA ---------------------->Q'+str(iva)+'.00\n')
    textoRecibo.insert(END, '************************************************************************\n\n')
    textoRecibo.insert(END, 'GRAN TOTAL A PAGAR ---------------> \t\t\t Q'+str(total)+'.00\n')


#funciones para los totales
def grantotal():
    global varcostocomida, varcostobebida,varcostopostre, subtotal, iva, total
    #valores de comida
    t_pollo=int(textpollo.get())
    t_carne=int(textCarne.get())
    t_arroz=int(textArroz.get())
    t_ensalada=int(textCarneEnsalada.get())
    t_pasta=int(textPasta.get())
    t_pizza=int(textPizza.get())
    t_sushi=int(textSushi.get())
    t_tacos=int(textTacos.get())
    t_paella=int(textPaella.get())
    t_lasagna=int(textLasagna.get())
    varcostocomida=(t_pollo*15)+(t_carne*35)+(t_arroz*10)+(t_ensalada*10)+(t_pasta*20)+(t_pizza*25)+(t_sushi*38)+(t_tacos*18)+(t_paella*45)+(t_lasagna*68)
    casillaCostoComida.config(state=NORMAL)
    casillaCostoComida.delete(0,END)
    casillaCostoComida.insert(0,varcostocomida)
    casillaCostoComida.config(state=DISABLED)

#Valores de bebidas
    t_pepsi=int(textPepsi.get())
    t_coca=int(textCocaCola.get())
    t_seven=int(textSevenUp.get())
    t_mirinda=int(textMirinda.get())
    t_grapete=int(textGrapete.get())
    t_orange=int(textOrange.get())
    t_limonada=int(textLimonada.get())
    t_naranjada=int(textNaranjada.get())
    t_jamaica=int(textJamaica.get())
    t_horchata=int(textHorchata.get())
    varcostobebida=(t_pepsi*5)+(t_coca*7)+(t_seven*5)+(t_mirinda*6)+(t_grapete*6)+(t_orange*6)+(t_limonada*5)+(t_naranjada*5)+(t_jamaica*5)+(t_horchata*5)
    casillasCostoBebidas.config(state=NORMAL)
    casillasCostoBebidas.delete(0,END)
    casillasCostoBebidas.insert(0,varcostobebida)
    casillasCostoBebidas.config(state=DISABLED)

#Valores postres
    t_pchoco=int(textPastelChocolate.get())
    t_brownie=int(textBrownie.get())
    t_pleches=int(textPastelTresLeches.get())
    t_pzanahoria=int(textPastelDeZanahoria.get())
    t_manie=int(textPastelDeManie.get())
    t_palmendra=int(textPastelDeAlmendra.get())
    t_pmanzana=int(textPastelDeManzana.get())
    t_churro=int(textChurros.get())
    t_rellenito=int(textRellenitos.get())
    t_flan=int(textFlan.get())
    varcostopostre=(t_pchoco*20)+(t_brownie*12)+(t_pleches*21)+(t_pzanahoria*16)+(t_manie*18)+(t_palmendra*15)+(t_pmanzana*10)+(t_churro*10)+(t_rellenito*18)+(t_flan*20)
    casillaCostoPostres.config(state=NORMAL)
    casillaCostoPostres.delete(0,END)
    casillaCostoPostres.insert(0,varcostopostre)
    casillaCostoPostres.config(state=DISABLED)

    subtotal=varcostocomida+ varcostobebida+varcostopostre
    casillasubtotal.config(state=NORMAL)
    casillasubtotal.delete(0,END)
    casillasubtotal.insert(0,subtotal)
    casillasubtotal.config(state=DISABLED)

    iva=int(casillasubtotal.get()) *0.12
    casillaiva.config(state=NORMAL)
    casillaiva.delete(0,END)
    casillaiva.insert(0,iva)
    casillaiva.config(state=DISABLED)

    total= iva + subtotal
    casillapagoTotal.config(state=NORMAL)
    casillapagoTotal.delete(0,END)
    casillapagoTotal.insert(0,total)
    casillapagoTotal.config(state=DISABLED)

#Funciones para activar y desactivar casillas
def pollo():
    if var1.get()==1:
        textpollo.config(state=NORMAL)
        textpollo.delete(0,END)
        textpollo.focus()
    else:
        textpollo.config(state=DISABLED)
        txtPollo.set('0')

def carne():
    if var2.get()==1:
        textCarne.config(state=NORMAL)
        textCarne.delete(0,END)
        textCarne.focus()
    else:
        textCarne.config(state=DISABLED)
        txtCarne.set('0')

def arroz():
    if var3.get()==1:
        textArroz.config(state=NORMAL)
        textArroz.delete(0,END)
        textArroz.focus()
    else:
        textArroz.config(state=DISABLED)
        txtArroz.set('0')
def ensalada():
    if var4.get()==1:
        textCarneEnsalada.config(state=NORMAL)
        textCarneEnsalada.delete(0,END)
        textCarneEnsalada.focus()
    else:
        textCarneEnsalada.config(state=DISABLED)
        txtEnsalada.set('0')
def pasta():
    if var5.get()==1:
        textPasta.config(state=NORMAL)
        textPasta.delete(0,END)
        textPasta.focus()
    else:
        textPasta.config(state=DISABLED)
        txtPasta.set('0')
def pizza():
    if var6.get()==1:
        textPizza.config(state=NORMAL)
        textPizza.delete(0,END)
        textPizza.focus()
    else:
        textPizza.config(state=DISABLED)
        txtPizza.set('0')
def sushi():
    if var7.get()==1:
        textSushi.config(state=NORMAL)
        textSushi.delete(0,END)
        textSushi.focus()
    else:
        textSushi.config(state=DISABLED)
        txtSushi.set('0')
def tacos():
    if var8.get()==1:
        textTacos.config(state=NORMAL)
        textTacos.delete(0,END)
        textTacos.focus()
    else:
        textTacos.config(state=DISABLED)
        txtTacos.set('0')
def paella():
    if var9.get()==1:
        textPaella.config(state=NORMAL)
        textPaella.delete(0,END)
        textPaella.focus()
    else:
        textPaella.config(state=DISABLED)
        txtPaella.set('0')
def lasagna():
    if var10.get()==1:
        textLasagna.config(state=DISABLED)
        textLasagna.delete(0,END)
        textLasagna.focus()
    else:
        textLasagna.config(state=DISABLED)
        txtLasagna.set('0')
#Funciones para las bebidas
def pepsi():
    if var11.get()==1:
        textPepsi.config(state=NORMAL)
        textPepsi.delete(0,END)
        textPepsi.focus()
    else:
        textPepsi.config(state=DISABLED)
        txtPepsi.set('0')
def coca():
    if var12.get()==1:
        textCocaCola.config(state=NORMAL)
        textCocaCola.delete(0,END)
        textCocaCola.focus()
    else:
        textCocaCola.config(state=DISABLED)
        txtCoca.set('0')
def seven():
    if var13.get()==1:
        textSevenUp.config(state=NORMAL)
        textSevenUp.delete(0,END)
        textSevenUp.focus()
    else:
        textSevenUp.config(state=DISABLED)
        txtSeven.set('0')
def mirinda():
    if var14.get()==1:
        textMirinda.config(state=NORMAL)
        textMirinda.delete(0,END)
        textMirinda.focus()
    else:
        textMirinda.config(state=DISABLED)
        txtMirinda.set('0')
def grapete():
    if var15.get()==1:
        textGrapete.config(state=NORMAL)
        textGrapete.delete(0,END)
        textGrapete.focus()
    else:
        textGrapete.config(state=DISABLED)
        txtGrapete.set('0')
def orange():
    if var16.get()==1:
        textOrange.config(state=NORMAL)
        textOrange.delete(0,END)
        textOrange.focus()
    else:
        textOrange.config(state=DISABLED)
        txtOrange.set('0')
def limonada():
    if var17.get()==1:
        textLimonada.config(state=NORMAL)
        textLimonada.delete(0,END)
        textLimonada.focus()
    else:
        textLimonada.config(state=DISABLED)
        txtLimonada.set('0')
def naranjada():
    if var18.get()==1:
        textNaranjada.config(state=NORMAL)
        textNaranjada.delete(0,END)
        textNaranjada.focus()
    else:
        textNaranjada.config(state=DISABLED)
        txtNaranjada.set('0')
def jamaica():
    if var19.get()==1:
        textJamaica.config(state=NORMAL)
        textJamaica.delete(0,END)
        textJamaica.focus()
    else:
        textJamaica.config(state=DISABLED)
        txtJamaica.set('0')
def horchata():
    if var20.get()==1:
        textHorchata.config(state=NORMAL)
        textHorchata.delete(0,END)
        textHorchata.focus()
    else:
        textHorchata.config(state=DISABLED)
        txtHorchata.set('0')
def choco():
    if var21.get()==1:
        textPastelChocolate.config(state=NORMAL)
        textPastelChocolate.delete(0,END)
        textPastelChocolate.focus()
    else:
        textPastelChocolate.config(state=DISABLED)
        txtchoco.set('0')
def brownie():
    if var22.get()==1:
        textBrownie.config(state=NORMAL)
        textBrownie.delete(0,END)
        textBrownie.focus()
    else:
        textBrownie.config(state=DISABLED)
        txtbrownie.set('0')
def leche():
    if var23.get()==1:
        textPastelTresLeches.config(state=NORMAL)
        textPastelTresLeches.delete(0,END)
        textPastelTresLeches.focus()
    else:
        textPastelTresLeches.config(state=DISABLED)
        txtleches.set('0')
def zanahoria():
    if var24.get()==1:
        textPastelDeZanahoria.config(state=NORMAL)
        textPastelDeZanahoria.delete(0,END)
        textPastelDeZanahoria.focus()
    else:
        textPastelDeZanahoria.config(state=DISABLED)
        txtzanahoria.set('0')
def manie():
    if var25.get()==1:
        textPastelDeManie.config(state=NORMAL)
        textPastelDeManie.delete(0,END)
        textPastelDeManie.focus()
    else:
        textPastelDeManie.config(state=DISABLED)
        txtmanie.set('0')
def almendra():
    if var26.get()==1:
        textPastelDeAlmendra.config(state=NORMAL)
        textPastelDeAlmendra.delete(0,END)
        textPastelDeAlmendra.focus()
    else:
        textPastelDeAlmendra.config(state=DISABLED)
        txtalmendra.set('0')
def manzana():
    if var27.get()==1:
        textPastelDeManzana.config(state=NORMAL)
        textPastelDeManzana.delete(0,END)
        textPastelDeManzana.focus()
    else:
        textPastelDeManzana.config(state=DISABLED)
        txtmanzana.set('0')
def churros():
    if var28.get()==1:
        textChurros.config(state=NORMAL)
        textChurros.delete(0,END)
        textChurros.focus()
    else:
        textChurros.config(state=DISABLED)
        txtchurro.set('0')
def rellenitos():
    if var29.get()==1:
        textRellenitos.config(state=NORMAL)
        textRellenitos.delete(0,END)
        textRellenitos.focus()
    else:
        textRellenitos.config(state=DISABLED)
        txtrelleno.set('0')
def flan():
    if var30.get()==1:
        textFlan.config(state=NORMAL)
        textFlan.delete(0,END)
        textFlan.focus()
    else:
        textFlan.config(state=DISABLED)
        txtflan.set('0')

#Diseño de la ventana principal
ventana = Tk()
ventana.title("Sistema restaurante | AO")
ventana.geometry("1300x650")
ventana.resizable(0,0)
ventana.config(bg="darkblue")

#Estableciendo las fuentes
Title=("arial black",25)
Subtitle=("consolas", 14)

#Marco de titulo principal
marcoSuperior=Frame(ventana,bd=12, relief=RIDGE,bg="blue")
marcoSuperior.pack(side=TOP)
#Titulo principal
tituloPrincipal=Label(marcoSuperior,text="Sistema de Restaurante AO", font=Title, fg="white",bg="blue",width=53)
tituloPrincipal.grid(row=0,column=0)

#Marcos secundarios
marcoMenu=Frame(ventana, bd=10, relief=RIDGE, bg="blue")
marcoMenu.pack(side=LEFT)
marcoCosto=Frame(marcoMenu, bd=2, relief=RIDGE, bg="blue")
marcoCosto.pack(side=BOTTOM)
marcoComida=LabelFrame(marcoMenu,text='Platillos', bd=5, font=Subtitle, relief=RIDGE, bg="white")
marcoComida.pack(side=LEFT)
marcoBebidas=LabelFrame(marcoMenu,text='Bebidas', bd=5,font=Subtitle, relief=RIDGE, bg="white")
marcoBebidas.pack(side=LEFT)
marcoPostres=LabelFrame(marcoMenu,text='Postres', bd=5,font=Subtitle, relief=RIDGE, bg="white")
marcoPostres.pack(side=LEFT)

#Marcos para el lado derecho
marcoDerecho=Frame(ventana,bd=10, relief=RIDGE, bg="blue")
marcoDerecho.pack(side=RIGHT)
marcoCalculadora=Frame(marcoDerecho,bd=5, relief=RIDGE, bg="blue")
marcoCalculadora.pack()
marcoRecibo=Frame(marcoDerecho,bd=5, relief=RIDGE,bg="blue")
marcoRecibo.pack()
marcoBotones=Frame(marcoDerecho,bd=5, relief=RIDGE, bg="blue")
marcoBotones.pack()

#Variables a usar para comida
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
#Variables para las bebidas
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
#Variables para los postres
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()

#Variables para las cajas de texto de la comida
txtPollo=StringVar()
txtPollo.set('0')
txtCarne=StringVar()
txtCarne.set('0')
txtArroz=StringVar()
txtArroz.set('0')
txtEnsalada=StringVar()
txtEnsalada.set('0')
txtPasta=StringVar()
txtPasta.set('0')
txtPizza=StringVar()
txtPizza.set('0')
txtSushi=StringVar()
txtSushi.set('0')
txtTacos=StringVar()
txtTacos.set('0')
txtPaella=StringVar()
txtPaella.set('0')
txtLasagna=StringVar()
txtLasagna.set('0')

#Variables para las cajas de texto de las bebidas
txtPepsi=StringVar()
txtPepsi.set('0')
txtCoca=StringVar()
txtCoca.set('0')
txtMirinda=StringVar()
txtMirinda.set('0')
txtGrapete=StringVar()
txtGrapete.set('0')
txtSeven=StringVar()
txtSeven.set('0')
txtOrange=StringVar()
txtOrange.set('0')
txtHorchata=StringVar()
txtHorchata.set('0')
txtLimonada=StringVar()
txtLimonada.set('0')
txtNaranjada=StringVar()
txtNaranjada.set('0')
txtJamaica=StringVar()
txtJamaica.set('0')

#Variables para las cajas de los textos de los postres
txtchoco=StringVar()
txtchoco.set('0')
txtbrownie=StringVar()
txtbrownie.set('0')
txtleches=StringVar()
txtleches.set('0')
txtzanahoria=StringVar()
txtzanahoria.set('0')
txtmanie=StringVar()
txtmanie.set('0')
txtalmendra=StringVar()
txtalmendra.set('0')
txtmanzana=StringVar()
txtmanzana.set('0')
txtchurro=StringVar()
txtchurro.set('0')
txtrelleno=StringVar()
txtrelleno.set('0')
txtflan=StringVar()
txtflan.set('0')



#Comida
#Etiqueta y boton para seleccionar
Pollo=Checkbutton(marcoComida,text="Pollo",font=Subtitle,onvalue=1,offvalue=0,variable=var1,command=pollo)
Pollo.grid(row=0, column=0, sticky=W)
Carne=Checkbutton(marcoComida,text="Carne",font=Subtitle,onvalue=1,offvalue=0,variable=var2,command=carne)
Carne.grid(row=1,column=0,sticky=W)
Arroz=Checkbutton(marcoComida,text='Arroz',font=Subtitle,onvalue=1,offvalue=0,variable=var3,command=arroz)
Arroz.grid(row=2,column=0,sticky=W)
Ensalada=Checkbutton(marcoComida,text='Ensalada',font=Subtitle,onvalue=1,offvalue=0,variable=var4,command=ensalada)
Ensalada.grid(row=3,column=0,sticky=W)
Pasta=Checkbutton(marcoComida,text='Pasta',font=Subtitle,onvalue=1,offvalue=0,variable=var5,command=pasta)
Pasta.grid(row=4,column=0,sticky=W)
Pizza=Checkbutton(marcoComida,text='Pizza',font=Subtitle,onvalue=1,offvalue=0,variable=var6,command=pizza)
Pizza.grid(row=5,column=0,sticky=W)
Sushi=Checkbutton(marcoComida,text='Sushi',font=Subtitle,onvalue=1,offvalue=0,variable=var7,command=sushi)
Sushi.grid(row=6,column=0,sticky=W)
Tacos=Checkbutton(marcoComida,text='Tacos',font=Subtitle,onvalue=1,offvalue=0,variable=var8,command=tacos)
Tacos.grid(row=7,column=0,sticky=W)
Paella=Checkbutton(marcoComida,text='paella',font=Subtitle,onvalue=1,offvalue=0,variable=var9,command=paella)
Paella.grid(row=8,column=0,sticky=W)
Lasagna=Checkbutton(marcoComida,text='Lasagna',font=Subtitle,onvalue=1,offvalue=0,variable=var10,command=lasagna)
Lasagna.grid(row=9,column=0,sticky=W)
#Cajas de texto para cada comida
textpollo=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPollo)
textpollo.grid(row=0,column=1)
textCarne=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCarne)
textCarne.grid(row=1,column=1)
textArroz=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtArroz)
textArroz.grid(row=2,column=1)
textCarneEnsalada=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtEnsalada)
textCarneEnsalada.grid(row=3,column=1)
textPasta=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPasta)
textPasta.grid(row=4,column=1)
textPizza=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPizza)
textPizza.grid(row=5,column=1)
textSushi=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtSushi)
textSushi.grid(row=6,column=1)
textTacos=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtTacos)
textTacos.grid(row=7,column=1)
textPaella=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtPaella)
textPaella.grid(row=8,column=1)
textLasagna=Entry(marcoComida,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtLasagna)
textLasagna.grid(row=9,column=1)

#Bebidas
#Etiqueta y boton de check
Pepsi=Checkbutton(marcoBebidas,text='Pepsi',font=Subtitle,onvalue=1,offvalue=0,variable=var11, command=pepsi)
Pepsi.grid(row=0,column=0,sticky=W)
CocaCola=Checkbutton(marcoBebidas,text='Coca Cola',font=Subtitle,onvalue=1,offvalue=0,variable=var12, command=coca)
CocaCola.grid(row=1,column=0,sticky=W)
SevenUp=Checkbutton(marcoBebidas,text='SevenUp',font=Subtitle,onvalue=1,offvalue=0,variable=var13, command=seven)
SevenUp.grid(row=2,column=0,sticky=W)
Mirinda=Checkbutton(marcoBebidas,text='Mirinda',font=Subtitle,onvalue=1,offvalue=0,variable=var14, command=mirinda)
Mirinda.grid(row=3,column=0,sticky=W)
Grapete=Checkbutton(marcoBebidas,text='Grapete',font=Subtitle,onvalue=1,offvalue=0,variable=var15, command=grapete)
Grapete.grid(row=4,column=0,sticky=W)
Orange=Checkbutton(marcoBebidas,text='Orange',font=Subtitle,onvalue=1,offvalue=0, variable=var16, command=orange)
Orange.grid(row=5,column=0,sticky=W)
Limonada=Checkbutton(marcoBebidas,text='Limonada',font=Subtitle,onvalue=1,offvalue=0, variable=var17, command=limonada)
Limonada.grid(row=6,column=0,sticky=W)
Naranjada=Checkbutton(marcoBebidas,text='Naranjada',font=Subtitle,onvalue=1,offvalue=0, variable=var18, command=naranjada)
Naranjada.grid(row=7,column=0,sticky=W)
Jamaica=Checkbutton(marcoBebidas,text='Jamaica',font=Subtitle,onvalue=1,offvalue=0, variable=var19, command=jamaica)
Jamaica.grid(row=8,column=0,sticky=W)
Horchata=Checkbutton(marcoBebidas,text='Horchata',font=Subtitle,onvalue=1,offvalue=0, variable=var20, command=horchata)
Horchata.grid(row=9,column=0,sticky=W)

#Casilla de entrada
textPepsi=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtPepsi)
textPepsi.grid(row=0,column=1)
textCocaCola=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtCoca)
textCocaCola.grid(row=1,column=1)
textSevenUp=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtSeven)
textSevenUp.grid(row=2,column=1)
textMirinda=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtMirinda)
textMirinda.grid(row=3,column=1)
textGrapete=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtGrapete)
textGrapete.grid(row=4,column=1)
textOrange=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtOrange)
textOrange.grid(row=5,column=1)
textLimonada=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtLimonada)
textLimonada.grid(row=6,column=1)
textNaranjada=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtNaranjada)
textNaranjada.grid(row=7,column=1)
textJamaica=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtJamaica)
textJamaica.grid(row=8,column=1)
textHorchata=Entry(marcoBebidas,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtHorchata)
textHorchata.grid(row=9,column=1)

#Postres
#Etiqueta y boton check
PastelChocolate=Checkbutton(marcoPostres,text='Pastel Chocolate',font=Subtitle,onvalue=1,offvalue=0, variable=var21,command=choco)
PastelChocolate.grid(row=0,column=0,sticky=W)
Brownie=Checkbutton(marcoPostres,text='Brownie',font=Subtitle,onvalue=1,offvalue=0, variable=var22,command=brownie)
Brownie.grid(row=1,column=0,sticky=W)
PastelTresLeches=Checkbutton(marcoPostres,text='Pastel Tres Leches',font=Subtitle,onvalue=1,offvalue=0, variable=var23,command=leche)
PastelTresLeches.grid(row=2,column=0,sticky=W)
PastelDeZanahoria=Checkbutton(marcoPostres,text='Pastel De Zanahoria',font=Subtitle,onvalue=1,offvalue=0, variable=var24, command=zanahoria)
PastelDeZanahoria.grid(row=3,column=0,sticky=W)
PastelDeManie=Checkbutton(marcoPostres,text='Pastel De Manie',font=Subtitle,onvalue=1,offvalue=0, variable=var25,command=manie)
PastelDeManie.grid(row=4,column=0,sticky=W)
PastelDeAlmendra=Checkbutton(marcoPostres,text='Pastel De Almendra',font=Subtitle,onvalue=1,offvalue=0, variable=var26,command=almendra)
PastelDeAlmendra.grid(row=5,column=0,sticky=W)
PieDeManzana=Checkbutton(marcoPostres,text='Pie De Manzana',font=Subtitle,onvalue=1,offvalue=0, variable=var27,command=manzana)
PieDeManzana.grid(row=6,column=0,sticky=W)
Churros=Checkbutton(marcoPostres,text='Churros',font=Subtitle,onvalue=1,offvalue=0, variable=var28,command=churros)
Churros.grid(row=7,column=0,sticky=W)
Rellenitos=Checkbutton(marcoPostres,text='Rellenitos',font=Subtitle,onvalue=1,offvalue=0, variable=var29,command=rellenitos)
Rellenitos.grid(row=8,column=0,sticky=W)
Flan=Checkbutton(marcoPostres,text='Flan',font=Subtitle,onvalue=1,offvalue=0, variable=var30,command=flan)
Flan.grid(row=9,column=0,sticky=W)
#Casilla de entrada
textPastelChocolate=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED,textvariable=txtchoco)
textPastelChocolate.grid(row=0,column=1)
textBrownie=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtbrownie)
textBrownie.grid(row=1,column=1)
textPastelTresLeches=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtleches)
textPastelTresLeches.grid(row=2,column=1)
textPastelDeZanahoria=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtzanahoria)
textPastelDeZanahoria.grid(row=3,column=1)
textPastelDeManie=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtmanie)
textPastelDeManie.grid(row=4,column=1)
textPastelDeAlmendra=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtalmendra)
textPastelDeAlmendra.grid(row=5,column=1)
textPastelDeManzana=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtmanzana)
textPastelDeManzana.grid(row=6,column=1)
textChurros=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtchurro)
textChurros.grid(row=7,column=1)
textRellenitos=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtrelleno)
textRellenitos.grid(row=8,column=1)
textFlan=Entry(marcoPostres,font=Subtitle,bd=7,width=8,state=DISABLED, textvariable=txtflan)
textFlan.grid(row=9,column=1)

#Etiquetas de totales y entradas para los valores
costoComida=Label(marcoCosto, text='Total en comida', font=Subtitle, bd=10, bg="blue",fg="white")
costoComida.grid(row=0,column=0)
casillaCostoComida=Entry(marcoCosto,font=Subtitle,bd=10, width=14, state="readonly")
casillaCostoComida.grid(row=0, column=1, padx=5)
costoBebidas=Label(marcoCosto, text="Total en bebidas", font=Subtitle,bd=10,width=14, bg="blue",fg="white")
costoBebidas.grid(row=1,column=0)
casillasCostoBebidas=Entry(marcoCosto, font=Subtitle,bd=10,width=14, fg="white", bg="blue", state="readonly")
casillasCostoBebidas.grid(row=1,column=1)
costoPostres=Label(marcoCosto,font=Subtitle,text="Total en postres", bd=10,bg="blue", fg="white")
costoPostres.grid(row=2,column=0)
casillaCostoPostres=Entry(marcoCosto,font=Subtitle,state="readonly",bd=10,width=14)
casillaCostoPostres.grid(row=2,column=1)

subtotal=Label(marcoCosto, text="Subtotal", font=Subtitle,bd=10, bg="blue",fg="white")
subtotal.grid(row=0,column=2)
casillasubtotal=Entry(marcoCosto,font=Subtitle,bd=10, width=14, state="readonly")
casillasubtotal.grid(row=0, column=3, padx=41)
iva=Label(marcoCosto, text="Impuesto IVA", font=Subtitle,bd=10,width=14, bg="blue",fg="white")
iva.grid(row=1,column=2)
casillaiva=Entry(marcoCosto, font=Subtitle,bd=10,width=14, fg="white", bg="blue", state="readonly")
casillaiva.grid(row=1,column=3)
pagoTotal=Label(marcoCosto,font=Subtitle,text="Pago Total", bd=10,bg="blue", fg="white")
pagoTotal.grid(row=2,column=2)
casillapagoTotal=Entry(marcoCosto,font=Subtitle,state="readonly",bd=10,width=14)
casillapagoTotal.grid(row=2,column=3)


#Programacion calculadora
operacion=''

def botonclick(numeros):
    global operacion
    operacion = operacion + numeros
    pantallacalculadora.delete(0,END)
    pantallacalculadora.insert(END,operacion)

def limpiar():
    global operacion
    operacion=''
    pantallacalculadora.delete(0,END)

def resultado():
    global operacion
    resultado=str(eval(operacion))
    pantallacalculadora.delete(0,END)
    pantallacalculadora.insert(0,resultado)
    operacion=''




#Calculadora de ayuda
pantallacalculadora=Entry(marcoCalculadora,font=('arial',19,'bold'),width=44, bd=4)
pantallacalculadora.grid(row=0,column=0, columnspan=4)
#Botones calculadora
boton7=Button(marcoCalculadora,text='7', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('7')).grid(row=1,column=0)
boton8=Button(marcoCalculadora,text='8', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('8')).grid(row=1,column=1)
boton9=Button(marcoCalculadora,text='9', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('9')).grid(row=1,column=2)
botonMas=Button(marcoCalculadora,text='+', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=lambda:botonclick('+')).grid(row=1,column=3)

boton4=Button(marcoCalculadora,text='4', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('4')).grid(row=2,column=0)
boton5=Button(marcoCalculadora,text='5', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('5')).grid(row=2,column=1)
boton6=Button(marcoCalculadora,text='6', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('6')).grid(row=2,column=2)
botonMenos=Button(marcoCalculadora,text='-', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=lambda:botonclick('-')).grid(row=2,column=3)

boton1=Button(marcoCalculadora,text='1', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('1')).grid(row=3,column=0)
boton2=Button(marcoCalculadora,text='2', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('2')).grid(row=3,column=1)
boton3=Button(marcoCalculadora,text='3', font=Subtitle,fg="red", bg="blue",bd=6,width=9, command=lambda:botonclick('3')).grid(row=3,column=2)
botonPor=Button(marcoCalculadora,text='*', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=lambda:botonclick('*')).grid(row=3,column=3)

botonIgual=Button(marcoCalculadora,text='=', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=resultado).grid(row=4,column=0)
botonBorrar=Button(marcoCalculadora,text='C', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=limpiar).grid(row=4,column=1)
boton0=Button(marcoCalculadora,text='0', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=lambda:botonclick('0')).grid(row=4,column=2)
botonDivision=Button(marcoCalculadora,text='/', font=Subtitle,fg="blue", bg="blue",bd=6,width=9, command=lambda:botonclick('/')).grid(row=4,column=3)

#Recibo
textoRecibo=Text(marcoRecibo, font=('arial',17,'bold'),bd=3,width=48,height=12)
textoRecibo.grid(row=0,column=0)
#Botones
botonTotal=Button(marcoBotones,text='Total',font=Subtitle, fg="red",bg="blue",bd=4,padx=9, command=grantotal).grid(row=0,column=0)
botonRecibo=Button(marcoBotones,text='Recibo',font=Subtitle, fg="red",bg="blue",bd=4,padx=9, command=recibo).grid(row=0,column=1)
botonGuardar=Button(marcoBotones,text='Guardar',font=Subtitle, fg="red",bg="blue",bd=4,padx=9, command=guardar).grid(row=0,column=2)
botonEnviar=Button(marcoBotones,text='Enviar',font=Subtitle, fg="red",bg="blue",bd=4,padx=9, command=enviar).grid(row=0,column=3)
botonBorrar=Button(marcoBotones,text='Borrar',font=Subtitle, fg="red",bg="blue",bd=4,padx=9, command=borrar).grid(row=0,column=4)

ventana.mainloop()
