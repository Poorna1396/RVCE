window.addEventListener('load', e => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/js/serviceworker.js', { scope: '/' }).then(function (registration) {
            // Registration was successful
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function (err) {
            // registration failed :(
            console.log('ServiceWorker registration failed: ', err);
        });
    } else {
        console.log('Service Worker is not supported in this browser.');
    }
});