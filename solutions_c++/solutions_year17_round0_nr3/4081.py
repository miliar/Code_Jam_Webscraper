#include <bits/stdc++.h>
using namespace std;
int T,N,K,last1,last2;
int main()
{
	ifstream cin("C-small-2-attempt0.in");
	ofstream cout("C-small-2-attempt0.out");
	cin>>T;
	for(int cases=1; cases<=T; cases++)
	{
		cin>>N>>K;
		multiset <int> S;
		S.insert(N);
		
		for(int i=1; i<=K; i++)
		{
			int y=*(S.rbegin());
			S.erase(--S.end());
			int last1=(int)floor((y-1)*1.0/2);
			int last2=(int)ceil((y-1)*1.0/2);
			S.insert(last1);
			S.insert(last2);
			if(i==K)
			{
				cout<<"Case #"<<cases<<": "<<last2<<" "<<last1<<endl;
			}
		}
	}
	return 0;
}
