#include<bits/stdc++.h>
using namespace std;
#define sf scanf 
#define pf printf
#define ll long long int
int main()
{
ll i,j,N,p=1;
sf("%lld",&N);
while(p<=N)
{
char v[10000];
cin>>v;
int l=strlen(v);
	i=0;
	while(i<(l-1))
	{
	if(v[i]>v[i+1])
	{	
		for(j=i+1;j<l;j++)
		{
		v[j]='9';
		}
	v[i]=char(int(v[i])-1);
	i=0;
	}
	else
	i++;}
	
pf("Case #%lld: ",p);
if(v[0]=='0')
{

for(i=1;i<l;i++)
pf("%c",v[i]);	
pf("\n");
}

else
cout<<v<<endl;
p++;
}
}
