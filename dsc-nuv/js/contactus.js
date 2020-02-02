 $(document).ready(function(){
          $.fn.serializeObject = function()
              {
               var o = {};
               var a = this.serializeArray();
               $.each(a, function() {
                   if (o[this.name]) {
                       if (!o[this.name].push) {
                           o[this.name] = [o[this.name]];
                       }
                       o[this.name].push(this.value || '');
                   } else {
                       o[this.name] = this.value || '';
                   }
               });
               return o;
              };
            var form = $('form#dsc-form'),
              url = 'https://script.google.com/macros/s/AKfycbwZDy1l54PwRoMsMnEGRkB1lVWbN4EFGLc0BpqhDYRmHGfvEBG-/exec';
              form.submit(function(e){
                e.preventDefault();
              var jqxhr = $.ajax({
                url: url,
                method: "GET",
                dataType: "json",
                data: form.serializeObject()
              });
                $(".form-control").remove();
                $(".contact_input_area").remove();
                $("#submit").remove();
                element = document.querySelector('.form-sent'); 
                element.style.visibility = 'visible'; 
              });
            });