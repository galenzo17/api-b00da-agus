# Introduccion

Me motiva trabajar en Buda.com por que creo en las crypto y la libertad que representan, el mercado y la adopción estan en edades tempranas y todavia queda mucho por innovar y en Buda.com llevan la delantera, por esto y mucho más me motive e hice esta API. 🎉<br>
Esta API integra tambien la api de Buda.com usando una cuenta y su respectiva autenticacion (que cuenta? la mía 😃, el ApiKey y ApiSecret estan guardados en una variable de entorno en mi proveedor cloud de turno 😉) el codigo completo de esta API lo puedes revisar en <https://github.com/galenzo17/api-b00da-agus>, además se puede obtener un Proof of Work con el string 'b00da' por defecto, puedes probar con otros string's si gustas.<br>




## <span id="api-example-for-a-submenu-entry">La respuesta 👀</span>

Haciendo una peticion GET a la siguiente url <https://api-b00da-agus.herokuapp.com/proofOfBuda> puedes comprobar este resultado. Puedes agregar ?text=TextoQueQuieras para obtener distintos resultados.

```json
{
    "hash": "0000616612596568a354910a66968b46b66fa5cbae36249a9544fa67b2533d22",
    "nonce": 106118,
    "text": "b00da"
}
```