#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <climits>
#include <set>
#include <cmath>
#define ll long long

using namespace std;

struct aa {
    int x, y;
    bool operator < (const aa &b) {
        if (x != b.x) return x < b.x;
        return y < b.y;
    }
};

bool cmp(int a, int b) {return a > b;}

int main() {
	bool debug = false;
	int T;
	cin >> T;
	for (int nm=1;nm<=T;nm++) {
		int N, Q;
		cin >> N >> Q;
		double horse_d[100], horse_s[100], map_d[100][100];
		int U[100], V[100];
		for (int i=0;i<N;i++) cin >> horse_d[i] >> horse_s[i];
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) cin >> map_d[i][j];
		for (int i=0;i<Q;i++) {
			cin >> U[i] >> V[i];
			U[i]--;
			V[i]--;
		}
		
		double map_t[100][100];
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) map_t[i][j] = map_d[i][j];
		for (int x=0;x<N;x++) {
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					for (int k=0;k<N;k++) {
						if (map_t[i][k] == -1 || map_t[k][j] == -1 || i == j) continue;
						if (map_t[i][k] + map_t[k][j] < map_t[i][j] || map_t[i][j] == -1) 
							map_t[i][j] = map_t[i][k] + map_t[k][j];
					}
				}
			}
		}
		if (debug) {
			printf("map_t:\n");
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					printf("%lf ", map_t[i][j]);
				}
				printf("\n");
			}
		}
		for (int i=0;i<N;i++) for (int j=0;j<N;j++) {
			if (map_t[i][j] > horse_d[i]) map_t[i][j] = -1;
			else if (map_t[i][j] != -1) map_t[i][j] /= horse_s[i];
		}
		if (debug) {
			printf("map_t:\n");
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					printf("%lf ", map_t[i][j]);
				}
				printf("\n");
			}
		}
		for (int x=0;x<N;x++) {
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					for (int k=0;k<N;k++) {
						if (map_t[i][k] == -1 || map_t[k][j] == -1 || i == j) continue;
						if (map_t[i][k] + map_t[k][j] < map_t[i][j] || map_t[i][j] == -1) 
							map_t[i][j] = map_t[i][k] + map_t[k][j];
					}
				}
			}
		}
		if (debug) {
			printf("map_t:\n");
			for (int i=0;i<N;i++) {
				for (int j=0;j<N;j++) {
					printf("%lf ", map_t[i][j]);
				}
				printf("\n");
			}
		}
		printf("Case #%d:", nm);
		for (int i=0;i<Q;i++) printf(" %lf", map_t[U[i]][V[i]]);
		printf("\n");
	}
	return 0;
}
