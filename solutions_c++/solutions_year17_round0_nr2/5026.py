#include<bits/stdc++.h>
using namespace std;
#define SZ(a) ((int)a.size())
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int kase=1;kase<=T;++kase) {
		string s;
		cin >> s;
		int fi=SZ(s);
		for (int i = SZ(s)-1;i>0;--i)
			if (s[i-1]>s[i]) {
				fi = i;
				--s[i-1];
			}
		for(int i=fi;i<SZ(s);++i) s[i]='9';
		if (SZ(s)>1&&s[0]=='0'){
			for (int i=0;i<SZ(s)-1;++i)
				s[i]=s[i+1];
			s.pop_back();
		}
		cout<< "Case #" << kase << ": " << s << '\n';
	}
}
