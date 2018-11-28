#include <bits/stdc++.h>

using namespace std;


char inv(char a)
{
	if(a == '-')return '+';
	return '-';
}

void solve() 
{
	string s;
	int k, ans = 0;
	cin >> s >> k;
	for (int i = 0; i < s.size() - k + 1; i++) {
		if(s[i] == '-') {
			ans++;
			for (int j = i; j < i + k; j++) s[j] = inv(s[j]);
		}
	}
	bool pode = true;
	//cout << s << endl;
	for (int i = 0; i < s.size(); i++) if(s[i] == '-') pode = false;
	if(pode) printf("%d\n", ans);
	else puts("IMPOSSIBLE");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int caso = 0; caso < T; caso++) {
		printf("Case #%d: ", caso + 1);
		solve();
	}
}
