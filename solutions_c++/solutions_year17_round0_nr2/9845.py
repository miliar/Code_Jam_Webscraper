#include<iostream>
using namespace std;
int main()
{
int t,n,p;
cin>>t;
for(int i=0;i<t;i++)
{
cin>>n;
while(n)
{
p=0;
for(int d=n,c=d/10;c;d/=10,c/=10)
{
if(c%10>d%10){p=1;break;}
}
if(p==1)n--;
else break;
}
cout<<"Case #"<<i+1<<": "<<n<<endl;
}
return 0;
}
