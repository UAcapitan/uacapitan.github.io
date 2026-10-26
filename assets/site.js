document.documentElement.classList.add('js');
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
if (menu && nav) {
  menu.hidden = false;
  const closeMenu = () => { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); };
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
}
const controls = document.querySelector('.catalog-controls');
if (controls) {
  controls.hidden = false;
  const cards = [...document.querySelectorAll('.game-card')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const search = document.querySelector('#game-search');
  let genre = 'all';
  const applyFilters = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    cards.forEach(card => {
      const show = (genre === 'all' || card.dataset.genre === genre) && card.dataset.search.includes(query);
      card.hidden = !show;
      if (show) count++;
    });
    buttons.forEach(button => { const active = button.dataset.filter === genre; button.classList.toggle('active', active); button.setAttribute('aria-pressed', String(active)); });
    document.querySelector('.empty-state').hidden = count !== 0;
    document.querySelector('#filter-status').textContent = `${count} ${count === 1 ? 'game' : 'games'} found`;
  };
  buttons.forEach(button => button.addEventListener('click', () => { genre = button.dataset.filter; applyFilters(); }));
  search.addEventListener('input', applyFilters);
  document.querySelector('#reset-filters').addEventListener('click', () => { genre = 'all'; search.value = ''; applyFilters(); search.focus(); });
}
document.querySelectorAll('[data-year]').forEach(element => { element.textContent = new Date().getFullYear(); });
