import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "7 Kebiasaan Anak Indonesia Hebat"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 24
    page.bgcolor = "#F8FAFC"
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- Header Aplikasi ---
    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Icon(ft.icons.STAR_ROUNDED, color=ft.colors.AMBER_600, size=36),
                    padding=10,
                    bgcolor=ft.colors.AMBER_50,
                    border_radius=50,
                ),
                ft.Text("7 Kebiasaan Anak Hebat", size=26, weight=ft.FontWeight.BOLD, color="#1E293B"),
                ft.Text("Developed by: Dennis Pardjer", size=13, weight=ft.FontWeight.W_600, color=ft.colors.INDIGO_600),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6
        ),
        alignment=ft.alignment.center,
        padding=10
    )

    # --- Section 1: Form Absensi (Nama & Tanggal) ---
    input_nama = ft.TextField(
        label="Nama Lengkap",
        hint_text="Masukkan nama kamu...",
        prefix_icon=ft.icons.PERSON_ROUNDED,
        border_radius=12,
        border_color="#CBD5E1",
        focused_border_color=ft.colors.INDIGO_500,
        bgcolor=ft.colors.WHITE,
        expand=True
    )

    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d")
    input_tanggal = ft.TextField(
        label="Tanggal Absen",
        value=tanggal_sekarang,
        prefix_icon=ft.icons.CALENDAR_MONTH_ROUNDED,
        border_radius=12,
        border_color="#CBD5E1",
        focused_border_color=ft.colors.INDIGO_500,
        bgcolor=ft.colors.WHITE,
        expand=True
    )

    form_absensi = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.BADGE_ROUNDED, color=ft.colors.INDIGO_600, size=20),
                        ft.Text("Identitas Siswa", size=16, weight=ft.FontWeight.BOLD, color="#334155")
                    ],
                    spacing=8
                ),
                ft.Divider(height=15, color="#E2E8F0"),
                ft.ResponsiveRow(
                    controls=[
                        ft.Container(content=input_nama, col={"sm": 12, "md": 6}),
                        ft.Container(content=input_tanggal, col={"sm": 12, "md": 6}),
                    ]
                )
            ]
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=16,
        border=ft.border.all(1, "#E2E8F0"),
    )

    # --- Section 2: Daftar 7 Kebiasaan dengan Ikon Unik ---
    kebiasaan_data = [
        {"label": "1. Bangun Pagi Tepat Waktu", "icon": ft.icons.WB_SUNNY_ROUNDED},
        {"label": "2. Beribadah dan Berdoa", "icon": ft.icons.MOSQUE_ROUNDED},
        {"label": "3. Merapikan Tempat Tidur & Membantu", "icon": ft.icons.CLEANING_SERVICES_ROUNDED},
        {"label": "4. Mandi Bersih dan Sarapan Sehat", "icon": ft.icons.RESTAURANT_ROUNDED},
        {"label": "5. Belajar dan Membaca Buku", "icon": ft.icons.AUTO_STORIES_ROUNDED},
        {"label": "6. Berolahraga / Aktivitas Fisik", "icon": ft.icons.DIRECTIONS_RUN_ROUNDED},
        {"label": "7. Tidur Malam Tidak Terlalu Larut", "icon": ft.icons.NIGHTS_STAY_ROUNDED}
    ]

    checkbox_rows = []
    checkboxes = []

    for item in kebiasaan_data:
        cb = ft.Checkbox(
            label=item["label"], 
            value=False, 
            fill_color=ft.colors.INDIGO_600,
            check_color=ft.colors.WHITE
        )
        checkboxes.append(cb)
        
        row_item = ft.Row(
            controls=[
                ft.Icon(item["icon"], color=ft.colors.INDIGO_400, size=20),
                cb
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        checkbox_rows.append(row_item)

    form_kebiasaan = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CHECKLIST_ROUNDED, color=ft.colors.INDIGO_600, size=20),
                        ft.Text("Daftar Kebiasaan Hari Ini", size=16, weight=ft.FontWeight.BOLD, color="#334155")
                    ],
                    spacing=8
                ),
                ft.Divider(height=15, color="#E2E8F0"),
                ft.Column(controls=checkbox_rows, spacing=8)
            ]
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=16,
        border=ft.border.all(1, "#E2E8F0"),
    )

    # --- Section 3: Status & Output Hasil ---
    txt_hasil = ft.Text(value="", size=14, weight=ft.FontWeight.W_600, text_align=ft.TextAlign.CENTER)

    def simpan_absensi(e):
        nama = input_nama.value.strip()
        tgl = input_tanggal.value.strip()

        if not nama:
            txt_hasil.value = "⚠️ Harap masukkan nama lengkap terlebih dahulu!"
            txt_hasil.color = ft.colors.RED_600
        else:
            tercentang = [cb.label for cb in checkboxes if cb.value]
            
            txt_hasil.value = (
                f"✅ Absen Berhasil Disimpan!\n"
                f"Nama: {nama} | Tanggal: {tgl}\n"
                f"Hebat! Kamu menyelesaikan {len(tercentang)} dari 7 kebiasaan hari ini."
            )
            txt_hasil.color = ft.colors.GREEN_700
        
        page.update()

    btn_simpan = ft.ElevatedButton(
        text="Simpan Absen & Kebiasaan",
        icon=ft.icons.SAVE_ROUNDED,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.INDIGO_600,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=2
        ),
        on_click=simpan_absensi
    )

    footer = ft.Text("© 2026 Aplikasi 7 Kebiasaan • Developed by Dennis Pardjer", size=11, color="#94A3B8")

    # --- Menambahkan Semua Elemen ke Halaman ---
    page.add(
        ft.Column(
            controls=[
                header,
                ft.Container(height=10),
                form_absensi,
                ft.Container(height=15),
                form_kebiasaan,
                ft.Container(height=15),
                ft.Container(
                    content=btn_simpan,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=5),
                ft.Container(
                    content=txt_hasil,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=20),
                ft.Container(
                    content=footer,
                    alignment=ft.alignment.center
                )
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )
    )

if __name__ == "__main__":
    ft.app(target=main)