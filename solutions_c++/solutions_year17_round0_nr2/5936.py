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

const int N = 1e5+7;
const int INF = 1e9+7;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
template<class T> bool umod(T& a, T b) { a += b; while(a < 0) a += INF; a %= INF; return 1;}
typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> omar;

ll a, b, c, d[20], n, m, t;
char sf[20];

int main(){
	freopen("file.in" , "r" , stdin);
	freopen("file.out" , "w" , stdout);
	
	scanf("%lld", &t);
	
	for(int j=1; j<=t; j++){
		scanf("%s", sf);
		
		memset(d, 0LL, sizeof(d));
		d[1] = 1; a = 0, b = 1, c = 0;
		n = strlen(sf);
		
		printf("Case #%d: ", j);
		
		if(n == 1){
			printf("%s\n", sf);
			continue;
		}
		
		for(int i=2; i<=n; i++){
			if(sf[i-1] < sf[i-2]){
				a = i;
				break;
			}
			else if(sf[i-1] > sf[i-2])
				d[i] = i;
			else
				d[i] = d[i-1];
		}
		
		if(!a){
			printf("%s\n", sf);
			continue;
		}
		
		sf[d[a-1]-1]--;
		for(int i=d[a-1]+1; i<=n; i++)
			sf[i-1] = '9';
		
		for(int i=n; i>=1; i--)
			c += (sf[i-1]-'0')*b, b *= 10;
		
		printf("%lld\n", c);
	}
	
	return 0;
}
