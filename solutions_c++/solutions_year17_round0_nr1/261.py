#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int testn;
	cin>>testn;
	for (int loop = 1; loop<=testn; ++loop) {
		cout<<"Case #"<<loop<<": ";
		string S;
		int K;
		cin>>S>>K;
		int L = S.length();
		int cnt = 0;
		for (int i = 0; i+K<=L; ++i) {
			if (S[i]=='-') {
				for (int j = i; j<i+K; ++j) {
					S[j] = S[j]=='-'?'+':'-';
				}
				++cnt;
				//cout<<S<<endl;
			}
		}
		bool flag = true;
		for (int i = L-1; i>=0 && flag; --i)
			if (S[i]=='-') flag = false;
		if (flag) cout<<cnt<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
