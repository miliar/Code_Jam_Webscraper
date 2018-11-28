#include "bits/stdc++.h"

#define mp make_pair
#define pb push_back
#define ppb pop_back
#define db puts("*****");
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

const int N = 50+7;
const int INF = 1e9+7;

template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}

int n, m, t;
double a, b, c, d[N], U;

int main(){
	freopen("file3.in", "r", stdin);
	freopen("file3.out", "w", stdout);
	
	cout.precision(12);
	scanf("%d", &t);
	
	for(int test=1; test<=t; test++){
		memset(d, 0.0, sizeof(d));
		cout << "Case #" << test << ": ";
		scanf("%d%d", &n, &m);
		scanf("%lf", &U);
		double tr = 1;
		
		for(int i=1; i<=n; i++)	scanf("%lf", &d[i]);
		sort(d+1, d+n+1);
		
		for(int i=2; i<=n; i++){
			if(d[i] == d[i-1])	continue;
			if(U/(i-1) >= d[i]-d[i-1]){
				U -= (i-1)*(d[i]-d[i-1]);
				
				for(int j=1; j<=i; j++)
					d[j] = d[i];
			}
			else{
				for(int j=1; j<i; j++)
					d[j] += (double)U/(i-1);
				
				U = 0;
				break;
			}
		}
		
		for(int i=1; i<=n; i++)	d[i] += (double)U/n;
		
		for(int i=1; i<=n; i++)	tr *= d[i];
		
		cout << fixed << tr << endl;
	}
	
	return 0;
}

