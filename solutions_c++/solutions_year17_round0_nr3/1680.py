#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	int T; cin>>T;
	ll N,K;
	for (int t=1;t<=T;t++)
	{
		cin>>N>>K;
		while (K>1)
		{
			N=(K&1?N/2-!(N&1):N/2);
			K/=2;
		}
		cout<<"Case #"<<t<<": "<<N/2<<" "<<N/2-!(N&1)<<endl;
	}
}