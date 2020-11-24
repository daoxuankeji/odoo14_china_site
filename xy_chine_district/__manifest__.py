# -*- coding: utf-8 -*-
#################################################################################
# Author      : 湖南道玄社文化传媒有限公司 (<https://siiyi.cn/>)
# Copyright(c): 2020-至今，湖南道玄社文化传媒有限公司
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://siiyi.cn/license.html/>
#################################################################################

{
  "name"                 :  "odoo地址中国化设置",
  "summary"              :  "将odoo客户地址、产品发货地址等设置成符合中国思维，国-省-市=县区-乡镇-村",
  "category"             :  "Uncategorized",
  "license"              : 'LGPL-3',
  "version"              :  "0.1",
  #"sequence"             :  1,
  "author"               :  "湖南道玄社文化传媒有限公司",
  "license"              :  "Other proprietary",
  "website"              :  "https://www.siiyi.cn/",
  "ipone"                :"14789891183",
  "description"          :  """将odoo地址中国话设置.""",
  "live_test_url"        :  "",
  "depends"              :  ['base'],
  "data"                 :  [
                            'security/ir.model.access.csv',
                            'views/templates.xml',
                            'views/views.xml',
                            ],
  # only loaded in demonstration mode
  "demo"                 :  [
                            'demo/demo.xml',
                            ],
  "images"               :  [
                            'static/images/main_screenshot.png'
                            'static/description/icon.png'
                            ],
  #"application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  #"pre_init_hook"        :  "pre_init_check",
  #"external_dependencies":  {'python': ['urllib']},
}
