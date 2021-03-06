"""Increase size of xref column

Revision ID: 54672c4d904
Revises: 3ee16503d82
Create Date: 2015-03-03 20:59:38.872362

"""

# revision identifiers, used by Alembic.
revision = '54672c4d904'
down_revision = '3ee16503d82'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('parts', 'xref',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=1024),
               existing_nullable=True)
    op.alter_column('binaries', 'xref',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=1024),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('binaries', 'xref',
               existing_type=sa.VARCHAR(length=1024),
               type_=sa.String(length=256),
               existing_nullable=True)
    op.alter_column('parts', 'xref',
               existing_type=sa.VARCHAR(length=1024),
               type_=sa.String(length=256),
               existing_nullable=True)
    ### end Alembic commands ###
