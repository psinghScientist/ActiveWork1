category1=[]
x=""
if re.match(r".*((assist|troubl| issue|problem|fail|error|fallout|try[a-z\s]{0,10}activate|troubl[a-z\s]{0,10}activat|help)[a-z\s]{0,20}(activat|activat[a-z\s]{0,10}troubl|phone)|(activat|activat[a-z\s]{0,10}troubl|phone)[a-z\s]{0,20}(assist|troubl| issue|problem|fail|error|fallout|try[a-z\s]{0,10}activate|trouble[a-z\s]{0,10}activat|help)).*", x):
        category1.append("activation issue")
category1
