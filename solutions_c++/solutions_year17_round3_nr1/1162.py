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
#define N 2000
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
typedef priority_queue<pii , vector<pii > ,greater<pii > > min_pq;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> OST; 

double dp [ 1011 ][ 1011 ] [2];

pair <double,double > ar[N];

ll n , k;

double solve ( ll idx , ll numb ,ll taken)
{
	// cout << idx <<" "<<  numb <<" "<< taken<<endl;
	if ( numb == 0 || idx == 0)
	{
		// cout << " hell";
		return 0;
	}
	else if ( dp[idx][numb][taken] != -1)
	{
		// cout << " hie";
		return dp[idx][numb][taken];
	}
	else
	{
		double val = solve ( idx - 1 , numb,taken);
		if ( taken )
		{
			// cout << " hi";
			val = max ( val , (double)solve ( idx -1 , numb - 1 , 1 ) + (double)(PI)*(double)(2)*(ar[idx].fi)*(ar[idx].sec) );
		}
		else
			val = max ( val , (double)solve ( idx -1 , numb - 1 , 1) + (double)(PI)*(double)(2)*(ar[idx].fi)*(ar[idx].sec) + (double)(PI)*(double)(ar[idx].fi)*(ar[idx].fi));
		return dp[idx][numb][taken]=val;
	}

}

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

		for( ll i=1;i<=n;i++)
		{
			cin >> ar[i].fi >> ar[i].sec;
		}

		sort ( ar+1 , ar + n + 1 );

		for (ll i=0;i<1011;i++)
		{
			for (ll j=0;j<1011;j++)
			{
				for (ll f=0;f<=1;f++)
					dp[i][j][f] = -1;
			}
		}

		cout <<  fixed <<setprecision(8)<<solve ( n , k , 0 )  <<endl; 



		


		// cout << ans << endl;









		

		


		
	}













}	