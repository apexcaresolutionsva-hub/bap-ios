"""Applies BAP's iOS settings to the generated Capacitor project: permission messages, encryption
declaration, version numbers, app icon and launch screen. Run after `npx cap add ios` / `npx cap sync ios`."""
import glob, os, plistlib, sys
from PIL import Image, ImageDraw, ImageFont

APP = "ios/App/App"
version = os.environ.get("APP_VERSION", "1.0.0")
build = os.environ.get("BUILD_NUMBER", "1")

p = f"{APP}/Info.plist"
d = plistlib.load(open(p, "rb"))
d.update({
    "CFBundleDisplayName": "BAP",
    "CFBundleShortVersionString": version,
    "CFBundleVersion": build,
    "NSLocationWhenInUseUsageDescription": "BAP uses your location to drop a pin and look up the property in front of you while driving for dollars.",
    "NSCameraUsageDescription": "BAP uses the camera so you can take photos of properties and attach them to your leads.",
    "NSPhotoLibraryUsageDescription": "BAP lets you choose property photos from your library to attach to your leads.",
    "NSPhotoLibraryAddUsageDescription": "BAP can save property photos you take to your photo library.",
    "ITSAppUsesNonExemptEncryption": False,
})
plistlib.dump(d, open(p, "wb"))

def font(size):
    for f in ["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

def art(w, h, bg, scale):
    im = Image.new("RGB", (w, h), bg); dr = ImageDraw.Draw(im)
    s = min(w, h) * scale; cx, cy = w / 2, h / 2
    dr.line([(cx - s * .30, cy - s * .02), (cx, cy - s * .27), (cx + s * .30, cy - s * .02)], fill="white", width=int(s * .055), joint="curve")
    f = font(int(s * .25)); b = dr.textbbox((0, 0), "BAP", font=f)
    dr.text((cx - (b[2] - b[0]) / 2 - b[0], cy + s * .03 - b[1]), "BAP", font=f, fill="white")
    return im

art(1024, 1024, (31, 63, 160), 1.0).save(f"{APP}/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png")
for sp in glob.glob(f"{APP}/Assets.xcassets/Splash.imageset/*.png"):
    w, h = Image.open(sp).size
    art(w, h, (15, 20, 27), .35).save(sp)
print(f"prepared iOS project: version {version} ({build})")
