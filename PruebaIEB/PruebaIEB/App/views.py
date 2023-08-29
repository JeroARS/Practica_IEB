from django.shortcuts import render, redirect
from .models import Productos

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        nuevo_producto = Productos(nombre=nombre, descripcion=descripcion, precio=precio)
        nuevo_producto.save()
        return redirect('detalle_producto')
    productos_disponibles = Productos.objects.all() 
    return render(request, 'crear_producto.html', {'productos_disponibles': productos_disponibles})

def detalle_producto(request):
    productos_disponibles = Productos.objects.all() 
    return render(request, 'detalle_producto.html', {'productos_disponibles': productos_disponibles})

def mostrar_informacion(request):
    productos = Productos.objects.all()
    return render(request, 'mostrar_informacion.html', {'productos': productos})

from django.shortcuts import render, redirect
from .models import Productos, DetalleProductos

def guardar_detalle(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        
        try:
            producto = Productos.objects.get(id_producto=producto_id)
            
            # Calcular Valor Total y Valor IVA
            valor_total = producto.precio * cantidad
            valor_iva = valor_total * 0.19
            
            # Guardar detalle en la base de datos
            detalle = DetalleProductos(
                producto=producto,
                cantidad=cantidad,
                valor_total=valor_total,
                valor_iva=valor_iva
            )
            detalle.save()
            
            return redirect('mostrar_informacion')
        except Productos.DoesNotExist:
            # Manejar el caso si el producto no existe
            return render(request, 'error.html', {'mensaje': 'Producto no encontrado'})
    
    # Otras acciones si la solicitud no es POST
    return render(request, 'error.html', {'mensaje': 'Método no permitido'})
