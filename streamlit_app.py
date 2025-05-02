import streamlit as st
from snowflake.snowpark.functions import col


def main() -> None:
    session = st.connection('snowflake').session()
    st.title('Zena\'s Amazing Athleisure Catalog')
    catalog_df = session.table('zenas_atheleisure_db.products.catalog_for_website')
    color_or_style_chosen = st.multiselect(
        label='Pick a sweatsuit color or style',
        options=catalog_df.select(col('color_or_style')),
    )


if __name__ == '__main__':
    main()
