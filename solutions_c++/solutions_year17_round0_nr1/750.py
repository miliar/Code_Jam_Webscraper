#include <bits/stdc++.h>

using namespace std;
string st;
int k;
int len;

inline int calc(){
	int sum = 0;
	int l = 0;
	for (int i = 0; i <= len - k; i++){
		if (st[i] == '+')
			continue;
		++sum;
		for (int j = i; j < i + k; j++)
			if (st[j] == '-')
				st[j] = '+';
			else
				st[j] = '-';
	}
	for (int i = len - k + 1; i < len; i++)
		if (st[i] == '-')
			return -1;
	return sum;
}

int main(){
	// freopen("A-small-attempt0.in", "r", stdin);
	// freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	// cout << T << endl;
	char ch = getchar();
	for (int i = 0; i < T; i++){
		cin >> st >> k;
		len = st.length();
		int ans = calc();
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}