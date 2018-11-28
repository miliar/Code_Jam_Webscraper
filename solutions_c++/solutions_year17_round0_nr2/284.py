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
	string S;
	cin >> S;
	for (int i = 1; i < S.size(); i++) {
		if (S[i] < S[i - 1]) {
			int j = i - 1;
			while (j > 0 && S[j - 1] == S[j]) j--;
			assert(S[j] > 0);
			S[j]--;
			for (int k = j; ++k < S.size(); ) {
				S[k] = '9';
			}
		}
	}

	int j = 0;
	while (j < S.size() && S[j] == '0') j++;
	S = S.substr(j);

	cout << "Case #" << tc << ": ";
	cout << S;
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
