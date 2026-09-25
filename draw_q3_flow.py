from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon
from matplotlib.font_manager import FontProperties, fontManager


OUT = Path(__file__).parent / "figures"
FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
FONT_BOLD_PATH = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
fontManager.addfont(FONT_PATH)
fontManager.addfont(FONT_BOLD_PATH)
FONT = FontProperties(fname=FONT_PATH)
FONT_BOLD = FontProperties(fname=FONT_BOLD_PATH)
NAVY = "#1F4E79"
BLUE = "#2F75B5"
TEAL = "#2A9D8F"
ORANGE = "#E07A16"
INK = "#243447"
PALE_BLUE = "#EAF2F8"
PALE_TEAL = "#E8F5F2"
PALE_ORANGE = "#FFF1E3"
PALE_GRAY = "#F4F6F7"


def box(ax, x, y, w, h, text, face, edge, size=11, weight="normal"):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.012,rounding_size=0.025",
        linewidth=1.4, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(patch)
    text_color = "white" if edge == NAVY else INK
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=text_color, fontsize=size, fontweight=weight, fontproperties=FONT,
            linespacing=1.25)


def arrow(ax, x1, y1, x2, y2, color=INK, lw=1.4, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=12, linewidth=lw,
                                 color=color, shrinkA=3, shrinkB=3))


def finish(fig, stem):
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight", pad_inches=0.05)
    fig.savefig(OUT / f"{stem}.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


def overall():
    fig, ax = plt.subplots(figsize=(11.5, 5.35))
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 5.35); ax.axis("off")
    header_edge = "#8A949E"
    panel_edge = "#66727D"
    dark_blue = "#385A98"
    dark_red = "#C53D4B"
    dark_green = "#5A8E35"
    light_blue = "#DCE6F5"
    light_orange = "#F8E4D1"
    light_green = "#E1EED8"

    ax.add_patch(Rectangle((0.18, 4.78), 11.14, 0.40,
                           facecolor="white", edgecolor=header_edge, linewidth=1.0))
    ax.text(5.75, 4.98, "问题三联合资源配置流程", ha="center", va="center",
            fontsize=14, fontproperties=FONT_BOLD, color="#20252B")

    columns = [
        (0.18, "前两问输入", "质量、配方与响应接口", dark_blue, light_blue),
        (3.96, "联合优化", "预算账本与有限支持域", dark_red, light_orange),
        (7.74, "结果检验", "候选配置与结构判定", dark_green, light_green),
    ]
    for x, title, subtitle, color, face in columns:
        ax.add_patch(Rectangle((x, 4.18), 3.58, 0.44,
                               facecolor=color, edgecolor=panel_edge, linewidth=0.9))
        ax.text(x + 1.79, 4.40, title, ha="center", va="center",
                fontsize=11.5, fontproperties=FONT_BOLD, color="white")
        ax.add_patch(Rectangle((x, 3.86), 3.58, 0.32,
                               facecolor="white", edgecolor=panel_edge, linewidth=0.9))
        ax.text(x + 1.79, 4.02, subtitle, ha="center", va="center",
                fontsize=8.7, fontproperties=FONT_BOLD, color="#303840")
        ax.add_patch(Rectangle((x, 0.72), 3.58, 3.14,
                               facecolor=face, edgecolor=panel_edge, linewidth=0.9))

    def plain_box(x, y, w, h, text, face="white", edge="#5E6974", size=9.7, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.015,rounding_size=0.035",
                                    facecolor=face, edgecolor=edge, linewidth=0.9))
        text_color = "white" if face == dark_green else "#202A33"
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=size, fontproperties=FONT_BOLD if bold else FONT,
                color=text_color, linespacing=1.18)

    def connect(x1, y1, x2, y2, color="#65717C", rad=0.0, lw=1.25):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=11, linewidth=lw, color=color,
                                     shrinkA=3, shrinkB=3,
                                     connectionstyle=f"arc3,rad={rad}"))

    # Inputs from the two preceding questions and C7.
    plain_box(0.52, 3.22, 2.90, 0.46, "问题一：固定 Q^(17)", edge=dark_blue, bold=True)
    plain_box(0.52, 2.43, 2.90, 0.46, "A4真实配方：512行")
    plain_box(0.52, 1.60, 2.90, 0.52, "问题二：13域响应\nL_k(N,D,p)", size=9.2)
    connect(1.97, 3.22, 1.97, 2.89, color=dark_blue)
    connect(1.97, 2.43, 1.97, 2.12, color=dark_blue)

    # Joint decision and cost accounting.
    plain_box(4.28, 3.30, 2.88, 0.43, "外生 L_ctx：C7 五个可行值", size=9.0)
    plain_box(4.28, 2.60, 2.88, 0.43, "决策变量：N、D、p、Q", size=9.2)
    plain_box(4.28, 1.85, 2.88, 0.47, "C_train + C_attn + C_Q ≤ C", size=9.2)
    plain_box(4.28, 1.06, 2.88, 0.47, "p=A^T w，w≥0，1^T w=1", size=9.2)
    connect(5.72, 3.30, 5.72, 3.03, color=dark_red)
    connect(5.72, 2.60, 5.72, 2.32, color=dark_red)
    connect(5.72, 1.85, 5.72, 1.53, color=dark_red)

    # Verification and reporting.
    plain_box(8.08, 3.28, 2.90, 0.45, "多起点约束求解", edge=dark_green, bold=True, size=9.1)
    plain_box(8.08, 2.57, 2.90, 0.45, "消融、敏感性与独立复算", size=9.1)
    plain_box(8.08, 1.86, 2.90, 0.45, "有限候选与结构转移判定", size=9.0)
    plain_box(8.08, 1.05, 2.90, 0.52, "N*、D*、p*、Q*\n及审计记录", face=dark_green, edge=dark_green,
              size=9.3, bold=True)
    connect(9.53, 3.28, 9.53, 3.02, color=dark_green)
    connect(9.53, 2.57, 9.53, 2.32, color=dark_green)
    connect(9.53, 1.86, 9.53, 1.57, color=dark_green)

    # Hand-off arrows between the three work areas.
    connect(3.52, 2.00, 4.25, 2.00, color=dark_blue, lw=1.5)
    connect(7.35, 2.02, 8.05, 2.02, color=dark_red, lw=1.5)

    ax.add_patch(Rectangle((0.18, 0.18), 11.14, 0.34,
                           facecolor="white", edgecolor=header_edge, linewidth=0.8))
    ax.text(5.75, 0.35,
            "Q^(17)为前两问交接的固定域质量向量；Q为联合优化中的治理质量变量。",
            ha="center", va="center", fontsize=8.5, fontproperties=FONT, color="#46515B")
    finish(fig, "flow_overall_model")


