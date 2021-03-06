"""empty message

Revision ID: b3a059931312
Revises: 1847bdd36b31
Create Date: 2021-10-10 10:36:49.993253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b3a059931312"
down_revision = "1847bdd36b31"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "post", sa.Column("language", sa.String(length=5), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("post", "language")
    # ### end Alembic commands ###
