#include<iostream>
using namespace std;
int main ()
{int N;
int x=0,y=0,z=0,w=0;
int T=0;


cin>>T;

for(int i=1; i<=T; i++)
{
cin>>N;
z= N%10;
y=(N/10)%10;
x= (N/100)%10;
w=N/1000;

if(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z)
  {cout<<"Case #"<<i<<": "<<N<<endl;}

else
{
   do{ N--;
    w=N/1000;
    z= N%10;
    y=(N/10)%10;
    x= N/100;
     }

while(!(w<=x&&w<=y&&w<=z&&x<=y&&x<=z&&y<=z));
   cout<<"Case #"<<i<<": "<<N<<endl;
}
}

return 0;
}
