/* --------------------------------- PK app --------------------------------- */

// copies element text to the clipboard
$("button[copy-button]").click(function() {
  $(this).text('✓');
  var temp=$('<input>');
  $('body').append(temp);
  temp.val($("[copy-source='"+$(this).attr('copy-button')+"']").text()).select();
  document.execCommand('copy');
  temp.remove();
});