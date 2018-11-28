#include<bits/stdc++.h>
#define ll long long 
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("answer.txt","w",stdout);
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		ll n,ind;
		int f=0;
		cin>>n;
		for(ll i=n;i>=0;i--)
		{
			int f=0;
			stringstream ss;
			ss<<i;
			string a=ss.str();
			ll l=a.size();
			for(ll j=0;j<l-1;j++)
			{
				if(a[j+1]<a[j]){
				f=1;
				break;}
				
			}
			if(!f)
			{
				ind=i;
				break;
			}
		}
		if(!f)
		printf("Case #%d: %d\n",k,ind);
		k++;
	}
}
