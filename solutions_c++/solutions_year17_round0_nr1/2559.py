#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

void solve() {
	char S[10001];
	int K;
	scanf("%s %d\n", S, &K);
	//cout << S;
	//cin >> K;

	int s = strlen(S), c=0, i=0;

	while(i < s-K) {
		if (S[i] == '+') i++;
		else {
			for(int j=i;j<i+K;j++) S[j] = (S[j] == '+') ? '-':'+';
			c++;
		}
	}

	if (S[i] == '-') {
		for(int j=i;j<i+K;j++) S[j] = (S[j] == '+') ? '-':'+';
		c++;
	}

	bool f = true;
	while (i < s) {
		if (S[i] == '-') {
			f = false;
			break;
		} else i++;
	}

	if (f) cout << c;
	else cout << "IMPOSSIBLE";
}

int main() {
	freopen("0Q/A-large.in", "r", stdin);
	freopen("0Q/out.txt","w", stdout);

	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}

