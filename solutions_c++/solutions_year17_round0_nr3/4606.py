#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
ll i,j,n,k,t,top,mid;
cin>>t;
for(i=0;i<t;i++)
{
ll a[2];
priority_queue<ll>pq;
cin>>n>>k;
pq.push(n);
for(j=0;j<k;j++)
{
top=pq.top();
pq.pop();
if(top%2==0)
{
pq.push(top/2);
pq.push((top/2)-1);
a[0]=top/2;
a[1]=(top/2)-1;
}
else
{
pq.push(top/2);
pq.push(top/2);
a[0]=top/2;
a[1]=top/2;
}
}
cout<<"Case #"<<i+1<<": "<<a[0]<<" "<<a[1]<<endl;
}
return 0;
}
