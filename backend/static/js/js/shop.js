fetch("http://127.0.0.1:5000/products")
  .then(res => res.json())
  .then(products => {
    console.log(products);
    // later: display products dynamically
  });
