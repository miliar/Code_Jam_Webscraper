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
	for (int i = 0; i < T; i++) {
		int R = 0, C = 0;
		char cake[27][27]= {};
		fscanf(file, "%d %d", &R, &C);
		//cin >> R >> C;
		for (int j = 0; j < R; j++) {
			fscanf(file, "%s", cake[j]);
			//cin >> cake[j];
		}
		bool flag[26] = {};
		int sq[26][4] = {};
		for (int k = 0; k < R; k++) {
			for (int l = 0; l < C; l++) {
				int box = (int)(cake[k][l] - 'A');
				if (!flag[box]) {
					sq[box][0] = l;
					sq[box][1] = k;
					sq[box][2] = l;
					sq[box][3] = k;
					flag[box] = true;
				}
				else {
					sq[box][0] = min(sq[box][0], l);
					sq[box][1] = min(sq[box][1], k);
					sq[box][2] = max(sq[box][2], l);
					sq[box][3] = max(sq[box][3], k);
				}
			}
		}
		for (int j = 0; j < 26; j++) {
			if (!flag[j])continue;
			for (int k = sq[j][1]; k <= sq[j][3]; k++) {
				for (int l = sq[j][0]; l <= sq[j][2]; l++) {
					cake[k][l] = (char)('A' + j);
				}
			}
		}
		for (int j = 0; j < 26; j++) {
			if (!flag[j])continue;
			bool can = true;
			while (can) {
				for (int k = sq[j][0]; k <= sq[j][2]; k++) {
					if (cake[sq[j][3] + 1][k] != '?')can = false;
				}
				if (!can)continue;
				sq[j][3]++;
				for (int k = sq[j][0]; k <= sq[j][2]; k++) {
					cake[sq[j][3]][k] = (char)('A' + j);
				}
			}
		}
		for (int j = 0; j < 26; j++) {
			if (!flag[j])continue;
			bool can = true;
			while (can) {
				if (sq[j][1] == 0)break;
				for (int k = sq[j][0]; k <= sq[j][2]; k++) {
					if (cake[sq[j][1] - 1][k] != '?')can = false;
				}
				if (!can)continue;
				sq[j][1]--;
				for (int k = sq[j][0]; k <= sq[j][2]; k++) {
					cake[sq[j][1]][k] = (char)('A' + j);
				}
			}
		}
		for (int j = 0; j < 26; j++) {
			if (!flag[j])continue;
			bool can = true;
			while (can) {
				for (int k = sq[j][1]; k <= sq[j][3]; k++) {
					if (cake[k][sq[j][2]+1] != '?')can = false;
				}
				if (!can)continue;
				sq[j][2]++;
				for (int k = sq[j][1]; k <= sq[j][3]; k++) {
					cake[k][sq[j][2]] = (char)('A' + j);
				}
			}
		}
		for (int j = 0; j < 26; j++) {
			if (!flag[j])continue;
			bool can = true;
			while (can) {
				if (sq[j][0] == 0)break;
				for (int k = sq[j][1]; k <= sq[j][3]; k++) {
					if (cake[k][sq[j][0]-1] != '?')can = false;
				}
				if (!can)continue;
				sq[j][0]--;
				for (int k = sq[j][1]; k <= sq[j][3]; k++) {
					cake[k][sq[j][0]] = (char)('A' + j);
				}
			}
		}
		fprintf(ofile, "Case #%d:\n", i + 1);
		for (int j = 0; j < R; j++) {
		//	cout << cake[j] << endl;
			fprintf(ofile, "%s\n", cake[j]);
		}
	}
	fclose(file);
	fclose(ofile);
	return 0;
}
