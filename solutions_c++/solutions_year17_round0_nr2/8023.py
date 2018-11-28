#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <tuple>
#include <stdio.h>
#include <string>
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

int n;

bool sorted(char S[]){
	FOR(i, 0, n-1){
		if (S[i] > S[i+1]) return false;
	}
	return true;
}

long long beta(str pal){
	long long ans = 0;
	vecint vec;
	int n=pal.size();
	int j;
	FOR(i, 0, n-1){
		j = pal[i] - '0';
		vec.pb(j);
		if (pal[i] > pal[i+1]){	
			int h=i;
			while (h > 0 && pal[h - 1] == pal[h]){
				vec[h] = 9;
				h--;
			}
			vec[h] -= 1;
			i++;
			FOR(j, 0, vec.size()){
				ans = ans*10 + vec[j];
			}
			while(i<n){
				ans = ans*10 + 9;
				i++;
			}
			return ans;
		}
	}
	j = pal[n-1] -'0';
	FOR(i, 0, vec.size()){
		ans = ans*10+vec[i];
	}
	return ans*10+j;
}

int main(){
	int T;
	ri(T);
	FOR (t, 0, T){
		str pal;
		cin >> pal;
		printf("Case #%d: %lld\n", t + 1, beta(pal));
	}
	return 0;
}