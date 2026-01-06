// =====================
// PARALLAX EFFECT
// =====================
function setupParallax() {
  const orbs = document.querySelectorAll(".orb");

  window.addEventListener("mousemove", (e) => {
    const mouseX = e.clientX / window.innerWidth;
    const mouseY = e.clientY / window.innerHeight;

    orbs.forEach((orb, index) => {
      const moveX = (mouseX - 0.5) * (50 + index * 20);
      const moveY = (mouseY - 0.5) * (50 + index * 20);

      orb.style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
  });
}

// =====================
// INITIALIZE
// =====================
document.addEventListener("DOMContentLoaded", () => {
  setupParallax();
});
