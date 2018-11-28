#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <map>
#include <string>
#include <ctime>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION SMALL
#define MAKE_OUTFILE
#define MAX_SIZE 102
#define INF 100000007
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,ans;
int Hd, Ad, Hk, Ak, B, D;
int dp[MAX_SIZE][MAX_SIZE][MAX_SIZE][MAX_SIZE];
bool vis[MAX_SIZE][MAX_SIZE][MAX_SIZE][MAX_SIZE];
int search(int hd, int ad, int hk, int ak) {
	if (ak < 0) 
		ak = 0;
	if (hd <= 0) {
		dp[hd][ad][hk][ak] = INF;
		return INF;
	} 
	if (hk <= 0) {
		dp[hd][ad][hk][ak] = 0;
		//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
		return 0;
	}
	if (hk <= ad) {
		dp[hd][ad][hk][ak] = 1;
		//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
		return 1;
	}
	if (dp[hd][ad][hk][ak] != -1)
		return dp[hd][ad][hk][ak];
	if (vis[hd][ad][hk][ak])
		return INF;
	vis[hd][ad][hk][ak] = 1;
	int x = INF, y;
	if (ak-D >= hd) {
		dp[hd][ad][hk][ak] = min(search(max(0,Hd-ak), ad, hk, ak)+1,INF);
		//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
		return dp[hd][ad][hk][ak];
	}
	if (ak >= hd) {
		x = min(search(max(0,Hd-ak), ad, hk, ak)+1,INF);
		y = min(search(max(0,hd-max(0,ak-D)), ad, hk, max(0,ak-D))+1,INF);
		if (x < y) {
			dp[hd][ad][hk][ak] = x;
			//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
			return x;
		} else {
			dp[hd][ad][hk][ak] = y;
			//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
			return y;
		}
	}	
	y = min(search(max(0,hd-ak), ad, max(0,hk-ad), ak)+1,INF);
	if (y < x)
		x = y;		
	y = min(search(max(0,hd-max(0,ak-D)), ad, hk, max(0,ak-D))+1,INF);
	if (y < x)
		x = y;
	if (ad+B <= hk) {
		y = min(search(max(0,hd-ak), ad+B, hk, ak)+1,INF);
		if (y < x)
			x = y;
	}
	dp[hd][ad][hk][ak] = x;
	//cout << hd << ' ' << ad << ' ' << hk << ' ' << ak << " = " << dp[hd][ad][hk][ak] << '\n';
	return x;
}
		
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("C-small.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("C-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		clock_t t0 = clock();
		for (int i=0; i<=Hd; ++i) {
			for (int j=0; j<=max(Ad, Hk); ++j) {
				for (int k=0; k<=Hk; ++k) {
					for (int l=0; l<=Ak; ++l) {
						dp[i][j][k][l] = -1;
						vis[i][j][k][l] = 0;
					}
				}
			}
		}
		ans = search(Hd,Ad,Hk,Ak);
		cout << "Case #" << cas+1 << ": ";
		if (ans == INF) {
			cout << "IMPOSSIBLE\n";
		} else {
		  cout << ans << '\n';
		}
		//cout << clock()-t0 << endl;
	}
	return 0;
}
