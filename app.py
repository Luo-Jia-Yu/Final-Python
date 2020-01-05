from flask import Flask,render_template
from pyecharts import options as opts
from pyecharts.charts import Line
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts



app = Flask(__name__)

df=pd.read_csv('cncollege.csv',index_col="Country Name")





@app.route('/')
def line1_base() -> Line:
    x轴 = [str(x) for x in df.columns.values[3:11]]
    中国 = list(df.loc["中国"].values)[3:11]
    c = (
         Line()
        .add_xaxis(x轴)
        .add_yaxis("中国",中国)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国高等院校入学率", subtitle="百分比"))
    )
    c.render("./templates/university.html")
    with open("./templates/university.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('1.html',
                               the_sym=sym,
                               )

@app.route('/1')
def line_base() -> Line:
    a = pd.read_csv('cngdp.csv', index_col="Country Name")
    x轴 = [str(x) for x in a.columns.values[3:11]]
    中国 = list(a.loc["中国"].values)[3:11]
    c = (
         Line()
        .add_xaxis(x轴)
        .add_yaxis("中国",中国)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国GDP", subtitle="现价美元"))
    )
    c.render("./templates/GDP.html")
    with open("./templates/GDP.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('5.html',
                               the_sym=sym,
                               )
@app.route('/2')
def line2_base() -> Line:
    b = pd.read_csv('cnfemalesmoke.csv', index_col="Country Name")
    x轴 = [str(x) for x in b.columns.values[4:11]]
    中国 = list(b.loc["中国"].values)[4:11]
    c = (
         Line()
        .add_xaxis(x轴)
        .add_yaxis("中国",中国)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国女性吸烟率", subtitle="百分比"))
    )
    c.render("./templates/nvxing.html")
    with open("./templates/nvxing.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('2.html',
                               the_sym=sym,
                               )

@app.route('/3')
def line3_base() -> Line:
    c = pd.read_csv('cnmalesmoke.csv', index_col="Country Name")
    x轴 = [str(x) for x in c.columns.values[4:11]]
    中国 = list(c.loc["中国"].values)[4:11]
    c = (
         Line()

        .add_xaxis(x轴)
        .add_yaxis("中国",中国)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国男性吸烟率", subtitle="百分比"))
    )
    c.render("./templates/nanxing.html")
    with open("./templates/nanxing.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('3.html',
                               the_sym=sym,
                               )

@app.route('/4')
def line() -> Line:
    df = pd.read_csv('data4.csv', index_col="指标")
    x轴 = [str(x) for x in df.columns.values[1:11]]
    二氧化硫排放量 = list(df.loc["二氧化硫排放量(吨)"].values)[1:11]
    氮氧化物排放量 = list(df.loc["氮氧化物排放量(吨)"].values)[1:11]
    烟尘排放量 = list(df.loc["烟(粉)尘排放量(吨)"].values)[1:11]
    c = (
        Line()
        .add_xaxis(x轴)
        .add_yaxis("二氧化硫排放量(吨)",二氧化硫排放量)
        .add_yaxis("氮氧化物排放量(吨)",氮氧化物排放量)
        .add_yaxis("烟(粉)尘排放量(吨)",烟尘排放量)
        .set_global_opts(title_opts=opts.TitleOpts(title="中国污染物排放量", subtitle="吨数"))
    )
    c.render("./templates/wuranwu.html")
    with open("./templates/wuranwu.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('4.html',
                               the_sym=sym,
                               )




if __name__ == '__main__':
    app.run()
