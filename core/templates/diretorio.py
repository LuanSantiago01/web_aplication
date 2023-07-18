import os
print(os.path.dirname(os.path.realpath(__file__)))

""""
        <picture class="my-picture" >
            <img src="{% img_url produto.picture ratio="3/2" file_type="webp" width=800 %}" alt="produto picture">
                <source type="image/webp"
                    srcset="/Users/Luan Santiago/PycharProjects/django2/produto/image/800w.webp 800w, /Users/Luan Santiago/PycharProjects/django2/produto/image/100w.webp 100w, /Users/Luan Santiago/PycharProjects/django2/produto/image/200w.webp 200w, /Users/Luan Santiago/PychaProjects/django2/produto/image/300w.webp 300w, /Users/Luan Santiago/PycharmProjects/django2/produto/image/400w.webp 400w, /Users/Luan Santiago/PycharmProjects/django2/produto/image/500w.webp 500w, /Users/Luan Santiago/PycharmProjects/django2/produto/image/600w.webp 600w, /Users/Luan Santiago/PycharmProjects/django2/produto/image/700w.webp 700w"
                    sizes="(min-width: 0px) and (max-width: 991px) 100vw, (min-width: 992px) and (max-width: 1199px) 33vw, 600px">
            <img src="/Users/Luan Santiago/PycharProjects/produto/image.jpg" alt="Spiderman" width="800" height="800" loading="lazy">
        </picture>
        
        {% load pictures %}
        {% picture produto.picture img_alt="Spiderman" ratio="16/9" m=6 l=4 %}
"""