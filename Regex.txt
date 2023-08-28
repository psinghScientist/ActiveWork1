def find_cat(x):
    category = []
    if re.match(r".*((understand|go over|question|inquir|assist|explain|read|view|see|fetch)[a-z\s]{0,20}( bill)|(bill)[a-z\s]{0,20}(understand | go over | question | inquir| assist | explain | read | view | see | fetch)).*", x):
        category.append("Bill_Explanation")
    if re.match(r".*((waive|appl|told| den|give|issue|receive|get|refund|tak[a-z\s]{0,5}off|know about|courtes|return|revers|incentive credit|credit charg|credit|have|mov|offset|adjust)[a-z\s]{0,20}(fee|credit|charge|bill credit|incentive credit|adjustment|credit charge|bill|credit request|credit balanc)|(fee|credit|charge|bill credit|incentive credit|adjustment|credit charg|bill|credit request|credit balanc)[a-z\s]{0,20}(waiv|appl|told|den|give|issu|receiv|get|refund|tak[a-z\s]{0,5}off|know about|courtes|return|revers|incentive credit|credit charg|credit| hav| mov|offset|adjust)).*", x):
        category.append("Credit Request/ Get Waiver")


    return category






(assist|troubl| issue|problem|fail|error|fallout|try[a-z\s]{0,10}activate|troubl[a-z\s]{0,10}activat|help)[a-z\s]{0,20}
(activat|activat[a-z\s]{0,10}troubl|phone)|(activat|activat[a-z\s]{0,10}troubl|phone)[a-z\s]{0,20}
(assist|troubl| issue|problem|fail|error|fallout|try[a-z\s]{0,10}activate|trouble[a-z\s]{0,10}activat|help)




res=find_cat("I deny the unauthorized  charges on  the bill and want to understand the bill")