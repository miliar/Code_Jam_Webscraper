#include<iostream>
using namespace std;
int main ()
{int num;
int x=0,y=0,z=0,w=0;
int T=0;


cin>>T;

for(int i=1; i<=T; i++)
{
cin>>num;
z= num%10;
y=(num/10)%10;
x= (num/100)%10;
w=num/1000;

if(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z)
  {cout<<"Case #"<<i<<": "<<num<<endl;}

else
{
   do{ num--;
    w=num/1000;
    z= num%10;
    y=(num/10)%10;
    x= num/100;
     }

while(!(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z));
   cout<<"Case #"<<i<<": "<<num<<endl;
}
}

return 0;
}
