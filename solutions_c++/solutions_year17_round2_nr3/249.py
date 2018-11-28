#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

long long dist[105][105];
int ev[105];
double sv[105];

struct node{
	long long dist;
	int pos;
	int operator<(const node &n) const{
		return dist > n.dist;
	}
};

int main(){
	int T;
	cin >> T;
	for(int tc=1; tc <= T; ++tc){
		int N, Q;


		cin >> N >> Q;
		for(int i=0; i<N; ++i){
			cin >> ev[i] >> sv[i];
		}

		for(int i=0; i<N; ++i){
			for(int j=0; j<N; ++j){
				long long D;
				cin >> D;
				if(D < 0) D=1000000000000LL;
				dist[i][j] = D;
			}
		}

		std::vector<std::vector<double>> spath(N, std::vector<double>(N, 1e100));

		for(int i=0; i<N; ++i){
			priority_queue<node> pq;
			vector<bool> vis(N, false);

			pq.push({0, i});
			while(!pq.empty()){
				auto n = pq.top();
				pq.pop();
				if(vis[n.pos]) continue;
				vis[n.pos] = true;
				double csp = n.dist / sv[i];
//				fprintf(stderr, "%d=>%d : %lf : %lld\n", i, n.pos, csp, n.dist);
				spath[i][n.pos] = min(spath[i][n.pos], csp);

				for(int j=0; j<N; ++j){
					if(vis[j]) continue;
					long long nt = dist[n.pos][j] + n.dist;
					if(nt > ev[i]) continue;
					pq.push({nt, j});

				}
			}
		}

		for(int k=0; k<N; ++k){
			for(int i=0; i<N; ++i){
				for(int j=0; j<N; ++j){
					double np = spath[i][k] + spath[k][j];
					double &cp = spath[i][j];
					if(cp > np) cp = np;
				}
			}
		}




		printf("Case #%d: ", tc);

		for(int i=0; i<Q; ++i){
			int U, V;
			cin >> U >> V;
			printf("%f", spath[U-1][V-1]);
			if(i+1 < Q) printf(" ");
		}
		printf("\n");



	}
}