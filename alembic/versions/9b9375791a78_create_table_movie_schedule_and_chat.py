"""create table movie schedule and chat

Revision ID: 9b9375791a78
Revises:
Create Date: 2019-01-17 01:04:02.834985

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9b9375791a78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'chat',
        sa.Column('telegram_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('telegram_id')
    )
    op.create_table(
        'movie',
        sa.Column('kofa_id', sa.String(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('director', sa.String(), nullable=True),
        sa.Column('synopsis', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('runtime', sa.Interval(), nullable=True),
        sa.PrimaryKeyConstraint('kofa_id')
    )
    op.create_table(
        'schedule',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('movie_kofa_id', sa.String(), nullable=True),
        sa.Column('start_time', sa.Time(), nullable=True),
        sa.Column('is_bookable', sa.Boolean(), nullable=True),
        sa.Column('is_delivered', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['movie_kofa_id'], ['movie.kofa_id']),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    op.drop_table('movie')
    op.drop_table('chat')
    # ### end Alembic commands ###
