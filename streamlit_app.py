import streamlit as st

st.title('Zena\'s Amazing Athleisure Catalog')
session = st.connection('snowflake').session()
catalog_df = session.table('zenas_athleisure_db.products.catalog_for_website').to_pandas()
color_or_style_chosen = st.selectbox(
    label='Pick a sweatsuit color or style',
    options=catalog_df.index,
    index=None,
    placeholder="Select color or style...",
    format_func=lambda i: catalog_df.at[i, 'COLOR_OR_STYLE'],
    accept_new_options=False,
)
if color_or_style_chosen is not None:
    row = catalog_df.iloc[color_or_style_chosen]
    st.image(
        image=row['FILE_URL'],
        caption=f"Our warm, comfortable, {row['COLOR_OR_STYLE']} sweatsuit!",
        width=400,
    )
    st.markdown(f"**Price:** ${row['PRICE']:.2f}")
    st.markdown(f"**Sizes Available:** {row['SIZE_LIST']}")
    st.markdown(f"**Also Consider:** {row['UPSELL_PRODUCT_DESC']}")
