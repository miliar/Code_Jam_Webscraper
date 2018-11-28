#include<bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define ll long long
#define int long long

using namespace std ;

const int MAXN = 1001 * 1001 ; 

void solve()
{
	int n , p ; 
	int a[4] = {} ;
	cin >> n >> p  ;
	int x ; 
	for(int i = 0 ; i < n ; i ++ ) cin >> x , a[x%p] ++ ; 
	if(p==2)
	{
		cout << a[0] + (a[1]+1) / 2 ;
		return; 
	}
	if(p==3)
	{
		int ans = a[0] + min(a[1],a[2]) ; 
		int x = min(a[1],a[2]) ; 
		a[1] -= x ; 
		a[2] -= x ;
		ans += a[1] / 3 + a[2] / 3 ;
		if(a[1]%3>0||a[2]%3>0) ans ++ ; 
		cout << ans ;
		return ; 
	}
	int ans = a[0] ;
	ans += (a[2]) / 2 ; 
	ans += min(a[1],a[3]) ;
    x = min(a[1],a[3]) ; 
	a[1] -= x , a[3] -= x ; 	
	ans += a[1] / 4 + a[3] / 4 ; 
	if(a[2]%2>0||a[1]%4>0||a[3]%4>0) ans ++ ; 
	cout << ans ; 
	return ;
}

int32_t main()
{
	ios::sync_with_stdio(0) ; cin.tie(0) ; 
	int t ;
	cin >> t ; 
	for(int i = 1 ; i <= t ; i ++ ) 
	{
		cout << "Case #"<<i << ": " ; 
		solve() ; 
		cout << endl ; 
	}
}
