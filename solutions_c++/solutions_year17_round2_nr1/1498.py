#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
typedef long long int lli;
typedef pair<lli, lli> ii;
const int MAXN = 10010, MAXL = 1000010;

int n, d;
int k, s;
double slowest, ans;

int main() {
	// freopen("A-large.in", "r", stdin);
	// freopen("output-large.txt", "w", stdout); 

	int t;
	scanf("%d", &t);

	for(int test=1; test<=t; test++) {
		printf("Case #%d: ", test);
		slowest = 0.0f;

		scanf("%d %d", &d, &n);
		for(int i=0; i<n; i++) {
			scanf("%d %d", &k, &s);

			double aux = double(d - k) / double(s);
			if(aux > slowest) {
				slowest = aux;
			}
		}

		printf("%.6lf\n", double(d)/slowest);
	}
}
