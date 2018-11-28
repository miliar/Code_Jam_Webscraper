#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

string s;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> s;
		string ans;
		bool fl = 0;
		for (int i = 0; i < s.size(); i++){
			if (fl)
				ans += '9';
			else{
				bool fine = 1;
				for (int j = i+1; j < s.size(); j++){
					if (s[j] < s[i]){
						fine = 0;
						break;
					}
					if (s[j] > s[i])
						break;
				}

				if (fine)
					ans += s[i];
				else{
					ans += char(s[i] - 1);
					fl = 1;
				}
			}
		}
	
		while (ans.size() > 1 && ans[0] == '0')
			ans.erase(ans.begin());

		cout << "Case #" << w << ": " << ans << "\n";
	}
	return 0;
}
