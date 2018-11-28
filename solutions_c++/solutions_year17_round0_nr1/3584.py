#include <bits/stdc++.h>
using namespace std;
int Solve()
{
	string str;
	int K;
	cin>>str>>K;
	int ans = 0;
	//cout<<str<<K<<endl;
	int len = str.size();
	for(int i=0;i <= len - K;++i)
	{
		if(str.at(i)=='-')
		{
			ans++;
			for(int j=0; j<K  ;++j)
			{
				if(str.at(i+j)=='-')
					str.at(i+j) ='+';
				else
					str.at(i+j) = '-';
			}
		}
	}
	for(int i=0;i<len ;++i)
		if(str.at(i)=='-') return -1;
	return ans;
}
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		int K = Solve();
		if(K== - 1)
			printf("Case #%d: IMPOSSIBLE\n",i);
		else
			printf("Case #%d: %d\n",i,K);

	}
	return 0;
}