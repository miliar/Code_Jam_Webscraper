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
#define N 1005

string s;
int k, t[N];

int main(){
    int tc;
   	sc(tc);
   	for(int test = 1 ; test <= tc ; test++){
   		cin >> s >> k;
   		int ans = 0 , r = 0 , n = s.size();
   		for(int i = 0 ; i < n ; i++)
   			if( s[i] == '+' ) t[i] = 1;
   			else t[i] = 0;
   		
   		for(int i = 0 ; i + k <= n ; i++){
   			if( !t[i] ){
   				ans++;
   				for(int j = i ; j < i + k ; j++)
   					t[j] = !t[j];
   			}
   		}
   		
   		for(int i = 0 ; i < n ; i++)
   			r += t[i];
   				
   		cout << " Case #" << test << ": ";
   		if( r != n ) cout << "IMPOSSIBLE\n";
   		else cout << ans << "\n";
   		
   	}
   	
    return 0;
}

