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

int Q;

int main(){
	FILE *file;
	FILE *ofile;
	ofile = fopen("1out.txt", "w");
	file = fopen("1.in", "r");
	fscanf(file, "%d", &Q);
	for (int i = 0; i < Q; i++) {
		fprintf(ofile, "Case #");
		fprintf(ofile, "%d: ", i + 1);
		char s[2000];
		int L = 0;
		int ans = 0;
		fscanf(file, "%s", s);
		fscanf(file, "%d",&L);
		for (int j = 0; s[j + L - 1] != NULL; j++) {
			if (s[j] == '+')continue;
			ans++;
			for (int k = j; k < j + L; k++) {
				if (s[k] == '+')s[k] = '-';
				else s[k] = '+';
			}
		}
		bool flag = true;
		for (int j = 0; s[j] !=NULL ; j++) {
			if (s[j] == '-') {
				fprintf(ofile, "Impossible\n");
				flag = false;
				break;
			}
		}
		if (flag)fprintf(ofile, "%d\n", ans);
	}
	return 0;
}
