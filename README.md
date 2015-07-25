# Pelican-Chard

pelican-chard是fork自 [greizgh/pelican-material](https://github.com/greizgh/pelican-material)的 [pelican](http://blog.getpelican.com/) 主题。进行了一定的修改来服务于我的个人blog:[SilverChard](http://silverchard.me)。

pelican-chard is a theme of pelican. Fork from pelican-material.Server for my personal blog [SilverChard](http://silverchard.me).


pelican-material/pelican-chard是基于[Materialize](http://materializecss.com/)的。所以需要安装Materialize才可以使用。Materialize是一款基于Google的Material设计规范的CSS/JS框架。可以使网站富有Material风格。
Material is a [pelican](http://blog.getpelican.com/) theme based on [Materialize](http://materializecss.com/), a material design framework.

## 安装与调试 / Setup & Configuration

**以下安装与调试说明将会基于CentOS7。其他操作系统可以适当根据自己的情况进行调整。**

安装该主题
```bash
#下载并安装该主题包（请确保已经安装pelican）
cd ~
git clone https://github.com/SilverChard/pelican-chard.git
pelican-themes -i pelican-chard

```
进入你的pelican-quickstart文件夹，修改pelicanconf.py文件，启用该主题。
```bash
cd /path/to/pelican-quickstart
vim pelicanconf.py
```
写入
```python
THEME = 'pelican-chard'
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order
```
安装Materizlize
```bash
make html
cd output/theme
bower install Materialize --allow-root
cd ../../
make html
```


## License

MIT
