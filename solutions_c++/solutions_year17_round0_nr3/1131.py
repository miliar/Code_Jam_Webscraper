#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <utility>
#include <algorithm>
using namespace std;

//int const MAX_N = 1024 * 1024;

char st[100100];

//struct pp {
//	int lf, rt, ind;
//	pp():lf(0),rt(0), ind(-1) {}
//	pp(int lf, int rt, int ind):lf(lf),rt(rt),ind(ind) {}
//};
//
//bool operator < (const pp &A, const pp &B) {
//	return (min(A.lf,A.rt) > min(B.lf,B.rt)) ||
//		   (  (min(A.lf,A.rt) == min(B.lf,B.rt)) && (max(A.lf,A.rt) > max(B.lf,B.rt))   ) ||
//		   (  (min(A.lf,A.rt) == min(B.lf,B.rt)) && (max(A.lf,A.rt) == max(B.lf,B.rt)) && (A.ind < B.ind)  );
//}
//
//int used[MAX_N];
//pp dst[MAX_N];
//
//void slow_solve(long long N, long long K, long long & mx, long long & mn) {
//	mx = mn = 0;
//	if (K > N)
//		return;
//
//	for (int i=0; i<N; i++) used[i] = 0;
//	for (int i=0; i<N; i++) dst[i] = pp(i, N-1-i, i);
//	pp last_ans;
//	for (int j=0; j<K; j++) {
//		pp mn_val;
//		int is_init = 0;
//
//		for (int i=0; i<N; i++)
//			if (!used[i]) {
//				if (!is_init) {
//					mn_val = dst[i];
//					is_init = 1;
//				}
//				else {
//					if (dst[i] < mn_val)
//						mn_val = dst[i];
//				}
//			}
//
//		used[mn_val.ind] = 1;
//		last_ans = mn_val;
//
//		//repaint
//		int x = mn_val.ind-1;
//		while (x >= 0 && !used[x]) {
//			dst[x].rt = min(dst[x].rt, mn_val.ind-x-1);
//			x--;
//		}
//		x = mn_val.ind + 1;
//		while (x < N && !used[x]) {
//			dst[x].lf = min(dst[x].lf, x-mn_val.ind-1);
//			x++;
//		}
//		//
//	}
//	mx = max(last_ans.lf, last_ans.rt);
//	mn = min(last_ans.lf, last_ans.rt);
//}

long long regen_it(long long N, long long K, long long sh) {
	long long sum_len = 0LL;
	long long cur_block_len = 1LL;
	
	long long our_block = 1, our_block_len = 1;

	for (long long block_id=1; ; block_id++) {
		sum_len += cur_block_len;
		if (sum_len >= K) {
			our_block = block_id;
			our_block_len = cur_block_len;
			break;
		}
		cur_block_len *= 2LL;
	}

	long long group_size = our_block_len * 2LL;
	long long group_sh = our_block_len * sh;

	N -= K;   // now index from '0'

	if (N < group_sh)
		return 0LL;

	N -= group_sh;   // from '0'

	long long gr_index = N / group_size;
	return gr_index + 1;
}

void solve_fast(long long N, long long K, long long & mx, long long & mn) {
	mx = mn = 0;
	if (K >= N)
		return;

	mx = regen_it(N,K,1);
	mn = regen_it(N,K,2);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int t;
	sscanf(st,"%d",&t);
	for (int q=1; q<=t; q++) {
		gets(st);
		printf("Case #%d: ",q);
		long long N,K;
		sscanf(st,"%lld %lld",&N,&K);

		long long a,b;
		solve_fast(N,K,a,b);
		printf("%lld %lld\n",a,b);
	}

	return 0;
}
