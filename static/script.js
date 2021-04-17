$('.radio').on('click', (event) => {
    let button = event.target
    // стираем класс активности у всех кнопок этого вопроса
    $(button).parent().children('button').removeClass('is-active')
    // ставим активной последнюю нажатую
    $(button).toggleClass('is-active')
    // считываем атрибут с ответом и записываем его в скрытое поле input
    answer = $(button).attr('value')
    $(button).parent().children('.answer').val(answer)
})