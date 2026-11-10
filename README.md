# 3D Print Toolbox

> Curated tools for **everything 3D printing** — slicers, CAD, model libraries, no-CAD generators, scanning, mesh repair, printer control, filament and calibration.

🌐 **Browse with search and filters:** https://syntaxslicer.github.io/3d-print-toolbox/

**137 tools** · Legend: 🆓 free · 💶 freemium/paid · 🔓 open source · 🌐 runs in browser · 🪄 no CAD needed · 🧑‍💻 needs coding · 🔑 login required

## Contents

- [🔪 Slicers](#-slicers)
- [📐 CAD & Modelling](#-cad--modelling)
- [🗂️ Model Libraries](#-model-libraries)
- [📦 Boxes & Organizers](#-boxes--organizers)
- [🔲 Gridfinity](#-gridfinity)
- [🏷️ Text, Tags & QR](#-text-tags--qr)
- [🖼️ Image to Print](#-image-to-print)
- [🗺️ Maps & Terrain](#-maps--terrain)
- [⚙️ Mechanical & Parametric](#-mechanical--parametric)
- [✨ AI 3D Generation](#-ai-3d-generation)
- [📷 3D Scanning](#-3d-scanning)
- [🩹 Mesh Repair & Reverse Engineering](#-mesh-repair--reverse-engineering)
- [🖥️ Printer Control & Monitoring](#-printer-control--monitoring)
- [🧵 Filament & Costs](#-filament--costs)
- [🎯 Calibration & G-code](#-calibration--g-code)
- [🏭 Print Services](#-print-services)
- [📚 Guides & Learning](#-guides--learning)
- [🧭 Directories & Hubs](#-directories--hubs)

## 🔪 Slicers

- **[OrcaSlicer](https://github.com/SoftFever/OrcaSlicer)** 🆓 🔓 — Feature-rich open-source slicer with profiles for most brands and built-in calibration tests (flow, PA, temp towers).
- **[PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/)** 🆓 🔓 — Prusa's mature open-source slicer: organic supports, variable layer height, SVG/text emboss, good third-party profiles.
- **[Bambu Studio](https://bambulab.com/en/download/studio)** 🆓 🔓 — Bambu Lab's slicer with multi-plate projects, AMS color painting and direct printer connection.
- **[UltiMaker Cura](https://ultimaker.com/software/ultimaker-cura/)** 🆓 🔓 — Long-standing slicer with a huge plugin marketplace and hundreds of fine-grained settings.
- **[ElegooSlicer](https://github.com/ELEGOO-3D/ElegooSlicer)** 🆓 🔓 — Orca-based slicer tuned for Elegoo FDM printers like the Centauri Carbon.
- **[SuperSlicer](https://github.com/supermerill/SuperSlicer)** 🆓 🔓 — PrusaSlicer fork with extra knobs and calibration menus for tinkerers.
- **[Lychee Slicer](https://lychee.mango3d.io/)** 💶 🔑 — Popular resin slicer with smart auto-supports, hollowing and island detection.
- **[CHITUBOX](https://www.chitubox.com/)** 💶 — Widely supported resin slicer for MSLA printers, with a Pro tier for advanced supports.
- **[Kiri:Moto](https://grid.space/kiri/)** 🆓 🔓 🌐 — Open-source slicer that runs entirely in the browser — FDM, SLA, CNC and laser. Handy on Chromebooks or locked-down PCs.
- **[Unlayered Slicer](https://unlayered3d.com/slicer)** 🆓 — OrcaSlicer fork that adds non-planar slicing on normal 3-axis printers, wave overhangs and 5-axis support. Free beta; Bambu wireless printing not yet supported.

## 📐 CAD & Modelling

- **[Tinkercad](https://www.tinkercad.com/)** 🆓 🌐 🔑 — Drag-and-drop CAD in the browser — the easiest start for simple functional parts and beginners. `STL · OBJ`
- **[Onshape](https://www.onshape.com/)** 💶 🌐 🔑 — Full parametric CAD in the browser. Free plan for hobbyists, documents are public. `STL · STEP · 3MF`
- **[Fusion](https://www.autodesk.com/products/fusion-360/personal)** 💶 🔑 — Autodesk's parametric CAD/CAM; free for personal, non-commercial use with some limits. `STL · STEP · 3MF`
- **[FreeCAD](https://www.freecad.org/)** 🆓 🔓 — Open-source parametric CAD; version 1.x fixed the topological naming problem and made it much more usable. `STL · STEP · 3MF`
- **[Shapr3D](https://www.shapr3d.com/)** 💶 🔑 — Touch- and pencil-friendly direct modelling on iPad, Mac and Windows. `STL · STEP`
- **[OpenSCAD](https://openscad.org/)** 🆓 🔓 🧑‍💻 — Model with code — the language behind most online customizers and generators. `STL · 3MF`
- **[build123d](https://github.com/gumyr/build123d)** 🆓 🔓 🧑‍💻 — Python code-CAD on the OpenCascade kernel — real B-rep, fillets and STEP export, great for parametric parts. `STL · STEP · 3MF`
- **[CadQuery](https://github.com/CadQuery/cadquery)** 🆓 🔓 🧑‍💻 — Python code-CAD with a fluent API, also on OpenCascade. `STL · STEP`
- **[ExportToPython](https://github.com/Visionware-Solutions/ExportToPython)** 🆓 🔓 🧑‍💻 — Fusion add-in that converts a Fusion design into build123d Python code — bridge from GUI modelling to parametric code.
- **[OCP CAD Viewer (VS Code)](https://github.com/bernhard-42/vscode-ocp-cad-viewer)** 🆓 🔓 🧑‍💻 — The standard live 3D viewer for build123d/CadQuery inside VS Code — show(), measure, explode, clip planes.
- **[Yet Another CAD Viewer](https://github.com/yeicor-3d/yet-another-cad-viewer)** 🆓 🔓 🌐 🧑‍💻 — Browser-based viewer for build123d/OCP models; share models as a static web page.
- **[CQ-editor (build123d fork)](https://github.com/jdegenstein/jmwright-CQ-Editor)** 🆓 🔓 🧑‍💻 — Standalone code editor with 3D preview and object tree, adapted for build123d.
- **[OCP.wasm](https://github.com/yeicor/OCP.wasm)** 🆓 🔓 🌐 🧑‍💻 — Runs build123d's OpenCascade stack in the browser via WebAssembly — basis for web-based parametric generators.
- **[partomatic](https://github.com/x0pherl/partomatic)** 🆓 🔓 🧑‍💻 — Framework for standardized parametric build123d models with config files and a web interface to generate variants.
- **[PartCAD](https://partcad.readthedocs.io/en/latest/)** 🆓 🔓 🧑‍💻 — Package manager for CAD: version, share and reuse build123d/CadQuery/OpenSCAD parts across projects.
- **[blendquery](https://github.com/uki-dev/blendquery)** 🆓 🔓 🧑‍💻 — Run build123d/CadQuery scripts inside Blender and keep them parametric there.
- **[Blender](https://www.blender.org/)** 🆓 🔓 — Sculpting and organic modelling for figures and art pieces; ships a 3D-Print Toolbox add-on. `STL · OBJ · 3MF`

## 🗂️ Model Libraries

- **[Printables](https://www.printables.com/)** 🆓 🌐 — Prusa's model library with good tagging, remixes, print profiles and contests.
- **[MakerWorld](https://makerworld.com/)** 🆓 🌐 — Bambu Lab's library with ready-to-print 3MF profiles and in-browser parametric customizers.
- **[Thingiverse](https://www.thingiverse.com/)** 🆓 🌐 — The oldest large model archive — huge back catalogue, including many OpenSCAD customizers.
- **[Thangs](https://thangs.com/)** 💶 🌐 — Model search across sites, including geometric search by uploading a similar shape.
- **[Cults3D](https://cults3d.com/)** 💶 🌐 — Marketplace for free and paid designs, strong on miniatures and decor.
- **[Yeggi](https://www.yeggi.com/)** 🆓 🌐 — Search engine that indexes printable models across most repositories.

## 📦 Boxes & Organizers

- **[Bento3D](https://bento3d.design/)** 🆓 🌐 🪄 — Design partitioned trays and matching hinged boxes to the millimeter, with a live 3D preview and STL export. `STL`
- **[PrintPal Bin Generator](https://www.printpal.io/tools/bin-generator)** 🆓 🌐 🪄 — Sorting trays and drawer bins with a rows × columns grid, wall/floor thickness and corner radius. `STL`
- **[MakerWorld Parametric Model Maker](https://makerworld.com/makerlab/parametricModelMaker)** 🆓 🌐 🪄 🔑 — Runs OpenSCAD models in the browser. Thousands of community generators for boxes, enclosures, trays, gears and name tags. `STL · 3MF`
- **[openGrid Tile Generator](https://makerworld.com/en/models/1304337-opengrid-tile-generator)** 🆓 🌐 🪄 🔑 — Generates openGrid wall/desk panels in any size for the open-source openGrid mounting system — the board everything else clips onto. `STL · 3MF`
- **[Parametric Multiboard Generator](https://makerworld.com/models/2238855)** 🆓 🌐 🪄 🔑 — Multiboard wall tiles sized to your wall and bed, generated in MakerWorld's customizer. `STL · 3MF`
- **[Multiconnect Hook Generator](https://makerworld.com/en/models/650660-multiconnect-hook-generator)** 🆓 🌐 🪄 🔑 — Custom hooks and holders with the Multiconnect back for Multiboard and openGrid. `STL · 3MF`

## 🔲 Gridfinity

- **[Perplexing Labs Gridfinity Generator](https://gridfinity.perplexinglabs.com/)** 🆓 🌐 🪄 — The most complete Gridfinity web UI: bins, baseplates, lids and rugged boxes, backed by Gridfinity Rebuilt and Extended. `STL`
- **[Gridfinity Bin Generator (Bouwens)](https://gridfinity.bouwens.co/)** 🆓 🌐 🪄 — CadQuery-based bin and baseplate generator — exports STEP as well as STL, so you can keep editing. `STL · STEP`
- **[Gridfinity Layout Tool](https://gridfinitylayouttool.com/)** 🆓 🌐 🪄 — Plan a whole drawer and generate bins and baseplates in the browser; works offline once loaded. `STL · STEP · 3MF`
- **[Tooltrace](https://www.tooltrace.ai/)** 💶 🌐 🪄 — Photograph tools on an A4/Letter sheet; AI traces the outlines and builds a Gridfinity insert or shadow-box foam layout. `STL · DXF · SVG`
- **[GridFlock](https://github.com/yawkat/gridflock)** 🆓 🔓 — Splits large Gridfinity baseplates into puzzle-locking pieces that fit small print beds. `STL`

## 🏷️ Text, Tags & QR

- **[QRcode2stl](https://printer.tools/qrcode2stl/)** 🆓 🔓 🌐 🪄 — QR codes for URLs, Wi-Fi, vCards and Spotify codes as printable tags, with optional text and keychain hole. `STL`
- **[3D Print QR Code](https://3dprintqrcode.com/)** 🆓 🌐 🪄 — Client-side QR tag generator with separate base/code heights, labels, icons and rounded corners. `STL`
- **[MakerWorld Image to Keychain](https://makerworld.com/makerlab/imageToKeychain)** 🆓 🌐 🪄 🔑 — Turns a logo or picture into a multi-color keychain ready for Bambu Studio. `3MF`

## 🖼️ Image to Print

- **[HueForge](https://shop.thehueforge.com/)** 💶 — Filament painting: turns images into layered multi-color reliefs using filament transmission values, printable with one nozzle and color swaps. `STL · 3MF`
- **[ItsLitho](https://itslitho.com/)** 💶 🌐 🪄 — Feature-rich lithophane maker: flat, curved, lamps, night lights and globes, with a built-in image editor. `STL · 3MF`
- **[3DP.Rocks Lithophane](https://3dp.rocks/lithophane/)** 🆓 🔓 🌐 🪄 — Fast, minimal lithophane generator with gamma/thickness controls and backlit preview. `STL`
- **[Lithophane Maker](https://www.lithophanemaker.com/)** 🆓 🌐 🪄 — Lots of lithophane shapes — lamps, ceiling-fan covers, night lights, ornaments. `STL`
- **[Cookiecad Designer](https://cookiecad.com/designer)** 💶 🌐 🪄 — Trace an image into cookie cutters, stamps, embossers, stencils or cake toppers, with a PDF size check. `STL · OBJ · 3MF`
- **[MakerWorld MakerLab](https://makerworld.com/makerlab)** 🆓 🌐 🪄 🔑 — Bambu's playground of free generators: PrintMon (AI figures), lithophanes, lanterns, pixel puzzles, keychains and more — printer-agnostic exports. `3MF · STL`

## 🗺️ Maps & Terrain

- **[Terrain2STL](https://jthatch.com/Terrain2STL/)** 🆓 🔓 🌐 🪄 — Draw a box on a world map and download the terrain as an STL. Global coverage. `STL`
- **[TouchTerrain](https://touchterrain.geol.iastate.edu/)** 🆓 🔓 🌐 🪄 — Research-grade terrain models from elevation data, with tiling for prints bigger than your bed. `STL · OBJ`
- **[CADMAPPER](https://cadmapper.com/)** 💶 🌐 — City blocks with buildings from OpenStreetMap — free up to 1 km². Exports CAD formats you convert before slicing. `DXF · SKP`

## ⚙️ Mechanical & Parametric

- **[OpenSCAD Playground](https://ochafik.com/openscad2)** 🆓 🔓 🌐 🪄 — OpenSCAD in the browser with Customizer UI: paste any .scad generator, tweak sliders, export multi-color 3MF. `STL · 3MF`
- **[Gear Generator](https://geargenerator.com/)** 🆓 🌐 🪄 — Lay out involute spur gear trains and planetaries visually, check ratios, export the profile. `SVG · DXF`
- **[YAPP Box](https://github.com/mrWheel/YAPP_Box)** 🆓 🔓 🧑‍💻 — Yet Another Parametric Projectbox: PCB enclosures with cutouts, standoffs and snap lids. Works in OpenSCAD Playground. `STL`
- **[BOSL2](https://github.com/BelfrySCAD/BOSL2)** 🆓 🔓 🌐 🧑‍💻 — The big OpenSCAD standard library: involute gears and racks, threads, hinges, snap/dovetail joiners, bottle caps, rounding and attachments. `STL · 3MF`
- **[threadlib](https://github.com/adrianschlatter/threadlib)** 🆓 🔓 🌐 🧑‍💻 — OpenSCAD library for standard threads (metric, UNC/UNF, pipe threads) with clean, printable geometry. `STL`
- **[threads.scad](https://github.com/rcolyer/threads-scad)** 🆓 🔓 🌐 🧑‍💻 — Lightweight OpenSCAD threads: bolts, nuts, threaded holes and rods with adjustable tolerance. `STL`
- **[NopSCADlib](https://github.com/nophead/NopSCADlib)** 🆓 🔓 🧑‍💻 — Huge OpenSCAD library of real-world 'vitamins' (screws, bearings, motors, PCBs, extrusions) plus printed parts and assembly views. `STL`
- **[bd_warehouse](https://bd-warehouse.readthedocs.io/en/latest/index.html)** 🆓 🔓 🧑‍💻 — build123d parts library: ISO fasteners, threads, bearings, flanges, pipes and sprockets as real B-rep solids. `STEP · STL`
- **[py_gearworks](https://github.com/GarryBGoode/py_gearworks)** 🆓 🔓 🧑‍💻 — Python gear framework on build123d: spur, helical, bevel and more, with proper meshing setups. `STEP · STL`
- **[bd_vslot](https://bd-vslot.readthedocs.io)** 🆓 🔓 🧑‍💻 — V-slot aluminium extrusion components for build123d — handy for printer frames and jigs. `STEP`
- **[bd_beams_and_bars](https://bd-beams-and-bars.3d.experimentslabs.com/)** 🆓 🔓 🧑‍💻 — build123d library of standard steel sections and bars (UPN, IPN, flat, round…) as 2D profiles and 3D beams. `STEP`
- **[dl4to4ocp](https://github.com/yeicor-3d/dl4to4ocp/)** 🆓 🔓 🧑‍💻 — Topology optimization for build123d/OCP models — lets material follow the load path before printing.
- **[ocp-freecad-cam](https://github.com/voneiden/ocp-freecad-cam)** 🆓 🔓 🧑‍💻 — Generate CNC toolpaths from build123d/CadQuery models using FreeCAD's CAM engine.
- **[Fusion 360 FDM Threads](https://github.com/DurbansPoison/Fusion-360-FDM-threads)** 🆓 🔓 — Custom trapezoidal thread profiles for Fusion with built-in clearance classes (e.g. 0.1e bolt + 0.1i nut) that actually print well.
- **[FreeCAD Fasteners Workbench](https://wiki.freecad.org/Fasteners_Workbench)** 🆓 🔓 — Adds standard screws, nuts, washers and heat-set-insert holes to FreeCAD models, snapped to holes. `STEP`
- **[KiCad StepUp](https://wiki.freecad.org/KicadStepUp_Workbench)** 🆓 🔓 — Round-trips PCBs between KiCad and FreeCAD so enclosures fit the real board, connectors and mounting holes. `STEP`
- **[3DPrintCalcs Mechanical](https://3dprintcalcs.uk/mechanical/)** 🆓 🌐 🪄 — Browser calculators for printed mechanics, including cantilever snap-fit dimensions.
- **[Parametric Vacuum Adapter Generator](https://makerworld.com/en/models/1600508)** 🆓 🌐 🪄 🔑 — Hose and vacuum adapters between any two diameters for workshop dust extraction, from a form. `STL · 3MF`
- **[McMaster-Carr](https://www.mcmaster.com/)** 🆓 🌐 — Free, accurate CAD models (STEP) of almost every screw, bearing, spring and profile — drop them into your design to check fits. `STEP`
- **[GrabCAD Library](https://grabcad.com/library)** 🆓 🌐 🔑 — Millions of community CAD models — motors, sensors, dev boards — to design mounts and housings around. `STEP · STL`

## ✨ AI 3D Generation

- **[Meshy](https://www.meshy.ai/)** 💶 🌐 🔑 — Text- and image-to-3D with remeshing and repair. Free tier is limited and non-commercial. `STL · OBJ · GLB`
- **[Tripo](https://www.tripo3d.ai/)** 💶 🌐 🔑 — Image- and text-to-3D with good topology and segmentation. Monthly free credits. `STL · OBJ · GLB`
- **[Zoo Design Studio](https://zoo.dev/)** 💶 🌐 🔑 — Text-to-CAD and code-CAD (KCL) that outputs real B-rep geometry instead of meshes. `STEP · STL`

## 📷 3D Scanning

- **[KIRI Engine](https://www.kiriengine.app/)** 💶 🌐 🔑 — Phone photogrammetry, LiDAR and Gaussian-splat scanning with mesh export. `STL · OBJ`
- **[RealityScan](https://www.realityscan.com/)** 🆓 🔑 — Epic's photogrammetry app and desktop tool, now free to use for most makers. `OBJ · FBX`
- **[Polycam](https://poly.cam/)** 💶 🌐 🔑 — LiDAR and photo scanning on phones; quick room and object captures. `STL · OBJ`
- **[Meshroom](https://alicevision.org/#meshroom)** 🆓 🔓 — Open-source photogrammetry pipeline (AliceVision) for desktop; needs a CUDA GPU for best results. `OBJ`

## 🩹 Mesh Repair & Reverse Engineering

- **[Formware Online STL Repair](https://www.formware.co/onlinestlrepair)** 🆓 🌐 🪄 — Upload a broken STL, get it back watertight: holes, flipped normals, non-manifold edges. `STL`
- **[iamRapid STL Repair](https://iamrapid.com/tools/repair-3d-file/)** 🆓 🌐 — Diagnoses and repairs STL/OBJ meshes locally in the browser — nothing gets uploaded. `STL · OBJ`
- **[Online 3D Viewer](https://3dviewer.net/)** 🆓 🔓 🌐 🪄 — Open-source viewer for STL, 3MF, OBJ, STEP and more, right in the browser — quick look and measure without installing anything. `STL · 3MF · OBJ · STEP`
- **[ImageToStl](https://imagetostl.com/)** 🆓 🌐 🪄 — Browser converters between almost any 3D and image format: SVG/PNG to STL, STEP/OBJ/3MF/GLB to STL and back. `STL · OBJ · 3MF · STEP`
- **[MeshLab](https://www.meshlab.net/)** 🆓 🔓 — Swiss-army knife for meshes: cleanup, decimation, remeshing, measuring scans. `STL · OBJ · PLY`
- **[Meshmixer](https://meshmixer.com/)** 🆓 — Classic for hollowing, cutting, tree supports and sculpt fixes. No longer developed, but still downloadable. `STL · OBJ`
- **[MeshInspector](https://meshinspector.com/feature/stl-file-repair/)** 💶 🌐 — Free in-browser repair tools without sign-up (fill holes, flip normals, fix tunnels, simplify); automatic healing and a desktop app for big scans are paid. `STL · OBJ · PLY · 3MF`
- **[CloudCompare](https://www.cloudcompare.org/)** 🆓 🔓 — Open-source point cloud and mesh processing: align scans, compare a print against its CAD (deviation color maps), clean and mesh point clouds. `STL · OBJ · PLY`
- **[Instant Meshes](https://github.com/wjakob/instant-meshes)** 🆓 🔓 — Turns messy scan triangles into clean, evenly spaced quad/tri meshes in seconds — great before editing or converting a scan. `OBJ · PLY`
- **[FreeCAD Reverse Engineering Workbench](https://wiki.freecad.org/Reverse_Engineering_Workbench)** 🆓 🔓 — Free scan-to-CAD toolkit in FreeCAD: fit planes, cylinders and B-spline surfaces to meshes or point clouds, then model on top. Closest free thing to Geomagic Design X. `STEP · STL`
- **[Detessellate](https://github.com/DesignWeaver3D/Detessellate)** 🆓 🔓 — FreeCAD macro workbench for turning STL/3MF meshes back into editable solids: align, mesh-to-body, auto-generate and clean coplanar sketches, then finish in PartDesign. `STEP`
- **[BumpMesh](https://www.bumpmesh.com/)** 🆓 🔓 🌐 🪄 — CNC Kitchen's texture tool: bakes real displacement textures (knurl, leather, wood…) onto STL/3MF/STEP models — a better fuzzy skin. Runs locally in the browser. `STL · 3MF`
- **[ScanRuler](https://scanruler.com/)** 🆓 🌐 — CNC Kitchen's scan analysis tool: fit spheres, cylinders and planes to a 3D scan, measure it, map deviation from CAD and check wall thickness. Runs locally in the browser.

## 🖥️ Printer Control & Monitoring

- **[Klipper](https://www.klipper3d.org/)** 🆓 🔓 — Firmware that moves the motion planning to a Raspberry Pi; input shaping, pressure advance, macros.
- **[Mainsail](https://docs.mainsail.xyz/)** 🆓 🔓 — Lightweight web interface for Klipper/Moonraker with G-code viewer and timelapse support.
- **[Fluidd](https://docs.fluidd.xyz/)** 🆓 🔓 — Alternative Klipper web UI with a clean dashboard and Spoolman integration.
- **[OctoPrint](https://octoprint.org/)** 🆓 🔓 — The classic web host for Marlin printers, with hundreds of plugins.
- **[Marlin](https://marlinfw.org/)** 🆓 🔓 — Most common open-source firmware for hobby FDM printers.
- **[Obico](https://www.obico.io/)** 💶 🔓 🌐 — AI spaghetti detection and remote access for OctoPrint, Klipper and Bambu; server can be self-hosted.
- **[SimplyPrint](https://simplyprint.io/)** 💶 🌐 🔑 — Cloud print management for single printers to farms: queue, cloud slicing, AI detection, user management.
- **[OctoEverywhere](https://octoeverywhere.com/)** 💶 🌐 🔑 — Secure remote access, notifications and AI detection for OctoPrint, Klipper and Bambu printers.
- **[Prusa Connect](https://connect.prusa3d.com/)** 🆓 🌐 🔑 — Prusa's free cloud dashboard for monitoring, queues and file transfer across Prusa printers.
- **[Open Bambu Networking](https://github.com/ClusterM/open-bambu-networking)** 🆓 🔓 — Open-source drop-in replacement for Bambu Studio's closed networking plugin. LAN-first: discovery, printing, file transfer and camera; also works with OrcaSlicer 2.3.2+.
- **[Bambuddy](https://github.com/maziggy/bambuddy)** 🆓 🔓 🌐 — Self-hosted print management for Bambu printers without Bambu Cloud: live monitoring, queue and scheduling, archive, fleet dispatch by loaded filament, optional headless Orca/Bambu Studio slicing. Live demo at demo.bambuddy.cool.
- **[PrintBuddy](https://github.com/vmhomelab/printbuddy)** 🆓 🔓 🌐 — One self-hosted dashboard for mixed fleets — Bambu, Klipper/Moonraker and PrusaLink — with filament tracking and print history. Early development, not production-ready yet.
- **[Printago](https://www.printago.io/)** 💶 🌐 🔑 — Cloud print-farm software built around Bambu printers (others too): automatic queue dispatch, slicing in the cloud, SKU-based order workflows for shops — no Raspberry Pi needed.
- **[Mobileraker](https://github.com/Clon1998/mobileraker)** 💶 🔓 — Polished phone app for Klipper/Moonraker printers with push notifications, webcam and multi-printer support.
- **[KlipperScreen](https://github.com/KlipperScreen/KlipperScreen)** 🆓 🔓 — Touchscreen UI for Klipper on a small HDMI/DSI display attached to the Pi.
- **[Home Assistant Bambu Lab](https://github.com/greghesp/ha-bambulab)** 🆓 🔓 — Brings Bambu printers into Home Assistant: status, AMS, camera, automations like switching off the enclosure fan or light after a print.

## 🧵 Filament & Costs

- **[Spoolman](https://github.com/Donkie/Spoolman)** 🆓 🔓 — Self-hosted spool inventory that tracks remaining filament per spool and syncs usage from Klipper/Moonraker and OctoPrint.
- **[FilaMan](https://github.com/ManuelW77/Filaman)** 🆓 🔓 — ESP32 + NFC + load cell filament manager: weighs spools, reads/writes NFC tags and syncs with Spoolman and Bambu printers.
- **[SpoolmanScale](https://github.com/Niko11111/SpoolmanScale)** 🆓 🔓 — DIY touchscreen spool scale (ESP32-S3, PN532 NFC, NAU7802) that shows remaining filament and syncs with Spoolman, FilaMan or BamBuddy. Around €50–60 in parts.
- **[Open Filament Database](https://openfilamentdatabase.org/)** 🆓 🔓 🌐 — Community-maintained, MIT-licensed database of filament brands, products and stores with a public API — a neutral data source for apps and spool managers.
- **[SpoolmanDB](https://github.com/Donkie/SpoolmanDB)** 🆓 🔓 🌐 — Open filament catalog (brand, material, color, density, spool weight) that Spoolman uses to prefill new spools.
- **[3D Filament Profiles](https://3dfilamentprofiles.com/)** 💶 🌐 — Searchable filament catalog with community print settings, colors and spool data, plus personal inventory tracking.
- **[FilamentColors.xyz](https://filamentcolors.xyz/)** 🆓 🔓 🌐 — Library of real, photographed filament swatches with color matching — find which filament actually matches a target color.
- **[Prusa Material Guide](https://help.prusa3d.com/materials)** 🆓 🌐 — Per-material cheat sheets: temperatures, bed surface, strengths, drying and safety notes.
- **[Omni 3D Printing Cost Calculator](https://www.omnicalculator.com/other/3d-printing)** 🆓 🌐 — Quick estimate of filament, electricity and machine cost per print.

## 🎯 Calibration & G-code

- **[Teaching Tech Calibration](https://teachingtechyt.github.io/calibration.html)** 🆓 🔓 🌐 — Step-by-step calibration with generated test G-code: first layer, flow, retraction, temperature, acceleration, linear advance.
- **[Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/)** 🆓 🔓 🌐 — Deep-dive tuning reference (pressure advance, extrusion multiplier, input shaping). Orca's built-in tests follow it.
- **[OrcaSlicer Calibration Wiki](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration)** 🆓 🔓 🌐 — How to use Orca's built-in temperature, flow, pressure advance, retraction and max-flow tests.
- **[Klippain Shake&Tune](https://github.com/Frix-x/klippain-shaketune)** 🆓 🔓 — Klipper module that turns accelerometer data into readable graphs for input shaping, belt tension comparison and frame resonances.
- **[FullControl](https://fullcontrol.xyz/)** 🆓 🔓 🌐 🪄 — Generate G-code directly from parametric designs — vases, lattices, test prints — without a slicer or CAD. `G-code`
- **[gCodeViewer](https://gcode.ws/)** 🆓 🔓 🌐 — Inspect G-code layer by layer locally in the browser, with print statistics.

## 🏭 Print Services

- **[Craftcloud](https://craftcloud3d.com/)** 💶 🌐 — Upload a file, compare prices and lead times from dozens of print services worldwide (FDM, SLS, MJF, resin, metal, CNC).
- **[JLC3DP](https://jlc3dp.com/)** 💶 🌐 — Low-cost industrial printing (SLA, MJF, SLS, metal) from the JLCPCB group — handy to add parts to a PCB order.

## 📚 Guides & Learning

- **[Simplify3D Print Quality Guide](https://www.simplify3d.com/resources/print-quality-troubleshooting/)** 🆓 🌐 — Photo-based troubleshooting: find the picture that looks like your failed print, get causes and fixes.
- **[Prusa Knowledge Base](https://help.prusa3d.com/)** 🆓 🌐 — Extensive, well-illustrated articles on print quality, materials and maintenance — useful beyond Prusa printers.
- **[CNC Kitchen](https://www.cnckitchen.com/)** 🆓 🌐 — Data-driven tests of part strength, infill, annealing, inserts and materials.
- **[All3DP](https://all3dp.com/)** 🆓 🌐 — Large magazine with guides, software round-ups and printer reviews.
- **[r/3Dprinting](https://www.reddit.com/r/3Dprinting/)** 🆓 🌐 — Big, active community for help with failed prints and printer questions.
- **[SolidCraft CAD](https://solidcraftcad.com/)** 🆓 🌐 — Guide to SolidCraft, an open-source parametric CAD app written in Rust: running it in the browser or on desktop, setting up its MCP server, and exporting STL or 3MF for printing.

## 🧭 Directories & Hubs

- **[printer.tools](https://printer.tools/)** 🆓 🌐 — Broad directory of 3D printing tools, guides and calculators.
- **[gridfinity.xyz](https://gridfinity.xyz/)** 🆓 🌐 — Community hub for the Gridfinity system with links to generators, specs and layout tools.

## Contributing

Add or fix a tool in [`tools.json`](tools.json), run `python scripts/build_readme.py`, open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Generated from tools.json — do not edit by hand. -->
