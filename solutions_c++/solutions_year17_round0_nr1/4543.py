#include <bits/stdc++.h>
/*
TASK: hidden
LANG: C++11
*/
using namespace std;
typedef long long ll;
typedef pair<int, int> pair2;
typedef pair<int, pair<int, int> > pair3;
typedef pair<int, pair<int, pair<int, int> > > pair4;
#define MAXN 10000
//#define INFINITY 1000000000000000L
#define mp make_pair
#define add push_back
#define remove pop

int n, tempforwards[MAXN], forwards[MAXN];
int solve(int size) {
	for (int i = 0; i < n; i++) {
		tempforwards[i] = forwards[i];
	}

	queue<int> end;
	int total = 0;
	int currentStamps = 0; //the number of stamps that have been applied to our current position
	for (int i = 0; i <= n - size; i++) {
		if ((end.front()) == i) {
			end.remove();
			currentStamps--;
		}
		//Decide whether or not we need to place a stamp at position i.
		tempforwards[i] += currentStamps;
		tempforwards[i] %= 2;
		if (!tempforwards[i]) {
			//stamp it
			currentStamps++;
			total++;
			end.push(i + size);
		}
	}

	for (int i = n - size + 1; i < n; i++) {
		if ((end.front()) == i) {
			end.remove();
			currentStamps--;
		}
		tempforwards[i] += currentStamps;
		tempforwards[i] %= 2;

		if (!tempforwards[i]) {
			return 1000000000; //didnt work cause this one is still negative
		}
	}

	return total;
}

int main() {
	//freopen("friendcross.in", "r", stdin);
	//freopen("friendcross.out", "w", stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);

	int T;
	cin >> T;

	int counter = 1;
	while (T--) {
		string s;
		cin >> s;
		n = s.length();
		for (int i = 0; i < n; i++) {
			forwards[i] = s[i] == '+';
		}

		int sz;
		cin >> sz;
		int answer = solve(sz);
		//cout << "solving " << s;
		cout << "Case #" << counter++ << ": ";
		if (answer == 1000000000) {
			cout << "IMPOSSIBLE" << '\n';
		} else {
			cout << answer << '\n';
		}
	}
}