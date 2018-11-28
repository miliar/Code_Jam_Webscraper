//----------------------JUGNU:LET YOUR LIGHT SHINE---------------------------//
#include <bits/stdc++.h>
#define ll long long int
#define ld long double
#define pb push_back
#define pf push_front
#define sz size
#define mk make_pair
#define ln length
#define fr(i,a,b) for(i=a;i<b;i++)
#define fre(i,a,b) for(i=a;i<=b;i++)
#define frr(i,a,b) for(i=a;i>=b;i--)
#define sc(a) scanf("%d", &a)
#define sm(a, b) scanf("%d%d", &a, &b)
#define pr(a) printf("%d\n", a)
#define pm(a, b) printf("%d %d\n", a, b)
#define isset(x,i) ((x>>i)&1)
#define MAXN 100005
#define MOD 1000000007LL
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);

#define trace1(x)       cerr << #x << " : " << x << endl;
#define trace2(x, y)    cerr << #x << " : " << x << " | " << #y << " : " << y << endl;
#define trace3(x, y, z) cerr << #x << " : " << x << " | " << #y << " : " << y << " | " << #z << " : " << z << endl;
#define cline cout << "----------------------" << endl;
using namespace std;
bool isTidy(ll x){
	int prev = x % 10;
	x /= 10;
	while(x != 0){
		if((x % 10) > prev) return false;
		prev = x % 10;
		x /= 10;
	}
	return true;
}

ll n;
int main()
{
	int i, j, t, m, k, l, r, temp, mini, maxi, flag, cnt, test;
	scanf("%d", &test);
	fre(t, 1, test){
		scanf("%lld", &n);
		while(!isTidy(n)) n--;
		printf("Case #%d: %lld\n", t, n);
	}
return 0;
}