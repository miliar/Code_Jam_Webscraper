#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int T;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		string st;
		int k;
		cin>>st>>k;
		int ans = 0;
		for (int i = 0; i < st.length(); i++)
			if (st[i]=='-') {
				if (i>st.length()-k) {
					cout<<"Case #"<<tt+1<<": IMPOSSIBLE"<<endl;
					ans = -1;
					break;
				}
				ans++;
				for (int j = 0; j < k; j++)
					st[i+j] = st[i+j]=='-'?'+':'-';
			}
		if (ans!=-1)
			cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;
}