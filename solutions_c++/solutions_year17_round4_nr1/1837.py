#include<bits/stdc++.h>
using namespace std;

int N, P;
int A[110];
bool cmp2(int a, int b)
{
	return a%2 < b%2;
}
bool cmp3(int a, int b)
{
	return (3-a%3)%3 < (3-b%3)%3;
}
int main()
{
	int T; cin>>T;
	for(int tc = 1; tc<=T; tc++)
	{
		cin>>N>>P;
		for(int i = 0; i<N; i++)
		{
			cin>>A[i];
		}
		int ans = 0;
		if(P==2)
		{
			sort(A,A+N,cmp2);
			int candies = 0;
			for(int i = 0; i<N; i++)
			{
				if(candies==0) ans++;
				while(candies<A[i]) candies+=2;
				candies -= A[i];
			}
		}
		else if(P==3)
		{
			vector<int> f[3];
			for(int i = 0; i<N; i++)
			{
				f[A[i]%3].push_back(A[i]);
			}
			vector<int> S;
			for(auto&& x : f[0])
			{
				S.push_back(x);
			}
			int mode = 2;
			while(!(f[1].empty() && f[2].empty()))
			{
				if(mode == 1 && f[1].size()>0)
				{
					S.push_back(f[1].back());
					f[1].pop_back();
				}
				if(mode == 2 && f[2].size()>0)
				{
					S.push_back(f[2].back());
					f[2].pop_back();
				}
				if(mode==2) mode = 1;
				else mode = 2;
			}
			int candies = 0;
			for(int i = 0; i<N; i++)
			{
				if(candies==0) ans++;
				while(candies<S[i]) candies+=3;
				candies -= S[i];
			}
		}
		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
}
