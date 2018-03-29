import rules
import guardian

@rules.predicate
def is_item_owner(user, item):
    return item.created_by == user

@rules.predicate
def has_model_level_permission(user):
    return user.has_perm('app.change_item')

@rules.predicate
def has_object_level_permission(user, item):
    return user.has_perm('app.change_item', item)

rules.add_perm('app.rules_change_item', is_item_owner |
                                    has_model_level_permission |
                                    has_object_level_permission )

