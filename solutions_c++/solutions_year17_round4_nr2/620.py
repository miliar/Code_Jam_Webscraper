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
		int N, M, C;
		//cin >> N >> M >> C;
		fscanf(file, "%d %d %d", &N, &M, &C);
		int people[1001] = {};
		int place[1001] = {};
		int sum[1001] = {};
		for (int j = 0; j < C; j++) {
			int a, b;
			fscanf(file, "%d %d", &a, &b);
			//cin >> a >> b;
			place[a]++;
			people[b]++;
		}
		int ride = 0;
		for (int j = 1; j < 1001; j++)ride = max(ride, people[j]);
		for (int j = 1; j < 1001; j++) {
			sum[j] = sum[j - 1] + place[j];
			ride = max(ride, (sum[j] + j - 1) / j);
		}
		int pro = 0;
		for (int j = 1; j < 1001; j++) {
			pro += max(0, place[j] - ride);
		}
		//Case #1: 1 1
		fprintf(ofile, "Case #%d: %d %d\n", i, ride, pro);
		//cout << ride << " " << pro << endl;
	}

	return 0;
}