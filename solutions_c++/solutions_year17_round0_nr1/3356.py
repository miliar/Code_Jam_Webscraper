#include <bits/stdc++.h>
using namespace std;

int t,k;
string s;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ": ";
		cin >> s >> k;
		int ok=0,ans=0;
		while (!ok){
			ok=1;
			int pos=-1;
			for (int i=0;i<(int)s.size();i++){
				if (s[i]=='-'){
					ok=0;
					pos=i;
					break;
				}
			}
			if (!ok){
				if (pos+k-1<(int)s.size()){
					for (int i=0;i<k;i++){
						if (s[pos+i]=='+'){
							s[pos+i]='-';
						}else{
							assert(s[pos+i]=='-');
							s[pos+i]='+';
						}
					}
					ans++;
				}else{
					break;
				}
			}
		}
		if (ok){
			cout << ans << "\n";
		}else{
			cout << "IMPOSSIBLE\n";
		}
	}
}
