#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<bits/stdc++.h>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<bitset>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define mod 1000000007
#define mod1 mod
#define mod2 100000009
#define li long long int
#define ll long long int
#define readi(x) scanf("%d",&x)
#define  reads(x)  scanf("%s", x)
#define readl(x) scanf("%I64d",&x)
#define rep(i,n) for(i=0;i<n;i++)
#define revp(i,n) for(i=(n-1);i>=0;i--)
#define myrep1(i,a,b) for(i=a;i<=b;i++)
#define myrep2(i,a,b) for(i=b;i>=a;i--)
#define pb push_back
#define mp make_pair
#define fi first
#define sec second
#define MAXN 1000000000000000100
#define MINN -10000000000000
#define pii pair<ll,ll> 
#define pic pair<int,char>
#define N 1500
#define N2 5010
#define lgn 20
#define ddouble long double
#define minus minu
#define INTMAX 10000000
#define si short int
#define PI 3.1415926535
using namespace std;
using namespace __gnu_pbds;         
typedef priority_queue<pair<ll,char> , vector<pair<ll , char> > > max_pq;
typedef priority_queue<ll, vector<ll > ,greater<ll > > min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST; 

ll n , k;

min_pq pq;

double u;

int main()
{

	ios::sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t;

	cin>>t;

	for (ll x=1 ;x<=t ;x++)
	{

		cout << "Case #"<<x<<": ";

		cin >> n >> k;

		cin >> u;

		ll f = (double)(u)*(double)(10000) + (double)0.1;
		for (ll i=1;i<=n;i++)
		{
			double p;
			cin >> p;
			ll y;
			y = (double)(p)*(double)(10000) + (double)0.1;
			pq.push ( y );
		}

		while ( f!=0)
		{
			// cout << u << endl;
			ll x =pq.top();
			pq.pop();
			f= (f) -(1);
			x = x + (1);
			pq.push ( x );

		}
		double ans = 0;

		while(!pq.empty())
		{
			ans = (double)(( double)( ans) + ( double)log( pq.top()) - (double)log( 10000));
			pq.pop();
		}

		cout << fixed <<setprecision ( 8 ) << exp(ans) <<endl;





		


		// cout << ans << endl;









		

		


		
	}













}	