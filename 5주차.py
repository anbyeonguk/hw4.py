def rep_char(c,n):
  print(c*n)
def draw_line_string(msg):
  nstr=len(msg)


  rep_char('-',nstr*2+4)
 
  print('hello',msg ,'welcome to seoul')
  rep_char('-', nstr*2+4)
a=input('input his/her name:')
draw_line_string(a)

