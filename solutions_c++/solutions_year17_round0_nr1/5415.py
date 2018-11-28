#include<iostream>
#include <cstring>
using namespace std;
int main()
{
int t;
cin>>t;
for(int k=0;k<t;k++)
{
cout<<"Case #"<<k+1<<": ";
int n,i,j,m,count=0;
char a[1000];
cin>>a>>n;
m=strlen(a);
for(i=0;i<m-n+1;i++)
{
if(a[i]==45)
{count++;
for(j=0;j<n;j++)
if(a[i+j]==45)
a[i+j]=43;
else
a[i+j]=45;
}
}
while(i<m)
{
if(a[i]==45)
{
n=-1;cout<<"IMPOSSIBLE\n";break;
}
i++;
}
if(n!=-1)
cout<<count<<endl;
}
return 0;
}
