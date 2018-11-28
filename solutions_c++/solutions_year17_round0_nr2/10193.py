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
	string s,sorted; int n,f; cin >> n; vector<string>x;
	while (n--) {
		cin >> s; f = 0; sorted = s;  sort(sorted.begin(), sorted.end());
		if (s.length() > 1) {
			char check = s[0]; int cnt = 0;
			if (s != sorted) {
				for (int i = 0; i < s.length(); i++) {
					if (s[i] == check)cnt++;
				}
				if (cnt != s.length()) {
					for (int i = 1; i < s.length(); i++) {
						if ((s[i] - '0') <= (s[i - 1] - '0')) {
							s[i - 1] = s[i - 1] - 1;
							for (int j = i; j < s.length(); j++) {
								s[j] = '9';
							}
							f = 1;
							break;
						}

					}
				}
			}
		}
		x.push_back(s);
	}
	for (int i = 0; i < x.size(); i++) {
		if (x[i][0] == '0')x[i].erase(0, 1);
		cout << "Case #" << i + 1 << ":" << " " << x[i]<<endl;
	}
	//system("pause");
	return 0;
}


