#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <iostream>
#define INF (1<<30)
using namespace std;

struct stalls{
	int left, right;
	stalls(int left, int right):left(left), right(right){}

	void LR(int &L, int &R) const{
		int mid=(left+right)/2;
		L=mid-left-1;
		R=right-mid-1;
	}

	bool operator<(const stalls &b) const{
		int L0, L1, R0, R1;
		LR(L0, R0);
		b.LR(L1, R1);
		if(min(L0, R0)!=min(L1, R1))return min(L0, R0)<min(L1, R1);
		if(max(L0, R0)!=max(L1, R1))return max(L0, R0)<max(L1, R1);
		return left<b.left;
	}
};

int main(int argc, char* argv[]){
	int t=0, c=0;
	scanf("%d", &t);
	while(t--){
		int N, K;
		scanf("%d %d", &N, &K);
		priority_queue<stalls> bathroom;
		bathroom.push(stalls(0, N+1));
		for(int i=0; i<K-1; i++){
			stalls tmp=bathroom.top(); bathroom.pop();
			int L=tmp.left, R=tmp.right;
			int mid=(L+R)/2;
			bathroom.push(stalls(L, mid));
			bathroom.push(stalls(mid, R));
		}
		stalls k_th=bathroom.top();
		int ans_L, ans_R;
		k_th.LR(ans_L, ans_R);
		printf("Case #%d: %d %d\n", ++c, max(ans_L, ans_R), min(ans_L, ans_R));
	}
	return 0;
}
