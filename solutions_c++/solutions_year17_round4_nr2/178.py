#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

#define x first
#define y second
#define mkp(a,b) make_pair(a,b)
#define PII pair<int,int>

const int MaxN = 1003;

int N, C, M;
int B[MaxN],R[MaxN],extra[MaxN];
vector<PII >  T,P;

int check(int X) {
	P.clear();
	int rem=0;
	int ret=0;
	int j=0;
	for(int r = N; r >= 1; -- r) {
		int cap = X;
		int i = j;
		for(; j < T.size() && T[j].x == r; ++ j);
		if(j - i > X) { // promote some
			int det = j - i - X;
			ret += det;
			rem += det;
		} else { // assign some
			int det = X - (j - i);
			rem = max(0, rem - det);
		}
	}
	if (rem > 0) return -1;
	return ret;
}

int run() {
	scanf("%d %d %d", &N, &C, &M);
	T.clear();
	memset(extra,0,sizeof(extra));
	for(int i=0;i<M;++i){
		scanf("%d %d", R+i, B+i);
		T.push_back(mkp(R[i],B[i]));
		extra[B[i]]++;
	}
	sort(T.begin(), T.end());
	reverse(T.begin(), T.end());
	int lo = *max_element(extra+1,extra+M+1)-1, hi = M, mid;
	while(lo + 1 < hi) {
		mid = lo + hi >> 1;
		int cur = check(mid);
		if (cur < 0) lo = mid;
		else hi = mid;
	}
	int ans = check(hi);
	printf(" %d %d\n", hi, ans);
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no)
	{
		printf("Case #%d:", no);
		run();
	}
}

/*
5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1
*/