def support_audit():
    fig, ax = plt.subplots(figsize=(11.5, 5.35))
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 5.35); ax.axis("off")
    header_edge = "#8A949E"
    panel_edge = "#66727D"
    dark_blue = "#385A98"
    dark_red = "#C53D4B"
    dark_green = "#5A8E35"
    light_blue = "#DCE6F5"
    light_orange = "#F8E4D1"
    light_green = "#E1EED8"
    light_gray = "#F4F5F6"

    # Reference-style title band and three colored work areas.
    ax.add_patch(Rectangle((0.18, 4.78), 11.14, 0.40,
                           facecolor="white", edgecolor=header_edge, linewidth=1.0))
    ax.text(5.75, 4.98, "真实锚点扩展与参考解检验流程", ha="center", va="center",
            fontsize=14, fontproperties=FONT_BOLD, color="#20252B")

    columns = [
        (0.18, "支持域建立", "真实配方与候选锚点", dark_blue, light_blue),
        (3.96, "改善方向扫描", "有限方向与重新求解", dark_red, light_orange),
        (7.74, "候选复核", "场景稳健性与识别边界", dark_green, light_green),
    ]
    for x, title, subtitle, color, face in columns:
        ax.add_patch(Rectangle((x, 4.18), 3.58, 0.44,
                               facecolor=color, edgecolor=panel_edge, linewidth=0.9))
        ax.text(x + 1.79, 4.40, title, ha="center", va="center",
                fontsize=11.5, fontproperties=FONT_BOLD, color="white")
        ax.add_patch(Rectangle((x, 3.86), 3.58, 0.32,
                               facecolor="white", edgecolor=panel_edge, linewidth=0.9))
        ax.text(x + 1.79, 4.02, subtitle, ha="center", va="center",
                fontsize=8.7, fontproperties=FONT_BOLD, color="#303840")
        ax.add_patch(Rectangle((x, 0.72), 3.58, 3.14,
                               facecolor=face, edgecolor=panel_edge, linewidth=0.9))

    def plain_box(x, y, w, h, text, face="white", edge="#5E6974", size=9.7, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.015,rounding_size=0.035",
                                    facecolor=face, edgecolor=edge, linewidth=0.9))
        text_color = "white" if face == dark_green else "#202A33"
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=size, fontproperties=FONT_BOLD if bold else FONT,
                color=text_color, linespacing=1.18)

    def decision(x, y, w, h, text):
        points = [(x + w / 2, y + h), (x + w, y + h / 2),
                  (x + w / 2, y), (x, y + h / 2)]
        ax.add_patch(Polygon(points, closed=True, facecolor="#FFF1DA",
                              edgecolor="#C77B21", linewidth=1.0))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=8.8, fontproperties=FONT_BOLD, color="#55360E",
                linespacing=1.15)

    def connect(x1, y1, x2, y2, color="#65717C", rad=0.0, lw=1.25):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                     mutation_scale=11, linewidth=lw, color=color,
                                     shrinkA=3, shrinkB=3,
                                     connectionstyle=f"arc3,rad={rad}"))

    # Column 1: support domain.
    plain_box(0.52, 3.22, 2.90, 0.46, "A4真实配方：512行", face="white", edge=dark_blue, bold=True)
    plain_box(0.52, 2.43, 2.90, 0.46, "25个初始锚点 / 97个扩展锚点")
    plain_box(0.52, 1.60, 2.90, 0.52, "有限凸组合\np=A^T w,  w≥0,  1^T w=1", size=9.2)
    connect(1.97, 3.22, 1.97, 2.89, color=dark_blue)
    connect(1.97, 2.43, 1.97, 2.12, color=dark_blue)

    # Column 2: scan and decision loop.
    plain_box(4.28, 3.30, 2.88, 0.43, "固定 N、D、Q，扫描512个真实配方", size=9.0)
    plain_box(4.28, 2.60, 2.88, 0.43, "两步长方向检查\nt∈{10^-4, 10^-3}", size=9.2)
    decision(5.05, 1.67, 1.35, 0.62, "发现严格\n改善？")
    plain_box(4.28, 0.92, 1.70, 0.46, "否：保留候选\n并记录方向", face=light_gray, edge="#7A8793", size=8.7)
    plain_box(6.20, 0.92, 1.12, 0.46, "是：加入至多4个\n重新求解", face="white", edge=dark_red, size=8.4)
    connect(5.72, 3.30, 5.72, 3.03, color=dark_red)
    connect(5.72, 2.60, 5.72, 2.29, color=dark_red)
    connect(5.72, 1.67, 5.14, 1.38, color="#7A8793", rad=0.05)
    connect(6.40, 1.98, 6.76, 1.38, color=dark_red, rad=-0.04)
    ax.text(5.23, 1.48, "否", fontsize=8.5, fontproperties=FONT_BOLD, color="#596570")
    ax.text(6.36, 1.76, "是", fontsize=8.5, fontproperties=FONT_BOLD, color=dark_red)
    # Loop from adding a point back to the scan box.
    ax.add_patch(FancyArrowPatch((6.76, 1.38), (6.96, 3.51), arrowstyle="-|>",
                                 mutation_scale=10, linewidth=1.15, color=dark_red,
                                 connectionstyle="arc3,rad=0.42", shrinkA=3, shrinkB=3))

    # Column 3: acceptance and audit.
    plain_box(8.08, 3.28, 2.90, 0.45, "可行、有限且各域Loss为正", edge=dark_green, bold=True, size=9.1)
    plain_box(8.08, 2.57, 2.90, 0.45, "预算、上下文与成本情景复核", size=9.1)
    plain_box(8.08, 1.86, 2.90, 0.45, "近等价配置与跨阈值反例审查", size=9.0)
    plain_box(8.08, 1.05, 2.90, 0.52, "有限候选库\n推荐配置 + 审计记录", face=dark_green, edge=dark_green,
              size=9.3, bold=True)
    connect(9.53, 3.28, 9.53, 3.02, color=dark_green)
    connect(9.53, 2.57, 9.53, 2.32, color=dark_green)
    connect(9.53, 1.86, 9.53, 1.57, color=dark_green)
    # Inter-column hand-off arrows.
    connect(3.52, 2.00, 4.25, 2.00, color=dark_blue, lw=1.5)
    connect(7.35, 2.02, 8.05, 2.02, color=dark_red, lw=1.5)

    ax.add_patch(Rectangle((0.18, 0.18), 11.14, 0.34,
                           facecolor="white", edgecolor=header_edge, linewidth=0.8))
    ax.text(5.75, 0.35,
            "未收敛、无改善方向和近等价反例不进入推荐，但统一保留在审计记录中。",
            ha="center", va="center", fontsize=8.5, fontproperties=FONT, color="#46515B")
    finish(fig, "flow_q3_model")


if __name__ == "__main__":
    overall()
    support_audit()
