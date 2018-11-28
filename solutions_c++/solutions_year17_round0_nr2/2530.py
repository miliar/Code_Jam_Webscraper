#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

void solve() {
	char N[19];
	scanf("%s\n", N);
	int d = strlen(N);

	bool t = true;
	int i = 0;
	for (int j = 1; j < d; j++) {
		if (N[j] > N[i])
			i = j;
		else if (N[i] > N[j]) {
			t = false;
			break;
		}
	}

	if (t)
		printf("%s", N);
	else {
		if (N[i] == '1') {
			for (int x = 1; x <= d - 1; x++)
				printf("9");
		} else {
			N[i]--;
			for (int x = i + 1; x <= d - 1; x++)
				N[x] = '9';
			printf("%s", N);
		}
	}
}

int main() {
	//freopen("0Q/in.txt", "r", stdin);
	//freopen("0Q/B-small-attempt0.in", "r", stdin);
	freopen("0Q/B-large.in", "r", stdin);
	freopen("0Q/out.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
}
