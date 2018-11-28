#include <bits/stdc++.h>
using namespace std;

int t;
string s;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> s;
		int ok=0;
		while (!ok){
			ok=1;
			char mn='9';
			for (int i=(int)s.size()-1;i>=0;i--){
				mn=min(mn,s[i]);
				if (mn!=s[i]){
					ok=0;
					assert(s[i]-'0');
					s[i]--;
					for (int j=i+1;j<(int)s.size();j++){
						s[j]='9';
					}
					break;
				}
			}
		}
		ok=0;
		for (int i=0;i<(int)s.size();i++){
			if (s[i]!='0'){
				ok=1;
			}
			if (ok) cout << s[i];
		}
		cout << "\n";
	}
}
