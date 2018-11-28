#include<bits/stdc++.h>
using namespace std;

double pi=3.14159265;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("op.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	
	int cnt=0;
	while(T--)
	{
		cnt++;
		vector<pair<long long,long long> >V;
		
		int i;
		long long N,K;
		
		scanf("%lld%lld",&N,&K);
		
		for (i=1;i<=N;i++)
		{
			long long r,h;
			scanf("%lld%lld",&r,&h);
			V.push_back(make_pair(r,h));
		}
		
		
		sort(V.begin(),V.end());
		
		multiset<long long>S;
		
		long long best=0;
		for (i=0;i<K;i++)
		{
			long long mul=2*V[i].first*V[i].second;
			S.insert(mul);
			best+=mul;
		}
		
		long long sum=best;
		best+=V[K-1].first*V[K-1].first;
		
		for (i=K;i<N;i++)
		{
			long long mul=2*V[i].first*V[i].second;
			
			long long x=*(S.begin());
			
			S.erase(S.begin());
			
			sum-=x;
			
			best=max(best,sum+V[i].first*V[i].first+mul);
			
			if(x>mul)
			{
				sum+=x;
				S.insert(x);
			}
			
			else
			{
				sum+=mul;
				S.insert(mul);
			}
			
		}
		
		long double p=(long double)best*pi;
		cout.precision(8);
		
		cout<<"Case #"<<cnt<<": ";
		cout<<fixed<<p<<endl;
	}
}
