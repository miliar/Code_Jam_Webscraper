#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
vector<int> v;

int main()
{
	int t,i;
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		ll n,rem,j,flag=0,res=0;
		cin>>n;
		
		v.clear();
		while(n!=0)
		{
			rem=n%10;
			v.pb(rem);
			n=n/10;
		}
		
		
		for(j=0;j<=((int)(v.size()/2))-1;j++)
		{
			int c;
			c=v[j];
			v[j]=v[v.size()-1-j];
			v[v.size()-1-j]=c;
		}
		
		while(1)
		{
			flag=0;
			for(j=0;j<v.size()-1;j++)
			{
				if(v[j]>v[j+1])
				{
					flag=1;
					break;
				}
			}
			
			if(flag==0) break;
			
			v[j]--;
			for(int l=j+1;l<v.size();l++) v[l]=9;
			
		}
		
		for(j=0;j<v.size();j++)
		res+=v[v.size()-1-j]*pow(10,j);
		res=(ll)res;
	
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
}
