#include<fstream>
#define ull unsigned long long 
std::ifstream cin("sample5.in");
std::ofstream cout("output5.out");
using namespace std;
int main()
{int t,s;
cin>>t;
for(s=1;s<=t;s++)
{ull n,p,num=0;
int r,i,j,k,c=0;
int a[19];
cin>>n;
p=n;
i=0;
while(n>0)
{r=n%10;
n=n/10;
a[i]=r;
i++;}
k=i-1;
if(k==0)
    c=1;
for(i=0;i<k;i++)
{if(a[i]>=a[i+1])
{c=1;
continue;
}
else
    {c=0;
break;}
}
if(c==0)
{
for(i=k;i>0;i--)
{ 
if(a[i]>a[i-1])
{ for(j=0;j<i;j++)
a[j]=0;

goto z;}
else if(a[i]==a[i-1])
{
if(a[i-2]<=a[i])
{for(j=0;j<i;j++)
{
a[j]=0;
}
goto z;}
else
continue;
}
}

z:for(i=k;i>=0;i--)
{
num=(num*10)+a[i];}

cout<<"Case #"<<s<<":"<<" "<<num-1<<endl;
}
else
    cout<<"Case #"<<s<<":"<<" "<<p<<endl;
}
return 0;
}
