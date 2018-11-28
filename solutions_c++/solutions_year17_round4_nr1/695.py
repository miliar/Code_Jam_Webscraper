#include "iostream"
#include "climits"
#include "list"
#include "queue"
#include "stack"
#include "set"
#include "functional"
#include "algorithm"
#include "math.h"
#include "utility"
#include "string"
#include "map"
#include "unordered_map"
#include "iomanip"
#include "random"

using namespace std;
const long long int MOD = 1000000007;

long long int T;



int main() {
	//ios::sync_with_stdio(false);
	FILE *file;
	FILE *ofile;
	file = fopen("1.txt", "r");
	ofile = fopen("1out.txt", "w");
	//cin >> T;
	fscanf(file, "%lld", &T);
	for (int i = 1; i <= T; i++) {
		int N, P;
		
		//cin >> N >> P;
		fscanf(file, "%d %d", &N, &P);
		vector<int>num(N);
		vector<int>mo(P);
		for (int i = 0; i < N; i++) {
			int a;
			//cin >> a;
			fscanf(file, "%d", &a);
			mo[a%P]++;
		}
		if (P == 2) {
			//cout << (mo[1] + 1) / 2 + mo[0] << endl;
			fprintf(ofile, "Case #%d: %d\n", i, (mo[1] + 1) / 2 + mo[0]);
		}
		else if (P == 3) {
			//cout << mo[0] << " " << mo[1] << " " << mo[2]<<endl;
			int ans = 0;
			ans = min(mo[2], mo[1]);
			//cout << ans << endl;
			mo[2] -= ans;
			mo[1] -= ans;
			ans += mo[1] / 3;
			mo[1] %= 3;
			ans += mo[2] / 3;
			mo[2] %= 3;
			ans += mo[0];
			if (mo[1] || mo[2])ans++;
			//cout << mo[0] << " " << mo[1] << " " << mo[2] << endl;
			//cout << ans << endl;
			fprintf(ofile, "Case #%d: %d\n", i, ans);
		}
		else {
			int ans = 0;
			ans = min(mo[1], mo[3]);
			mo[1] -= ans;
			mo[3] -= ans;
			ans += mo[2] / 2;
			mo[2] %= 2;
			if (mo[1] + mo[3] >= 2 && mo[2]) {
				if (mo[1]) {
					ans++;
					mo[1] -= 2;
					mo[2] = 0;
					ans += mo[3] / 4;
					mo[3] %= 4;
				}
				else {
					ans++;
					mo[3] -= 2;
					mo[2] = 0;
					ans += mo[1] / 4;
					mo[1] %= 4;
				}
			}
			ans += mo[0];
			if (mo[1] || mo[2] || mo[3])ans++;
			//cout << ans << endl;
			fprintf(ofile, "Case #%d: %d\n", i, ans);
		}
	}
	

	return 0;
}