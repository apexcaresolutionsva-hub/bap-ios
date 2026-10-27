// Copies the live BAP web app (app.buybap.com, built from the bap-app repo) into www/ so the iPhone build
// ships the current version. Run before `npx cap sync ios` (the GitHub Actions build does this automatically).
import { writeFile, mkdir } from "node:fs/promises";
const BASE = "https://raw.githubusercontent.com/apexcaresolutionsva-hub/bap-app/main/";
const FILES = ["index.html", "terms/index.html", "privacy/index.html", "refunds/index.html"];
for (const f of FILES) {
  const r = await fetch(BASE + f + "?t=" + Date.now());
  if (!r.ok) throw new Error(f + ": HTTP " + r.status);
  const out = "www/" + f;
  await mkdir(out.split("/").slice(0, -1).join("/"), { recursive: true });
  await writeFile(out, await r.text());
  console.log("fetched", f);
}
