#include <iostream>
using namespace std;



string S;
int K;



int solve()
{
	int l = S.length();
	bool s[l];
	for(int i=0;i<l;i++)s[i] = (S[i]=='+' ? 1 : 0);
	int ans = 0;
	for(int i=0;i<=l-K;i++)
	{
		bool status = s[i];
		if(!status)
		{
			for(int j=i;j<i+K;j++)s[j] = !(s[j]);
			ans++;
		}
	}
	for(int i=l-K+1;i<l;i++)
	{
		bool status = s[i];
		if(!status) return -1;
	}
	return ans;
}

int main()
{
	freopen ("A.in","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++)
	{
		cerr<<"Performing Case# "<<i<<endl;
		cin>>S>>K;
		int ans = solve();
		if(ans==-1)cout<<"Case #"<<i<<": IMPOSSIBLE"<<"\n";
		else cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
}