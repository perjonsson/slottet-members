"""empty message

Revision ID: 2a95a9014f4e
Revises: None
Create Date: 2015-04-01 12:22:39.287069

"""

# revision identifiers, used by Alembic.
revision = '2a95a9014f4e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('facebook_user_id', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pwd_hash', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('permalink', sa.String(), nullable=True),
    sa.Column('company_name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('website', sa.Text(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('twitter_handle', sa.String(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permalink')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    ### end Alembic commands ###
