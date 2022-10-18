from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class HomePage(Page):
    #Home page model
    templates = "home/home_page.html"
    max_count = 1

    #db fields
    banner_title = models.CharField(
        max_length = 100,
        blank = False, 
        null = True
        )

    banner_subtitle = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'])

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+",
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete = models.SET_NULL,
        related_name = "+",
    )


    #fields for admin pannel interface

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta')
        ]

    class Meta:
        verbose_name = "OH HELLO WORLD"
        verbose_name_plural = "PLURAL NAME"