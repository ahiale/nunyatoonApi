"""empty message

Revision ID: 4ee61522804d
Revises: 5e4e203e39ce
Create Date: 2024-07-07 02:53:00.241394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4ee61522804d'
down_revision: Union[str, None] = '5e4e203e39ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enfants', 'joursA')
    op.drop_column('enfants', 'allocation')
    op.drop_column('enfants', 'heuresA')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enfants', sa.Column('heuresA', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.add_column('enfants', sa.Column('allocation', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('enfants', sa.Column('joursA', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
