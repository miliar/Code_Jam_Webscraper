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

vecint check(str beta){
	vecint ans;
	FOR(i, 0, beta.size()){
		if (beta[i] != '?') ans.pb( i);
	}
	return ans;
}

int main()
{
	int T;
	ri(T);
	FOR(tc, 0, T){
		int r, c;
		rii(r, c);
		str pal[r];
		FOR(i, 0, r){
			cin >> pal[i];
		}
		printf("Case #%d: \n", tc+1);
		int aux = 1;
		str last;
		FOR(i, 0, r){
			vecint points = check(pal[i]);
			if (points.size() == 0){
				aux++;
				if (i == r-1)FOR(j, 0, aux-1) cout << last << endl;
			} 
			else{
				int start = 0;
				if (points[points.size()-1] < c-1){
					pal[i][c-1] = pal[i][ points [ points.size()-1 ] ];
					points[points.size()-1] = c-1;
				}
				FOR(j, 0, points.size()){
					int h = points[j];
					while(start < h) {pal[i][start] = pal[i][h];start++;}
					start = h+1;
				}
				FOR(j, 0, aux) cout << pal[i]<< endl;
				aux = 1;
				last = pal[i];
			}
		}
	}
	
	return 0;
}
