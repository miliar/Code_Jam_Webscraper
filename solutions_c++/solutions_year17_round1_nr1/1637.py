#include <bits/stdc++.h>
using namespace std;
const int oo = 0x3f3f3f3f;
const long long ooo = 0x3f3f3f3f3f3f3f3fll;
template<class T> T abs(T x) { return x > 0 ? x : -x;}
template<class T>  inline T sqr(T x) {return x*x; }
template<class T>  T lcm(T a, T b){return b*a/__gcd(a, b);}
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define rep(i, a, n) for(int i=a; i <n; ++i)
#define per(i, a, n) for(int i=n-1; i>=a; --i)
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define uniq(c) (c).resize(unique(all(c)) - (c).begin())
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<vector<ll> >matrix;
const int MAX = 500;
char s[MAX][MAX];
int sx[MAX], sy[MAX], bx[MAX], by[MAX];
vector<int>v;
void solve(int tc){
  	v.clear();
    for(int i = 'A'; i <= 'Z'; ++i)sx[i] = sy[i] = bx[i] = by[i] = -1;
    printf("Case #%d:\n", tc);
	int n, m;
	scanf("%d %d", &n, &m);
	for(int i = 0; i < n; ++i)scanf(" %s", s[i]);
	rep(i, 0, n){
		rep(j, 0, m){
		  	int c = (int)s[i][j];
			if(c < (int)'A' || c > (int)'Z')continue;
			if(sx[c] == -1){
				sx[c] = bx[c] = i;
				sy[c] = by[c] = j;
				v.push_back(c);
			}else{
				sx[c] = min(sx[c], i);
				bx[c] = max(bx[c], i);
				sy[c] = min(sy[c], j);
				by[c] = max(by[c], j);
			}
		}
	}
	rep(x, 0, sz(v)){
		int c = v[x];
		//printf("%c %d %d %d %d\n", (char)v[x], sx[c], bx[c], sy[c], by[c]);
		for(int i = sx[c]; i <= bx[c]; ++i){
			for(int j = sy[c] ; j <= by[c]; ++j){
				s[i][j] = (char)c;
			}
		}
	}
	rep(x, 0, sz(v)){
		int c = v[x];
		int can;
		do {
		  can = true;
		  int j = by[c] + 1;
		  if(j < m){
			for(int i = sx[c]; i <= bx[c]; ++i){
				if(s[i][j] != '?')can = false;
			}
		  }else can = false;
		  if(can){
			for(int i = sx[c]; i <= bx[c]; ++i){
				s[i][j] = (char)c;
			}
			by[c]++;
		  }
		}while(can);
		do {
		  can = true;
		  int j = sy[c] - 1;
		  if(j >= 0){
			for(int i = sx[c]; i <= bx[c]; ++i){
				if(s[i][j] != '?')can = false;
			}
		  }else can = false;
		  if(can){
			for(int i = sx[c]; i <= bx[c]; ++i){
				s[i][j] = (char)c;
			}
			sy[c]--;
		  }
		}while(can);
		do {
		  can = true;
		  int i = bx[c] + 1;
		  if(i < n){
			for(int j = sy[c]; j <= by[c]; ++j){
				if(s[i][j] != '?')can = false;
			}
		  }else can = false;
		  if(can){
			for(int j = sy[c]; j <= by[c]; ++j){
				s[i][j] = (char)c;
			}
			bx[c]++;
		  }
		}while(can);
		do {
		  can = true;
		  int i = sx[c] - 1;
		  if(i >= 0){
			for(int j = sy[c]; j <= by[c]; ++j){
				if(s[i][j] != '?')can = false;
			}
		  }else can = false;
		  if(can){
			for(int j = sy[c]; j <= by[c]; ++j){
				s[i][j] = (char)c;
			}
			sx[c]--;
		  }
		}while(can);
	}
	rep(i, 0, n)printf("%s\n", s[i]);
}
int main() {
    int tc;
	scanf("%d", &tc);
	rep(i, 0, tc)solve(i+1);
    return 0;
}
