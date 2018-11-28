#include "bits/stdc++.h"
#include "ext/pb_ds/assoc_container.hpp"

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define db puts("*****")
#define mid(x , y) ((x+y)>>1)
#define ff first
#define ss second
#define all(x)	x.begin(),x.end()
#define ll long long
#define sqr(x)	((x)*(x))
#define pii pair <int , int>
#define sz(x) int(x.size())
#define tr(it , c) for(__typeof(c.begin()) it = (c.begin()); it != (c.end()); it++)
#define y1 you_made_my_day

using namespace std;
using namespace __gnu_pbds;

const int N = 1e3+7;
const int INF = 1e9+7;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
template<class T> bool umod(T& a, T b) { a += b; while(a < 0) a += INF; a %= INF; return 1;}
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> omar;

int a, b, c, oka, okb, d[N], n, m, t, ans;
char s[N], f[N];

void flip(int x, int y){
	for(int i=x; i<=y; i++){
		if(s[i] == '-')	s[i] = '+';
		else			s[i] = '-';
	}
}

int main(){
	freopen("file.in" , "r" , stdin);
	freopen("file.out" , "w" , stdout);
	
	scanf("%d", &t);
	
	for(int test=1; test<=t; test++){
		scanf("%s%d", f, &m);
		printf("Case #%d: ", test);
		
		n = strlen(f); a = 0, b = 0, oka = okb = 1; ans = INF;
		
		for(int i=0; i<=1e3; i++)	s[i] = f[i];
		
		for(int i=0; i<=n-m; i++){
			if(s[i] == '+')	continue;
			flip(i, i+m-1); a++;
		}
		
		for(int i=0; i<n; i++)
			if(s[i] == '-')
				oka = 0;
		
		for(int i=0; i<=1e3; i++)	s[i] = f[i];
		
		for(int i=n-1; i>=m-1; i--){
			if(s[i] == '+')	continue;
			flip(i-m+1, i); b++;
		}
		
		for(int i=0; i<n; i++)
			if(s[i] == '-')
				okb = 0;
		
		if(oka)	umin(ans, a);
		if(okb)	umin(ans, b);
		
		if(ans == INF)	puts("IMPOSSIBLE");
		else 			printf("%d\n", ans);
	}
	
	return 0;
}
