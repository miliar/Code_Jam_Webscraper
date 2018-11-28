#include <cstdio>
#include <queue>
using namespace std;
void lsrs(int N, int *ls, int *rs) {
	if (N % 2 == 0) {
		*ls = (N - 1) / 2;
		*rs = (N - 1) / 2 + 1;
	}
	else {
		*ls = (N - 1) / 2;
		*rs = (N - 1) / 2;
	}
}
int main(void) {
	int T;
	FILE* infp = fopen("C-small-1-attempt0.in", "r");
	FILE* oufp = fopen("output.ou", "w");
	
	fscanf(infp,"%d", &T);

	for (int t = 0; t < T; t++) {
		int N, k = 0, ls, rs;
		
		priority_queue<int> before_queue;
		//printf("start\n");
		
		fscanf(infp,"%d %d", &N, &k);
		//printf("K %d\n", k);

		lsrs(N, &ls, &rs);
		if (ls < rs) {
			N = rs;
			before_queue.push(ls);
		}
		else if (ls >= rs) {
			N = ls;
			before_queue.push(rs);
		}

		//printf("K %d\n", k);

		for (int i = 2; i <= k; i++) {
			lsrs(N, &ls, &rs);
			if (ls < rs && rs >= before_queue.top()) {
				N = rs;
				before_queue.push(ls);
			}
			else if (ls >= rs && ls >= before_queue.top()) {
				N = ls;
				before_queue.push(rs);
			}else if (ls <= before_queue.top() && rs <= before_queue.top()){
				int tnum = before_queue.top();
				before_queue.pop();
				before_queue.push(ls);
				before_queue.push(rs);
				N = tnum;
			}
		}
		if(ls >= rs) fprintf(oufp,"Case #%d: %d %d\n",t+1,ls, rs);
		else fprintf(oufp,"Case #%d: %d %d\n", t+1,rs, ls);
	}
}