#include "iostream"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "string"
#include "vector"
using namespace std;
void maloosh_lazma() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
}
int main() {
	maloosh_lazma();
	int n, k, cnt, y,f=0; cin >> n; vector<string>x;
	string s,v,comp;
	while (n--) {
		cnt = 0; f = 0; comp = "";
		cin >> s; 	cin >> k; for (int i = 0; i < s.length(); i++)comp += '+';
		for( y=0;y<10000;y++){
			for (int i = 0; i < s.length(); i++) {
				if (s[i] == '-'&&i + k <= s.length()) {
					for (int j = i; j < i + k; j++) {
						if (s[j] == '+')s[j] = '-'; else s[j] = '+';
					}
					cnt++;
				}
				if (s == comp) { f = 1; break;}
			}
			if (f == 1)break;
		}
		if (y == 10000)x.push_back("IMPOSSIBLE"); else x.push_back(to_string(cnt));
	}
	for (int i = 0; i < x.size(); i++)cout << "Case #" << i << ":" << " " << x[i]<<endl;
	//system("pause");
	return 0;
}


