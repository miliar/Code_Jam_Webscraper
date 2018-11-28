#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

long long lower_power_2(long long n)

{
	long long ans=1;
	while(ans *4<=n)
	{
		ans*=2;
	}
	return ans;

}	

pair<long long,long long> solve(long long n,long long k,const pair<long long,long long > & parent)
{

	if(k ==1)
	{
		return make_pair((parent.first)/2,(parent.first -1 )/2);
	}
	else 
	{
		
		long long lp=lower_power_2(k);
		if ( k<lp*3)
		{
			pair<long,long> x=solve(n,k-lp,parent);
		//cout<<x.first<<","<<x.second<<endl;
		return make_pair(x.first/2,(x.first-1)/2);
		}
		else{
		
		pair<long,long> x=solve(n,k-lp*2,parent);
		return make_pair(x.second/2,(x.second-1)/2);
		}
	}
}	

int main()
{
	
	int n;
	cin>>n;
	for (int t=1;t<=n;t++)
	{
		long long n,k;
		cin>>n>>k;
			

				cout<<"Case #"<<t<<": ";
				//	if(k > (n+1)/2)
				//		cout<<"0 0"<<endl;
				//	else
					{
						pair<long long, long long> x = solve(n,k,make_pair(n,n));
						cout<<x.first<<" "<<x.second<<endl;
					}
		
	}
	return 0;
}
