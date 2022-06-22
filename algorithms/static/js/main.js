$(document).ready(function(){
    $('#submit').click(function(){
       const ben1= document.getElementById('ben1').value;
       const ben2= document.getElementById('ben2').value;
       const ben3= document.getElementById('ben3').value;
       const ben4= document.getElementById('ben4').value;
       const ben5= document.getElementById('ben5').value;
       const ben6= document.getElementById('ben6').value;
       const ben7= document.getElementById('ben7').value;
       const wei1= document.getElementById('wei1').value;

       const wei2= document.getElementById('wei2').value;
       const wei3= document.getElementById('wei3').value;

       const wei4= document.getElementById('wei4').value;
       const wei5= document.getElementById('wei5').value;

       const wei6= document.getElementById('wei6').value;
       const wei7= document.getElementById('wei7').value;
       const maximum= document.getElementById('maximum').value;
   



       $.ajax(
           {
               url: '',
               type:'get',
               data:{
                   'ben1':ben1,
                   'ben2':ben2,
                   'ben3':ben3,
                   'ben4':ben4,
                   'ben5':ben5,
                   'ben6':ben6,
                   'ben7':ben7,
                   
                   'wei1':wei1,
                   'wei2':wei2,
                   'wei3':wei3,
                   'wei4':wei4,
                   'wei5':wei5,
                   'wei6':wei6,
                   'wei7':wei7,
                   'maximum':maximum,
               },
               success: function (response){
                   $('#result').empty().append(response.result)
               }
           }
       )


    });
});