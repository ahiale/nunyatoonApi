"""empty message

Revision ID: 5e4e203e39ce
Revises: 4e26ea428ed9
Create Date: 2024-07-07 02:28:43.463316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e4e203e39ce'
down_revision: Union[str, None] = '4e26ea428ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parents', sa.Column('maxProfilEnfant', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parents', 'maxProfilEnfant')
    # ### end Alembic commands ###