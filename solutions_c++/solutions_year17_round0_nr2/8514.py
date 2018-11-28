#pragma GCC optimize("O3")
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define iter(i, a, b) for(void *i = a; i != b; i++)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
#define endl '\n'
#define INF 1 << 30
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

ll check_tidy(ll &nr, int rlv) {
	rlv++;
	if (nr < 100 && nr%100 == nr%10)
		return -1;
	ll next = (ll)(nr/10);
	if (nr%10 >= next%10)
		return check_tidy(next, rlv);
	else
		return rlv;
}	

int main() {
	cin.sync_with_stdio(0);
	
	ll test_cases, number;

	cin >> test_cases;
	int t_c = test_cases;
	while(test_cases--) {
		cin >> number;
		while (true) {
			ll rv = check_tidy(number, 0);
			if(rv == -1) {
				
				cout << "Case #" << t_c-test_cases << ": " << number << endl;
				break;
			} else {
				ll tmp = number;
				number-= (ll)pow(10, rv);
				if (number == 0) {
					number = tmp - 1;
					rv--;
				}
				number = number - number%((ll)pow(10, rv)) + (ll)pow(10, rv) - 1ll;
			}
		}
		

	}
	
	return 0;
}
