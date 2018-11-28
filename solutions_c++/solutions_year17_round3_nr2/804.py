#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <bitset>
#include <iomanip>
#include <cmath>
#include <queue>

# define M_PI           3.14159265358979323846

using namespace std;

typedef long long ll;
typedef pair<string, int> si;
typedef pair<int, int> ii;

const int CMAX = 1e5+10;
const double eps = 1e-7;



int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		
		int ans;

		int C, J;
		cin >> C >> J;

		if ((C == 1 && J == 1) || C + J < 2) {
			ans = 2;
			for (int j = 0; j < (C + J)*2; j++) {
				int x;
				cin >> x;
			}
		}
			
		else {
			int A, B, C, D;
			int As, Ae, Bs, Be;
			cin >> A >> B >> C >> D;

			if (B > D) {
				As = C;
				Ae = D;
				Bs = A;
				Be = B;
			}
			else {
				As = A;
				Ae = B;
				Bs = C;
				Be = D;
			}

			if (Be - As > 720 && Bs - Ae < 720)
				ans = 4;
			else
				ans = 2;

		}

		cout << "Case #" << i + 1 << ": " << ans << endl;

	}

	return 0;
}