#include <bits/stdc++.h>
using namespace std;

int prefix[1005];

int getPrefix(int i){
	if(i < 0) return 0;
	else return prefix[i];
}

int main(){
	int qt;
	cin >> qt;

	string s;
	int k;
	int ans;
	for (int q = 0; q < qt; q++){
		cin >> s >> k;

		ans = 0;
		int size = s.size();
		for (int i = 0; i < size-k+1; i++){
			prefix[i] = getPrefix(i-1);
			if(((s[i]=='+')+getPrefix(i)-getPrefix(i-k))%2 == 0){
				ans++;
				prefix[i]++;
			}
		}

		for (int i = size-k+1; i < size; i++){
			prefix[i] = getPrefix(i-1);
			if(((s[i]=='+')+getPrefix(i)-getPrefix(i-k))%2 == 0){
				ans = -1;
				break;
			}
		}

		cout << "Case #" << q+1 << ": ";
		if(ans == -1) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
}