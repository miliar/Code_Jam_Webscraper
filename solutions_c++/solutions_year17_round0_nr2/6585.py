#include<bits/stdc++.h>
using namespace std;
#define pi (2.0*acos(0.0))
#define eps 1e-6
#define ll long long
#define inf (1<<30)
#define vi vector<int>
#define vll vector<ll>
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define all(v) v.begin() , v.end()
#define me(a,val) memset( a , val ,sizeof(a) )
#define pb(x) push_back(x)
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define Q(x) (x) * (x)
#define L(x) ((x<<1) + 1)
#define R(x) ((x<<1) + 2)
#define fi first
#define se second
#define MOD 1000000007
#define N 1000000

string s;
int n;
ll t[20][10][2] , T[20];

ll f(int x,int last,int menor){
	if( x == n ){
		return 0;
	}
	ll &ret = t[x][last][menor];
	if( ret != -1 ) return ret;
	ret = -1000000000000000000LL;
	int h = (s[x] - '0');
	if( menor ) h = 9;
	for(int i = last ; i <= h ; i++){
		int newMenor = (i < (s[x] - '0'));
		ret = max( ret , T[n - 1 - x] * i + f( x + 1 , i , (newMenor|menor) ) );
	}
	
	return ret;
}

int main(){
	T[0] = 1;
	for(int i = 1 ; i < 19 ; i++)
		T[i] = T[i-1] * 10;
	
   	int tc;
   	sc(tc);
   	for(int test = 1 ; test <= tc ; test++){
   		cin >> s;
   		n = s.size();
   		me(t,-1);
   		cout << " Case #" << test << ": " << max( f( 1 , 0 , 1 ) , f( 0 , 1 , 0 ) ) << "\n";	
   	}
    return 0;
}

