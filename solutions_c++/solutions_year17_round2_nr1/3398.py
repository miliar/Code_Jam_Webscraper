#include<iostream>
using namespace std;
int main()
{
cout.setf(ios_base::showpoint);
cout.precision(15);
int a,b=1;
double c,d,e,f,g,h;
cin>>a;
while(b<=a)
{
cin>>c;
cin>>e;
h=0;
while(e)
{
cin>>f;
cin>>g;
f=c-f;
f=f/g;
if(f>h)
h=f;
--e;
}
cout<<"Case #"<<b<<": "<<(c/h)<<endl;
++b;
}
return 0;
}
