#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;

bool run(int tc)
{
	int k;
	string S;
	cin >> S >> k;

	int flips = 0;
	for (int i = 0; i + k <= S.size(); i++) {
		if (S[i] == '+') continue;
		for (int j = 0; j < k; j++) {
			S[i + j] = (S[i + j] == '+') ? '-' : '+';
		}
		flips++;
	}

	bool possible = true;
	for (int i = 0; i < S.size(); i++) {
		possible &= S[i] == '+';
	}

	cout << "Case #" << tc << ": ";
	if (possible) cout << flips;
	else cout << "IMPOSSIBLE";

	cout << endl;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
