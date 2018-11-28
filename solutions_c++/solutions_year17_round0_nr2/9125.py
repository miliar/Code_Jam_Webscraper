#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("B-large.in","r",stdin);
freopen("ee.txt","w",stdout);
long long t,found=0;
char n[60];
long long cc=0;
int i,l,j;
cin>>t;
while(t--)
{
cin>>n;
++cc;
l=strlen(n);
found=0;
for(j=0;j<l;j++)
{
found=0;
for(i=0;i<l;i++)
{

if(n[i+1]<n[i] && found==0 && i!=l-1)
{
found=1;
n[i]--;
}
else if(found==1)
n[i]='9';

}
}
long long x =atoll(n);
cout<<"Case #"<<cc<<": "<<x<<endl;

}
return 0;


}
