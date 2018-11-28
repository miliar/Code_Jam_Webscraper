#include<iostream>
using namespace std;
int main ()
{int Num;
int x=0,y=0,z=0,w=0;
int T=0;


cin>>T;

for(int i=1; i<=T; i++)
{
cin>>Num;
z= Num%10;
y=(Num/10)%10;
x= (Num/100)%10;
w=Num/1000;

if(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z)
  {cout<<"Case #"<<i<<": "<<Num<<endl;}

else
{
   do{ Num--;
    w=Num/1000;
    z= Num%10;
    y=(Num/10)%10;
    x= Num/100;
     }

while(!(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z));
   cout<<"Case #"<<i<<": "<<Num<<endl;
}
}

return 0;
}
