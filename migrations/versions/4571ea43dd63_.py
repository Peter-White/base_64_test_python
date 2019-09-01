"""empty message

Revision ID: 4571ea43dd63
Revises: 
Create Date: 2019-08-26 15:47:45.221174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4571ea43dd63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place_holder_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('place_holder_image')
    # ### end Alembic commands ###