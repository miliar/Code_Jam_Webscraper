#include <bits/stdc++.h>

#define SZ(a) (int)a.size()
#define PB push_back

using namespace std;

typedef long long ll;

void print_unicorn(char pri, char sec, char* first, int id, int num_sec) {
	if(first[id]) {
		first[id] = 0;
		for(int i = 0; i < num_sec; i++) printf("%c%c", pri, sec);
	}
	printf("%c", pri);
}

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		
		int N;
		char cpri[] = "RYB";
		char csec[] = "GVO";
		int pri[3];
		int sec[3];
		// R, O, Y, G, B, V;
		scanf("%d %d %d %d %d %d %d", &N, &pri[0], &sec[2], &pri[1], &sec[0], &pri[2], &sec[1]);
		
		bool pos = true;
		bool two_co = false;
		char co1 = 'x';
		char co2 = 'z';
		for(int i = 0; i < 3; i++) {
			if(pri[i] + sec[i] == N) {
				co1 = cpri[i];
				co2 = csec[i];
				two_co = true;
				if(pri[i] != sec[i]) pos = false;
			}
		}
		
		if(two_co && pos) {
			for(int i = 0; i < N; i += 2) {
				printf("%c%c", co1, co2);
			}
			printf("\n");
			continue;
		}
		
		int SUM = 0;
		for(int i = 0; i < 3; i++) {
			pri[i] -= sec[i];
			SUM += pri[i];
			if(sec[i] > 0 && pri[i] <= 0) pos = false;
		}
		
		int max_v = 0;
		int id = -1;
		for(int i = 0; i < 3; i++) {
			if(max_v < pri[i]) {
				id = i;
				max_v = pri[i];
			}
		}
		
		int fid = 0;
		if(fid == id) fid++;
		int bid = 2;
		if(bid == id) bid--;
		
		if(pri[fid] + pri[bid] < pri[id]) pos = false;
		
		if(!pos) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		char first_time[] = {1,1,1};
		
		for(int i = 0; i < pri[id]; i++) {
			print_unicorn(cpri[id], csec[id], first_time, id, sec[id]);
			if(i < pri[fid]) {
				print_unicorn(cpri[fid], csec[fid], first_time, fid, sec[fid]);
			}
			if(i >= pri[id] - pri[bid]) {
				print_unicorn(cpri[bid], csec[bid], first_time, bid, sec[bid]);
			}
		}
		printf("\n");
	}
	
	return 0;
}
