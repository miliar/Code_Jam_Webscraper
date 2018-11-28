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
	for (int loop = 1; loop <= T; loop++) {
		int ld, ad, lk, ak, b, d;
		fscanf(file,"%d %d %d %d %d %d", &ld, &ad, &lk, &ak, &b, &d);
		//cin >> ld >> ad >> lk >> ak >> b >> d;
		int a;
		a = lk / ad + !!(lk%ad);
		if (b) {
			for (int i = 1; i <= 50; i++) {
			//	cout << (lk / (ad + b*i)) + !!(lk % (ad + b*i)) << endl;
				a = min(a, i + lk / (ad + b*i) + !!(lk % (ad + b*i)));
			}
		}
		int best = -1;
		for (int i = 0; i < 100; i++) {
			int box = i;
			int boxld = ld;
			int boxak = ak;
			int turn = 0;
			while (box) {
				if (boxld > boxak-d) {
					boxak -= d;
					box--;
				}
				else boxld = ld;
				turn++;
				boxld -= boxak;
				if (turn > 300) {
					turn = -1;
					break;
				}
			}
			
			if (turn == -1)continue;
			box = a;
			while (box>1) {
				if (boxld > boxak)box--;
				else boxld = ld;
				turn++;
				boxld -= boxak;
				if (turn > 600) {
					turn = -1;
					break;
				}
			}
			turn++;
			//cout << i << " " << turn << endl;
			if (best == -1&&turn)best = turn;
			else if(turn) best = min(best, turn);
		}
		if(best==-1)fprintf(ofile, "Case #%d: IMPOSSIBLE\n",loop);
		else fprintf(ofile, "Case #%d: %d\n", loop, best);
		//if (best == -1)cout << "Impossible\n";
		//else cout << best << endl;

	}
	


	fclose(file);
	fclose(ofile);
	return 0;
}
