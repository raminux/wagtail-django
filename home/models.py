from django.db import models

from wagtail.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks


class HomePage(Page):
    """Home Page Model."""

    template = 'home/home_page.html'
    max_count = 1 # It means that only one Home Page can exist 
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, blank=False, null=True, related_name="+")
    # cta = Call To Action, it is an optional button 
    banner_cta = models.ForeignKey('wagtailcore.Page', on_delete=models.SET_NULL, blank=True, null=True, related_name="+")

    content = StreamField([
        ("cta", blocks.CTABlock()),
        
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'),
        StreamFieldPanel('content'), 
    ]

    class Meta: 
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'
