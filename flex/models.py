"""Flexible Page"""

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks 


class FlexPage(Page):
    """Flexible class page."""

    template = "flex/flex_page.html"

    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBlock()),
        ("full_richtext", blocks.RichtextBlock()),
        ("simple_richtext", blocks.SimpleRichtextBlock()),
        ("cards", blocks.CardBlock()),
        ("cta", blocks.CTABlock()),
        
    ], null=True, blank=True)

    subtitle = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'), 

    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'

