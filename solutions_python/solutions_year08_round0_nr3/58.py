import sys
#fF=open('input');
fF=sys.stdin;
fG=sys.stdout;
import math
def fIntegral(a,xa,xb):
  x=xa; fa=.5*x*math.sqrt(a*a-x*x)+a*a/2*math.asin(x/a);
  x=xb; fb=.5*x*math.sqrt(a*a-x*x)+a*a/2*math.asin(x/a);
  return fb-fa;
  
def fArea(x0,y0,d,R):#(x0,y0),width of rectangle : d, radius:R
  if d<=0:return 0;
  f1=x0*x0+y0*y0-R*R;
  f2=x0*x0+(y0+d)*(y0+d)-R*R;
  f3=(x0+d)*(x0+d)+(y0+d)*(y0+d)-R*R;
  f4=(x0+d)*(x0+d)+y0*y0-R*R;
  s=0;
  if f1>=0:s=0;
  elif f3<=0:s=d*d;
  elif f2<=0 and f3>=0 and f4<=0: #I
    ya=y0+d; t=ya;xa=math.sqrt(R*R-t*t);
    xb=x0+d; t=xb;yb=math.sqrt(R*R-t*t);
    s=(xa-x0)*d+fIntegral(R,xa,xb)-y0*(xb-xa);
  elif f1<=0 and f2>=0 and f3>=0 and f4<=0:#II
    xa=x0; t=xa; ya=math.sqrt(R*R-t*t);
    xb=x0+d;t=xb; yb=math.sqrt(R*R-t*t);
    s=fIntegral(R,xa,xb)-y0*(xb-xa);
  elif f2<=0 and f3>=0 and f4>=0 and f1<=0:#III
    ya=y0+d; t=ya; xa=math.sqrt(R*R-t*t);
    yb=y0; t=yb; xb=math.sqrt(R*R-t*t);
    s=(xa-x0)*d+fIntegral(R,xa,xb)-y0*(xb-xa);
  elif f1<=0 and f2>=0 and f4>=0 :#IV
    xa=x0;t=xa; ya=math.sqrt(R*R-t*t);
    yb=y0; t=yb;xb=math.sqrt(R*R-t*t);
    s=fIntegral(R,xa,xb)-y0*(xb-xa);
  return s;

x=fF.readline();N=int(x.strip());
for iN in range(1,N+1):
  x=fF.readline().split();t=[]
  for x1 in x:t.append(float(x1));
  f=t[0];R=t[1];k=t[2];r=t[3];g=t[4];
  SE=0;iX=-1;
  while 1:#for x0 in range(0,R,g+2*r):
    iX+=1;x0=iX*(g+2*r);iY=-1;
    if x0>=R:break;
    while 1:#for y0 in range(0,R,g+2*r):
      iY+=1;y0=iY*(g+2*r);
      if y0>=R:break;      
      #for rectangle start at (x0,y0)
      #escape area
      sE=fArea(x0+r+f,y0+r+f,g-2*f,R-k-f);
      SE+=sE;
  SW=math.pi*R*R/4;
  p=1-SE/SW;
  fG.write('Case #%d: %.6f\n'%(iN,p));
      
      
    
      
 
    
  
 
  
    
  
    
