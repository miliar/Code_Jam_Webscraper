#include <bits/stdc++.h>
using namespace std;
int main() 
{int t,o;cin>>t;o=t;
while(t--)
{
long long k,c;
cin>>k;
c=k;
vector <int> r;
while(c!=0)
{
int j=c%10;
r.push_back(j);
c=c/10;
}
for(int i=0;i<r.size();i++)
{
if(r[i]<r[i+1]&&r.size()>1)
{
r[i]=9;r[i+1]=r[i+1]-1;
for(int j=0;j<i;j++)
{
r[j]=9;	
}

}
}
long long ans=0;
for(int i=0;i<r.size();i++)
{
ans+=(pow(10,i)*r[i]);
}
cout<<"Case #" <<o-t<<": " <<ans<<endl;    
}
	
}
