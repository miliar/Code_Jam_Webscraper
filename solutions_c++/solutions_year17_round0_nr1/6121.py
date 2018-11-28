#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <limits>
#include <stdarg.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef set<int> si;
typedef set<ii> sii;
typedef map<int,int> mii;

double EPS = 1e-9;
double PI = acos(-1);
const bool VUPRINT = true;

const int _r[8] = { 0, 0,-1, 1, 1, 1, -1, -1};
const int _c[8] = { 1,-1, 0, 0, 1, -1, 1, -1};

int INF = numeric_limits<int>::max();
LL LL_INF = numeric_limits<LL>::max();

void pr(const char *fmt, ...) {
    if (VUPRINT) {
    	va_list args;
	    va_start(args, fmt);
	    vprintf(fmt, args);
	    va_end(args);	
    }
}






// int grid[3][3];
// void printGrid(){
// 	if (!pr) return;

// 	int maxR = 3;
// 	int maxC = 3;

// 	for (int i=0;i<maxR;i++) {
// 		for (int j=0;j<maxC;j++){
// 			pr("%5d", grid[i][j]);
// 		}
// 		pr("\n");
// 	}
// 	pr("\n");
// }

int main() {
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);

	int T,cases,K,result;
	// int W[120], array[1000];

	char row[1100];
	bool up[1100];
	// memset(array, 0, sizeof array);
	// memset(grid, 0, sizeof grid);

	scanf("%d ", &T);
	for (cases=1;cases<=T;cases++){
		scanf("%s", row);
		scanf(" %d", &K);
		memset(up, 0, sizeof up);

		for (int i=0;i<strlen(row);i++){
			up[i] = row[i]=='+';
		}

		bool can = true;
		int result = 0;
		int inde = 0;
		while (true){
			if (inde == strlen(row)){
				break;
			}
			if (!up[inde]) {
				//Flip from up[inde] to up[inde+K-1]
				if (inde+K > strlen(row)){
					can = false;
					break;
				}
				result++;
				for (int i=inde; i<inde+K; i++){
					up[i] = !up[i];
				}
			}
			inde++;
		}

		if (can) printf("Case #%d: %d\n",cases,result);
		else printf("Case #%d: IMPOSSIBLE\n",cases);

	}

}
