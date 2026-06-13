document.addEventListener("DOMContentLoaded", () => {
    // Auto flash dismissal
    setTimeout(() => {
        document.querySelectorAll(".alert-dismissible").forEach(a => a.remove());
    }, 4500);

    // Filter cards
    const search = document.getElementById("localCatalogSearch");
    if (search) {
        search.addEventListener("input", e => {
            const word = e.target.value.toLowerCase();
            document.querySelectorAll(".food-item-card-wrapper").forEach(card => {
                const name = card.querySelector(".card-title").textContent.toLowerCase();
                card.style.display = name.includes(word) ? "block" : "none";
            });
        });
    }
});