#include<iostream>
#include<map>
using namespace std;
#define LLD long long int

int main()
{
	int T;
	LLD N,K;
	map<LLD,LLD,greater<LLD> > M;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cin>>N>>K;
		M[N] = 1;
		LLD total = 0;
		LLD ans1, ans2;
		for(int j=1;j<=K;j++)
		{
			LLD val = M.begin()->first;
			LLD count = M.begin()->second;
			M.erase(val);
			ans2 = (val-1)/2;
			ans1 = val - 1 - ans2;
			total += count;
			if(total >= K)break;
			if(M.find(ans1) != M.end())M[ans1] += count;
			else M[ans1] = count;
			if(M.find(ans2) != M.end())M[ans2] += count;
			else M[ans2] = count;
		}
		cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<"\n";
		M.clear();
	}
}
		
