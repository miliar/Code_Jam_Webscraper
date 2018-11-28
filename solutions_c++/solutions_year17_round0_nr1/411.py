#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define endl "\n"

using namespace std;

typedef long long ll;
typedef long double ld;

int main(){
	ios::sync_with_stdio(false);
	
	int t;
	cin >> t;
	int caso = 1;
	while (t--){
		string s;
		cin >> s;
		
		int k;
		cin >> k;
		int a = 0;
		for (int i = 0; i < s.size() - k + 1; i++){
			if (s[i] == '-'){
				a++;
				for (int j = 0; j < k; j++){
					if (s[i + j] == '-') s[i + j] = '+';
					else if (s[i + j] == '+') s[i + j] = '-';
				}
			}
		}
		
		bool deu = true;
		for (int i = 0; i < s.size(); i++){
			if (s[i] != '+') deu = false;
		}
		if (!deu){
			cout << "Case #" << caso << ": " << "IMPOSSIBLE" << endl;
		}
		else cout << "Case #" << caso << ": " << a << endl; 
		caso++;
	}
	
	return 0;
}
