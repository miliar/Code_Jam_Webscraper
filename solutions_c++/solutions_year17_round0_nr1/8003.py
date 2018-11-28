#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <tuple>
#include <stdio.h>
#include <string>
#include <cstring>
using namespace std;
//Status: AC
#define FOR(j, s, m) for(int j = s; j < m; j++)
#define FORR(i, s, m)  for(int i = s; i > m; i--)
#define pb push_back
#define mp make_pair
#define SORTVEC(vec) sort(vec.begin(), vec.end())
#define SORTARR(arr, N) sort(arr, arr + N)
#define mset(arr, value) memset(arr, value, sizeof(arr))
#define mt make_tuple
#define SORTVECFUNC(vec, fun) sort(vec.begin(), vec.end(), fun)
#define fst first
#define scn second
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d %d", &x, &y)
#define lb_vec(v,x) lower_bound(v.begin(), v.end(), x)

typedef vector<int> vecint;
typedef string str;


bool check(int S[], int n){
	FOR(i, 0, n){
		if (S[i] == 0) return false;
	}
	return true;
}


int main()
{
	int t;
	ri(t);
	FOR(h, 0, t){
		str beta;
		int k, ans = 0;
		cin >> beta >> k;
		int beta2[beta.size()];
		FOR(i, 0, beta.size()){
			if (beta[i] == '+'){
				beta2[i] = 1;
			}
			else{
				beta2[i] = 0;
			}
		}
		FOR(i, 0, beta.size() - k +1){
			if (!beta2[i]){
				FOR(j, i, k+i){
					beta2[j] ^= 1;
				}
				ans++;
			}
		}
		if (!check(beta2, beta.size())){
			printf("Case #%d: IMPOSSIBLE\n", h+1);
		}
		else{
			printf("Case #%d: %d\n", h+1, ans);
		}
	}
	
	return 0;
}
