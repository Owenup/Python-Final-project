import plotly as py
import cufflinks as cf
import pandas as pd
from flask import Flask
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline, Grid, Page
from flask import render_template, request

app = Flask(__name__)
file = open("./static/data/duizhao", encoding="utf-8").read().split("\n")
ss1 = file[::3]
ss = file[2::3]
city = {i: j for i, j in zip(ss, ss1)}


# 2010-2017各国贫困率
@app.route('/pkl')
def index_bar():
    df = pd.read_csv('./static/data/pinkunlv.csv')

    tl = Timeline()
    for i in range(2010, 2018):
        c = (
            Map()
                .add("世界地图",
                     [(city[i], j) for i, j in zip(list(df['Country Name']), list(df['{}年'.format(i)])) if
                      city.get(i, None)],
                     "world")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各国贫困率".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=80),
            )
        )
        tl.add(c, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text1='''通过贫困率和贫困人口的两张地图对比可得，地图都有类似的点 两张地图颜色分布和变化趋势大致相同，可以得出贫困率跟贫困人口相关。
                            两份数据图的中东地区数据是都偏大的随着年份的增加，变化都不是很大 我们还可以看出随着年份的增加，尽管全球总体贫困率有所下降，尤其是在中国和拉丁美洲的多数地区，但非洲和部分亚洲地区的贫困率仍居高不下。
                           通过各国人均GDP和贫困率的两张地图对比可得到： 人均GDP和贫困率有一定的关系，欧洲有些高收入国家贫困率的数据也不低，说明人均GDP与贫困率的关系不大，但是也有一定的关系。看人均GDP和贫困人口，不能全面衡量和比较国
                           与国之间贫困率的差异贫富差距和社会保障，是决定国家贫困率的另外两个重要因素。''')


# 2010-2017各国贫困率
@app.route('/renkou')
def index_bar_every_1_tp():
    df = pd.read_csv("./static/data/pinkunrenkou.csv")
    tl = Timeline()
    for i in range(2010, 2018):
        c = (
            Map()
                .add("世界地图",
                     [(city[i], j) for i, j in zip(list(df['Country Name']), list(df['{}年'.format(i)])) if
                      city.get(i, None)],
                     "world")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各国贫困人口".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=80),
            )
        )
        tl.add(c, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text1='''通过贫困率和贫困人口的两张地图对比可得，地图都有类似的点 两张地图颜色分布和变化趋势大致相同，可以得出贫困率跟贫困人口相关。 
                           两份数据图的中东地区数据是都偏大的随着年份的增加，变化都不是很大 我们还可以看出随着年份的增加，尽管全球总体贫困率有所下降，尤其是在中国和拉丁美洲的多数地区，但非洲和部分亚洲地区的贫困率仍居高不下。
                           通过各国人均GDP和贫困率的两张地图对比可得到： 人均GDP和贫困率有一定的关系，欧洲有些高收入国家贫困率的数据也不低，说明人均GDP与贫困率的关系不大，
                           但是也有一定的关系。看人均GDP和贫困人口，不能全面衡量和比较国与国之间贫困率的差异贫富差距和社会保障，是决定国家贫困率的另外两个重要因素。''')


# 2010-2017各国人均GDP
@app.route('/GDP')
def index_bar_every():
    df = pd.read_csv('./static/data/renjunGDP.csv')
    tl = Timeline()
    for i in range(2010, 2018):
        c = (
            Map()
                .add("世界地图",
                     [(city[i], j) for i, j in zip(list(df['Country Name']), list(df['{}年'.format(i)])) if
                      city.get(i, None)],
                     "world")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各国人均GDP".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=80),
            )
        )
        tl.add(c, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           result=df.values.tolist(),
                           a=1,
                           data_x=df.columns.values.tolist()[1:],
                           text1='''通过贫困率和贫困人口的两张地图对比可得，地图都有类似的点 两张地图颜色分布和变化趋势大致相同，
                           可以得出贫困率跟贫困人口相关。 两份数据图的中东地区数据是都偏大的随着年份的增加，变化都不是很大 我们还可以看出随着年份的增加，尽管全球总体贫困率有所下降，尤其是在中国和拉丁美洲的多数地区，
                           但非洲和部分亚洲地区的贫困率仍居高不下。
    通过各国人均GDP和贫困率的两张地图对比可得到： 人均GDP和贫困率有一定的关系，欧洲有些高收入国家贫困率的数据也不低，
    说明人均GDP与贫困率的关系不大，但是也有一定的关系。看人均GDP和贫困人口，不能全面衡量和比较国与国之间贫困率的差异贫富差距和社会保障，是决定国家贫困率的另外两个重要因素。'''
                           )


