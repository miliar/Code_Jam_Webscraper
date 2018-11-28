#include <iostream>
#include <cstring>

#define MAXN 110

using namespace std;

void solve(char nu[]) {
	int len = strlen(nu);
	int head[MAXN];
	head[0] = 0;
	for (int i = 1; i < len; i++) {
		if (nu[i] == nu[i - 1]) {
			head[i] = head[i - 1];
		} else {
			head[i] = i;
		}
		if (nu[i] < nu[i - 1]) {
			nu[head[i - 1]]--;
			for (int j = head[i - 1] + 1; j < len; j++) {
				nu[j] = '9';
			}
			if (nu[0] == '0') {
				strcpy(nu, nu + 1);
			}
			return ;
		}
	}

}

int main() {
	int T, I;
	char nu[MAXN];
	cin >> T;

	for (I = 1; I <= T; I++) {
		scanf("%s", nu);
		solve(nu);
		cout << "Case #" << I << ": " << nu << endl;
	}

	return 0;
}

