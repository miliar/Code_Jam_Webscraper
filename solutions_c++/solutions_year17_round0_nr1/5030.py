#include<bits/stdc++.h>
using namespace std;
#define SZ(a) ((int)a.size())
const int N = 1<<10;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int kase=1;kase<=T;++kase) {
		string s;
		int k;
		cin >> s >> k;
		int n=SZ(s),ans=0;
		for (int i=0;i<n-k+1;++i)
			if (s[i]=='-') {
				++ans;
				for (int j=0;j<k;++j)
					s[i+j]=s[i+j]=='+'?'-':'+';
			}
		for (int i = n-k+1;i<n;++i)
			if (s[i]=='-') {
				ans=n+87;
				break;
			}
		cout <<"Case #"<<kase<<": ";
		if (ans > n)
			cout<< "IMPOSSIBLE\n";
		else
			cout << ans << '\n';
	}
}
