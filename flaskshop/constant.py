import enum

from flask_babel import lazy_gettext

ShipStatusKinds = enum.Enum(value="ShipStatus", names="pending delivered received")
PaymentStatusKinds = enum.Enum(
    value="PaymentStatus", names="waiting preauth confirmed rejected"
)
OrderStatusKinds = enum.Enum(
    value="OrderStatus", names="draft unfulfilled fulfilled canceled completed shipped"
)
OrderEvents = enum.Enum(
    value="OrderEvents",
    names="draft_created payment_captured payment_failed order_canceled order_delivered order_completed",
)
DiscountValueTypeKinds = enum.Enum(value="DiscountValueType", names="fixed percent")
VoucherTypeKinds = enum.Enum(
    value="VoucherType", names="product category shipping value"
)

SettingValueType = enum.Enum(
    value="SettingValueType", names="string integer float boolean select selectmultiple"
)


class Permission:
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTER = 0xFF

    PERMISSION_MAP = {
        LOGIN: ("login", lazy_gettext("Login user")),
        EDITOR: ("editor", lazy_gettext("Editor")),
        OPERATOR: ("op", lazy_gettext("Operator")),
        ADMINISTER: ("admin", lazy_gettext("Super administrator")),
    }


SiteDefaultSettings = {
    "project_title": {
        "value": "CatalogShop",
        "value_type": SettingValueType.string,
        "name": "Project title",
        "description": "The title of the project.",
    },
    "project_subtitle": {
        "value": "Магазин-каталог на основе Flask",
        "value_type": SettingValueType.string,
        "name": "Project subtitle",
        "description": "A short description of the project.",
    },
    "project_copyright": {
        "value": "Щеголев Данила 6303-020302D Доманицкий Александр 6303-020302D Орин Данил 6303-020302D",
        "value_type": SettingValueType.string,
        "name": "Project Copyright",
        "description": "Copyright notice of the Project like '&copy; FlaskShop'. ",
    },
}
