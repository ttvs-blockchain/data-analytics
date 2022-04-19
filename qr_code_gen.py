import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv("data/qr_code_gen.csv")
    print(df)
    # data for Huawei P8 Personal Info QR Code Generation
    personal_huawei_p8 = df["test_0_0"]
    # data for Huawei P8 Certificate Info QR Code Generation
    certificate_huawei_p8 = df["test_0_1"]
    # data for iPhone 8 Personal Info QR Code Generation
    personal_iphone8 = df["test_1_0"]
    # data for iPhone 8 Certificate Info QR Code Generation
    certificate_iphone8 = df["test_1_1"]
    # data for iPhone 12 Mini Personal Info QR Code Generation
    personal_iphone12_mini = df["test_2_0"]
    # data for iPhone 12 Mini Certificate Info QR Code Generation
    certificate_iphone12_mini = df["test_2_1"]

    # plot Huawei P8 Personal Info QR Code Generation
    fig, ax = plt.subplots()
    
    bars = ax.bar(
        x=np.arange(personal_huawei_p8.size), height=personal_huawei_p8
    )
    ax.axhline(personal_huawei_p8.mean(), color='red', linewidth=2)
    ax.text(-1, 72, "72.2")
    print(personal_huawei_p8.mean())


    # Axis formatting.
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    # Grab the color of the bars so we can make the
    # text the same color.
    bar_color = bars[0].get_facecolor()

    # Add text annotations to the top of the bars.
    # Note, you'll have to adjust this slightly (the 0.3)
    # with different data.
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            round(bar.get_height(), 1),
            horizontalalignment='center',
            color=bar_color,
            weight='bold'
        )

    # set axis range
    ax.set_ylim(40, 90)

    fig.tight_layout()
    plt.show()

