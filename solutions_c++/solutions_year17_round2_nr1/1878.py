#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int t;

int main() {
	fscanf(in,"%d", &t);
	for (int tc = 0; tc < t;tc++){
		int N, D;
		fscanf(in, "%d %d", &D, &N);
		vector<int > s(N), k(N);
		for (int i = 0; i < N; i++) {
			fscanf(in, "%d %d", &k[i], &s[i]);
		}
		vector<pair<double, int>> g;
		for (int i = 0; i < N; i++) {
			g.push_back(make_pair((double)(D-k[i]) / (double)s[i], i));
		}
		int ind = 0;
		double max=0;
		sort(g.begin(), g.end());
		
		fprintf(out,"Case #%d: %.6lf\n", tc + 1, D/g[N-1].first);
	}
	return 0;
}