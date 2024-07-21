import streamlit as st

st.title('Title -> welcom to data tech') #Title
st.header('Header -> Data Tech') #header
st.subheader('Subheader -> explore all data operation') #subheader
st.text('Text -> hello, welcom in data tech. We are providing all the data analytics tools,Which can provide you better interaction with data')


st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi \n  Hi')
st.success('Data is Submitted!') #success
st.info('Information: This is the Data Analyatics wbsite') #Information
st.warning('licence is mandetory to acsses the wbsite')  # WARNING
st.error('licence no is not valid') # error

exp = ZeroDivisionError('Division is not possible with zero')
st.exception(exp) ## exception is define first than pass it to function
st.help(ZeroDivisionError)

st.write('range(1,10)') # it can work like a text fuction where we can see only text
st.write(range(1,10)) # with the help of this we can perform various operation
st.write('1+2+3')
st.write(1+2+3) # here we can perform the addtion operation

st.code('x=10\n'
         'for i in range(x):\n' #to write a coding part
             'print(i)')
st.checkbox('Male')
st.checkbox('Female')        # this show only the checkbox
if(st.checkbox('Adult')):
    st.write("You are having Adult") #checkbox with validation


radiobutton=st.radio('Select:',('Male','Female','other')) # this is for radio button and with the validation
if(radiobutton=='Male'):
    st.write("You are Male")
if(radiobutton=='Female'):
    st.write("You are Female")
if(radiobutton=='other'):
    st.write("You are other")

selectbox=st.selectbox("Data Science:",['Data Analyatics','Web Scrapping','Machsion Learning','NLP'])

st.write("You've selected ",selectbox)

multiselectbox=st.multiselect("Data Science:",['Data Analyatics','Web Scrapping','Machsion Learning','NLP'])

st.write("You've selected ",len(multiselectbox))

## button

if(st.button('Submit')):
      st.write('Your Response Submitted Successfully!')
## Slider:
vol=st.slider('Select the volume',0,100,step=1)
st.write('You have selected:',vol)

## user input:
username=st.text_input('Enter your User name')
password=st.text_input('Enter your password:',type='password')

## Text area:
textarea=st.text_area('write review in 100 words',max_chars=100)
st.write(textarea)
## to input a number
st.number_input("Select your age",18,100)

## to input a data:
st.date_input("Date of Birth")

## to input time:
st.time_input("time")
