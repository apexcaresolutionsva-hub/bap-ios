# BAP for iPhone

The BAP web app (app.buybap.com) packaged as a native iPhone app with Capacitor, plus GPS (driving for dollars) and camera.

**Build:** Actions → "Build BAP for iPhone (TestFlight)" → Run workflow. GitHub's macOS runner pulls the latest
BAP web app, generates the Xcode project, signs it and uploads it to App Store Connect / TestFlight.

**One-time setup (repository secrets):** `APPLE_TEAM_ID`, `ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_KEY_P8`
(an App Store Connect API key with the App Manager role). The app record must exist in App Store Connect
with bundle ID `com.buybap.app`.
