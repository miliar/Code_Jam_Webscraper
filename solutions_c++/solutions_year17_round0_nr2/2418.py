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
	file = fopen("1.in", "r");
	ofile = fopen("1out.txt", "w");


	fscanf(file, "%d", &Q);

	for (int i = 0; i < Q; i++) {
		char s[200];
		fscanf(file, "%s", s);
		int D = 20;
		while (D) {
			D--;
			for (int j = 0; s[j + 1] != NULL&&s[j]!=NULL; j++) {
				if (s[j] <= s[j + 1])continue;
				if (s[j] > '0') {
					s[j]--;
					for (int k = j + 1; s[k] != NULL; k++)s[k] = '9';
				}
				else {
					s[j - 1]--;
					for (int k = j; s[k] != NULL; k++)s[k] = '9';
				}
			}
		}
		long long int ans = 0;
		for(int j=0;s[j]!=NULL;j++){
			ans *= 10;
			ans += (long long int)(s[j] - '0');
		}
		fprintf(ofile, "Case #%d: %lld\n", i+1,ans);
		//cout << ans << endl;
	}
	return 0;
}
