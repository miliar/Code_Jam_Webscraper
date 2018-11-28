#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base :: sync_with_stdio(false);cin.tie(0);
	freopen("B-large (1).in","r",stdin);
freopen("out.txt","w",stdout);
	int t,i=1;
	cin>>t;
	while(i<=t)
	{
		long long int a,k;
		cin>>k;
		a=k;
		vector<int> v;
		while(a != 0)
		{
			v.push_back(a%10);
			a=a/10;
		}
		int j,b;
		for(j=0;j<v.size()-1;j++)
		{
			b=j;
			if(v[j]<v[j+1])
			{
				v[j+1]=v[j+1]-1;
				while(b)
				{
					v[b]=9;
					b--;
				}
				v[0]=9;
			}
		}a=0;
		for(j=v.size()-1;j>=0;j--)
		{
			a=a*10+v[j];
		}
		cout<<"Case #"<<i<<": "<<a<<"\n";
		i++;
	}
	return 0;
}

