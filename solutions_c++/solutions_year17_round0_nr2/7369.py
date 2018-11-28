#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define sc(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);

#define scl(x) scanf("%lld",&x);
#define scl2(x,y) scanf("%lld%lld",&x,&y);
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);

#define pb push_back
#define mp make_pair

#define M 1000000007
#define inf 99999999999999999LL	//long long inf

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";

#define LIM 100020

ll n , digs,dp[22][4][11];
string s ;

ll func(int ind , int tight , int last)
{

	if( ind >= digs )
		return 1;
	ll &answer = dp[ind][tight][last];
	if(answer != -1)
		return answer;
	answer = 0;
	if( tight )
	{	
		int start = 0 ;
		for(int i = 0  ; i<=(int)(s[ind]-'0') ; i++)
		{
			if( i == s[ind] - '0')
			{
				if( i >= last )
					answer = answer + func( ind +1 , 1 , i );
			}
			else
			{
				if( i >= last )
					answer = answer + func( ind +1 , 0 , i );	
			}
		}
	}
	else
	{
		for(int i = 0  ; i<=9 ; i++)
		{
			if( i>=last )
				answer = answer + func( ind +1 , 0 , i );
		}
	}
	return answer ;

}
ll original ;
bool solve(ll mid)
{
	memset(dp,-1,sizeof dp);
	s = to_string( mid );
	digs = s.size();
	ll chut = func( 0 , 1 ,0);
	if( chut == original )
	{
		return true  ;
	}
	else
	{
		return false ;
	}
}
int main()
{
	int i,j,t;
	sc(t);
	int tutu = 1;
	while(t--)
	{
		memset(dp,-1,sizeof dp);
		n =0;
		cin>>s;
		digs = s.size();
		for (int i = 0; i < digs; ++i)
		{
			n = n*10 + (s[i] - '0');
		}
		original = func( 0, 1, 0 ) ;
		ll low = 0 , high = n ,mid;
		while(low<high)
		{
			mid = (low + high + 1)/2;
			if(solve( n - mid )==false)
				high = mid-1;
			else
				low = mid ;				
		}
		printf("Case #%d: %lld\n",tutu++,n-low);
	}
	return 0;
}