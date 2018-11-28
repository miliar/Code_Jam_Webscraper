#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)
#define EPS 1e-28
#define PI 2*acos(0.0)
#define y1 fdsad

typedef long long ll;
typedef vector<int> vi;

int T, R, C;
const int MAXN = 30;
string G[MAXN];
int main(){
	cin >> T;
	FOR(t, 1, T+1){
		cin >> R >> C;
		FOR(i, 0, R) cin >> G[i];
		
		FOR(i, 0, R) FOR(j, 1, C)
			if(G[i][j]=='?') G[i][j] = G[i][j-1];
		
		FOR(i, 0, R) FORR(j, C-2, -1)
			if(G[i][j]=='?') G[i][j] = G[i][j+1];
		
		FOR(i, 1, R) FOR(j, 0, C)
			if(G[i][j]=='?') G[i][j] = G[i-1][j];
		
		FORR(i, R-2, -1) FOR(j, 0, C)
			if(G[i][j]=='?') G[i][j] = G[i+1][j];
		
		cout << "Case #" << t << ": " <<endl;
		FOR(i, 0, R) cout << G[i] << endl;
	}
}

