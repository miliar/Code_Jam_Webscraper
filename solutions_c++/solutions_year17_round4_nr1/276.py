#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <utility>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <map>
#define ll long long
#define read(x) scanf("%d",&x);
#define readll(x) cin>>x;
#define FOR(x,a,b) for(int x=a;x<b;x++)
#define MP make_pair
#define PB push_back
#define pii pair<int,int>
#define readN(N,X) for(int i=0;i<N;i++) scanf("%d",&X[i]);
using namespace std;
int N;
int P;
int dp[101][101][101][4];
int wow[99];

int itung(int a,int b, int c, int pos){
	if (a == 0 && b == 0 && c == 0)
		return 0;
	if (dp[a][b][c][pos] != -1)
		return dp[a][b][c][pos];
	int kagi =0;
	if (a) kagi = max(kagi, itung(a-1,b,c, (pos + 1) % P));
	if (b) kagi = max(kagi, itung(a,b-1,c, (pos + 2) % P));
	if (c) kagi = max(kagi, itung(a,b,c-1, (pos + 3) % P));
	if (pos == 0) kagi++;
	dp[a][b][c][pos] = kagi;
	return kagi;

}

void solve(){
	int res = 0;
	read(N);
	read(P);
	wow[1] = 0;
	wow[2] = 0;
	wow[3] = 0;
	for(int i=0;i<N;i++){
		int x;
		read(x);
		int c = x % P;
		if (c == 0) res++;
		else {
			wow[c]++;
		}
	}
	memset(dp, -1, sizeof (dp));
	res += itung(wow[1], wow[2], wow[3], 0);
	cout<<res<<endl;
}

int main(){
	int T;
	read(T);
	int cn = 1;
	while(T--){
		printf("Case #%d: ", cn++);
		solve();
	}
}
