#include <cstdio>
#include <math.h>
#include <algorithm>

using namespace std;

int t, T;
int N, C, M;
int p[2000], b[2000];
int ccnt[2000];
int scnt[2000];
int y, z;

int main() {
	int i, j, s;
	bool flag;
	scanf("%d", &T);
	for(t = 1; t <= T; t++) {
		scanf("%d %d %d", &N, &C, &M);
		//init
		for(i = 0; i < 2000; i++) {
			ccnt[i] = 0;
			scnt[i] = 0;
			p[i] = 0;
			b[i] = 0;
		}
		y = 0;
		for(i = 0; i < M; i++) {
			scanf("%d %d", &p[i], &b[i]);
			ccnt[b[i]]++;
			scnt[p[i]]++;
			if(ccnt[b[i]] > y) y = ccnt[b[i]];
		}
		while(y <= M) {	
			z = 0;
			flag = false;
			s = 0;
			for(i = 1; i <= N; i++) {
				s += scnt[i];
				if(s > i * y) {
					flag = true;
					break;
				}
				if(scnt[i] > y) {
					z += scnt[i] - y;
				}
			}
			if(!flag) break;
			y++;
		}
				
		printf("Case #%d: %d %d\n", t, y, z);
	}
	return 0;
}
