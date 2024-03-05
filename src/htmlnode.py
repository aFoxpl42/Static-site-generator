class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if len(self.props) == 0:
            return None
        for k,v  in self.props.items():
            result += f' {k}="{v}"'
        return result
    
    
    def __repr__(self) -> str:
        return f"HTML Node:\n* Tag: {self.tag}\n* Value: {self.value}\n* Children: {self.children}\n* Props: {self.props}"
    
    