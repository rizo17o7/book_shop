from django.urls import path
from .views import IndexView, AboutView, BlogView, BlogDetailView, BlogLeftView, BlogNoView, CartView, \
    ContactView, CheckoutView, ErrorView, FAQView, HomeBoxView, HomeTwoView, PortfolioView, AccountView, \
    PortfolioThreeView, PortfolioDetailView, ShopGridView, ShopLeftView, ShopNoView, ShopRightView, \
    ShopListView, SingleProductView, TeamView, WishlistView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-detail/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog-left/', BlogLeftView.as_view(), name='blog-left'),
    path('blog-no/', BlogNoView.as_view(), name='blog-no'),
    path('cart/', CartView.as_view(), name='cart'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('error/', ErrorView.as_view(), name='error'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('home-box/', HomeBoxView.as_view(), name='home-box'),
    path('home-two/', HomeTwoView.as_view(), name='home-two'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('account/', AccountView.as_view(), name='account'),
    path('portfolio-three/', PortfolioThreeView.as_view(), name='portfolio-three'),
    path('portfolio-detail/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('shop-grid/', ShopGridView.as_view(), name='shop-grid'),
    path('shop-left/', ShopLeftView.as_view(), name='shop-left'),
    path('shop-no/', ShopNoView.as_view(), name='shop-no'),
    path('shop-right/', ShopRightView.as_view(), name='shop-right'),
    path('shop-list/', ShopListView.as_view(), name='shop-list'),
    path('single-product/', SingleProductView.as_view(), name='single-product'),
    path('team/', TeamView.as_view(), name='team'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
