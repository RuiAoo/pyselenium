# -*- coding=utf-8 -*-

def process_xpath_js(text: str):
    xpath_js = """$x = function(xpath, opt_startNode)
{
    var doc = (opt_startNode && opt_startNode.ownerDocument) || document;
    var result = doc.evaluate(xpath, opt_startNode || doc, null, XPathResult.ANY_TYPE, null);
    switch (result.resultType) {
        case XPathResult.NUMBER_TYPE:
            return result.numberValue;
        case XPathResult.STRING_TYPE:
            return result.stringValue;
        case XPathResult.BOOLEAN_TYPE:
            return result.booleanValue;
        default:
            var nodes = [];
            var node;
            while (node = result.iterateNext())
                nodes.push(node);
        return nodes;
    };
};
"""
    text = xpath_js + text
    driver.execute_script(text)
    
# 使用方法
text = """var s = $x('//*[@id="main"]/section/div[3]'); s[0].style.overflow = 'hidden';"""
process_xpath_js(text)
