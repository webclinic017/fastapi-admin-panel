import db as db_signals


startup_callbacks = [
    db_signals.db_init,
    db_signals.patch_sqlalchemy_crud,
    db_signals.create_initial_roles,
    db_signals.create_initial_superuser,
]

shutdown_callbacks = [

]
