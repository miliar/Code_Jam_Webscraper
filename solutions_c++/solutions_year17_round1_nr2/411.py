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

int T;

int main(){
	FILE *file;
	FILE *ofile;
	file = fopen("1.in", "r");
	ofile = fopen("1out.txt","w");
	
	fscanf(file,"%d", &T);
	//cin >> T;
//	cout << T << endl;

	for (int loop = 0; loop < T; loop++) {
		long long int N, P;
		int ans = 0;
		long long int num[50] = {};
		long long int part[50][50] = {};
		long long int use[50] = {};
		//cin >> N >> P;
		
		fscanf(file, "%lld %lld", &N, &P);
		//cout << N << P << endl;
		for (int i = 0; i < N; i++) {
			//cin >> num[i];
			fscanf(file, "%lld", &num[i]);
		//	cout << num[i] << " ";
		}
	//	cout << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				//cin >> part[i][j];
				fscanf(file, "%lld", &part[i][j]);
				//cout << part[i][j] << " ";
			}
			//cout << endl;
			stable_sort(part[i], part[i] + P);
		}
		for (int i = 1; i <= 1000000; i++) {
			bool can = true;
			bool con = true;
			while (can || con) {
				can = true;
				for (int j = 0; j < N; j++) {
					while (part[j][use[j]] * 100 < num[j] * 90 * i) {
						use[j]++;
						if (use[j] >= P) {
							con = false;
							can = false;
							break;
						}
					}
					if (part[j][use[j]] * 100 > num[j] * 110 * i) {
						can = false;
						con = false;
					}
					if (!can&&!con)break;
				}
				if (!can)continue;
				ans++;
				for (int j = 0; j < N; j++) {
					use[j]++;
				}
			}
			bool flag = true;
			for (int j = 0; j < N; j++)if (use[j] >= P)flag = false;
			if (!flag)break;
		}
		//cout << ans << endl;
		fprintf(ofile, "Case #%d: %d\n", loop + 1, ans);
	}


	fclose(file);
	fclose(ofile);
	return 0;
}
