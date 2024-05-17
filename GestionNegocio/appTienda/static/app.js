function eliminarProducto(id) {
    Swal.fire({
        title: "¿Está usted seguro de querer eliminar el Producto",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO"
    }).then((result) => {
        if (result.isConfirmed) {
            location.href = "/eliminarProducto/" + id
        }
    });
}