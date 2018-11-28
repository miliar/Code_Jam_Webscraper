#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) ((x < 0)?-(x):x)
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

typedef long long cat;

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	int ans[110][110][110];
	for(int t =0; t < T; t++) {
		if(T >= 10) {cerr << t << ((t == T-1)?"\n":" "); flush(cerr);}
		cout << "Case #" << t+1 << ": ";
		int N,P;
		cin >> N >> P;
		int cnt[4];
		cnt[0] =cnt[1] =cnt[2] =cnt[3] =0;
		int sum =0;
		for(int i =0; i < N; i++) {
			int x;
			cin >> x;
			sum +=x;
			cnt[x%P]++;}
		for(int i =0; i <= N; i++) for(int j =0; j <= N; j++) for(int k =0; k <= N; k++) ans[i][j][k] =-N;
		ans[cnt[1]][cnt[2]][cnt[3]] =cnt[0];
		int ansF =0;
		for(int i =N; i >= 0; i--) for(int j =N; j >= 0; j--) for(int k =N; k >= 0; k--) if(ans[i][j][k] >= 0) {
			ansF =max(ansF,ans[i][j][k]);
			for(int a =0; a <= min(4,i); a++) for(int b =0; b <= min(4,j); b++) for(int c =0; c <= min(4,k); c++) 
				if((a+2*b+3*c)%P == 0 && a+2*b+3*c > 0)
					ans[i-a][j-b][k-c] =max(ans[i-a][j-b][k-c],ans[i][j][k]+1);
			}
		if(sum%P != 0) ansF++;
		cout << ansF << "\n";}
	return 0;}

// look at my code
// my code is amazing