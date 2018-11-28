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

int M;

int main(){
	FILE *file;
	FILE *ofile;
	file = fopen("1.in", "r");
	ofile = fopen("1out.txt", "w");


	fscanf(file, "%d", &M);
	//cin >> M;
	for (int i = 0; i < M; i++) {
		list<long long int>L;
		long long int N, K;
		fscanf(file, "%lld %lld", &N, &K);
		//cin >> N >> K;
		L.push_back(N);
		for (auto j : L) {
			if (j < 2)break;
			if (j % 2) {
				if (j / 2 < *L.rbegin())L.push_back(j / 2);
			}
			else {
				if (j / 2 < *L.rbegin())L.push_back(j / 2);
				if (j / 2 - 1 < *L.rbegin())L.push_back(j / 2 - 1);
			}
		}

		map<long long int, long long int>ma;
		ma[*L.begin()] = 1;
		for (auto j : L) {
			if (!(j / 2)) break;
			ma[j / 2] += ma[j];
			ma[(j - 1) / 2] += ma[j];
		}
		long long int box = 0;
		for (auto j : L) {
			box += ma[j];
			if (box >= K) {
				box = j;
				break;
			}
		}
		fprintf(ofile, "Case #%d: %lld %lld\n", i + 1, box / 2, (box-1) / 2);
		//cout << box / 2 << " " << (box - 1) / 2 << endl;;
	}
	return 0;
}
