from playwright.sync_api import sync_playwright

OUTPUT_DIR = r"c:\Users\nachoruizhens\Desktop\Proyectos IA\hypeagent-web"

sites = [
    ("https://elguardiandechamberi.com", f"{OUTPUT_DIR}\\web_guardian.png"),
    ("https://primaveragomez.es", f"{OUTPUT_DIR}\\web_primavera.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for url, path in sites:
        page = browser.new_page(viewport={"width": 1200, "height": 800}, device_scale_factor=1)
        print(f"Loading {url} ...")
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.screenshot(path=path, full_page=False)
        print(f"Saved {path}")
        page.close()
    browser.close()

print("Done.")
