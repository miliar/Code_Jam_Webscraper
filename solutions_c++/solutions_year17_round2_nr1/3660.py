#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("A-large.in","r",stdin);
   freopen("g.txt","w",stdout);
int t;
cin>>t;
   int p=0;
while(t--)
{
p++;
int n,k;
cin>>n>>k;
float min1=0;
float d;
for(int i=0;i<k;i++)
{
int p,q;
cin>>p>>q;
d=(n-p)/(float)q;
min1=max(min1,d);
//cout<<min1<<endl;
}
d=n/min1;
cout<<"Case #"<<p<<":"<<" ";
printf("%.7f",d);
cout<<endl;
}
}