# 2010-2017各国贫困率跟贫困人口的关系
@app.route('/ren_pinkunlv')
def index_bar_every_1():
    df = pd.read_csv('./static/data/renjunGDP.csv', index_col=0)
    df1 = pd.read_csv('./static/data/pinkunlv.csv', index_col=0)
    df2 = pd.read_csv('./static/data/pinkunrenkou.csv', index_col=0)
    tl = Timeline()
    for i in range(2010, 2018):
        map0 = (
            Map()
                .add(
                "各国贫困率跟贫困人口的关系",
                [(city[i], j) for i, j in zip(list(df2.index), list(df1['{}年'.format(i)])) if city.get(i, None)],
                "world", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}各国贫困率跟贫困人口的关系".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=-1, max_=11.5),

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           result=df.values.tolist(),
                           a=1,
                           data_x=df.columns.values.tolist()[1:],
                           text1='''通过贫困率和贫困人口的两张地图对比可得，地图都有类似的点 两张地图颜色分布和变化趋势大致相同，
                           可以得出贫困率跟贫困人口相关。 两份数据图的中东地区数据是都偏大的随着年份的增加，变化都不是很大 我们还可以看出随着年份的增加，尽管全球总体贫困率有所下降，尤其是在中国和拉丁美洲的多数地区，
                           但非洲和部分亚洲地区的贫困率仍居高不下。
    通过各国人均GDP和贫困率的两张地图对比可得到： 人均GDP和贫困率有一定的关系，欧洲有些高收入国家贫困率的数据也不低，说明人均GDP与贫困率的关系不大，但是也有一定的关系。看人均GDP和贫困人口，不能全面衡量和比较国与国之间贫困率的差异贫富差距和社会保障
    ，是决定国家贫困率的另外两个重要因素。'''
                           )


@app.route('/')
def index_bar_every_2():
    c = (
        Line()
            .add_xaxis(['2017年', '2016年', '2015年', '2014年', '2013年', '2012年', '2011年'][::-1])
            .add_yaxis(
            "世界", [25.5, 20.7, 18.2, 15.7, 13.7, 12.8, 11.2], areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
        )

            .set_global_opts(title_opts=opts.TitleOpts(title="世界贫困率"))
    )
    return render_template('index.html',
                           myechart=c.render_embed(),
                           text1='''通过贫困率和贫困人口的两张地图对比可得，地图都有类似的点 两张地图颜色分布和变化趋势大致相同，
                           可以得出贫困率跟贫困人口相关。 两份数据图的中东地区数据是都偏大的随着年份的增加，变化都不是很大 我们还可以看出随着年
                           份的增加，尽管全球总体贫困率有所下降，尤其是在中国和拉丁美洲的多数地区，但非洲和部分亚洲地区的贫困率仍居高不下。
通过各国人均GDP和贫困率的两张地图对比可得到： 人均GDP和贫困率有一定的关系，欧洲有些高收入国家贫困率的数据也不低，说明人均GDP与贫困率的关系不大，
但是也有一定的关系。看人均GDP和贫困人口，不能全面衡量和比较国与国之间贫困率的差异贫富差距和社会保障，是决定国家贫困率的另外两个重要因素。'''
                           )


if __name__ == '__main__':
    app.run(debug=True)
