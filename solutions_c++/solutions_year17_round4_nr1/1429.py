/* In the Name of God */
#include <bits/stdc++.h> 
#define F first
#define S second
#define mod 1000000007

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 100000+10;

ofstream fout("out.out");

int a[maxn];

int dp[101][101][101];

int s[4];
int DP (int x , int y , int z)
{
	if(dp[x][y][z] != -1 )
		return dp[x][y][z];

	if(x + y + z == 0)
		return dp[x][y][z] = 0 ;
	
	if(x + y + z  <= 1 )
		return dp[x][y][z] = 1 ;

	if(y >= 2 )
		dp[x][y][z] = max(dp[x][y][z] ,DP(x , y-2 , z)+1 );
	if(x >=1 && z >= 1)
		dp[x][y][z] = max(dp[x][y][z] ,DP(x-1 , y , z-1)+1 );
	if(x >=2 && y >= 1)
		dp[x][y][z] = max(dp[x][y][z] ,DP(x-2 , y-1 , z)+1 );
	if(x >= 4 )
		dp[x][y][z] = max(dp[x][y][z] ,DP(x-4 , y , z)+1 );
	if(z >= 4 )
		dp[x][y][z] = max(dp[x][y][z] ,DP(x , y , z-4)+1 );
	if(z >=2 && y >= 1)
		dp[x][y][z] = max(dp[x][y][z] ,DP(x , y-1 , z-2)+1 );
	
	if(dp[x][y][z] == -1)
		dp[x][y][z] = 1;

	return dp[x][y][z];

}

void init()
{
	memset(dp , -1 , sizeof dp);
	s[0]=s[1]=s[2]=s[3]=0;

}
int main()
{
	int tt ;
	cin>>tt;
	for (int t = 1 ; t <= tt ; t ++ )
	{
		
		int n ,  p ;
		fout<<"Case #"<<t<<": ";
		cin>>n>>p;
		
		init();		
		
		for(int i = 1 ; i <= n ; i ++ )
		{
			cin>>a[i];
			s[ a[i]%p ] ++ ;
		}
		
		if(p == 2)
			fout<<s[0]+(s[1]+1)/2;
		else if( p == 3)
		{
			if(s[1] < s[2])
				swap(s[1] , s[2]);
			fout<<s[0]+(s[1] - s[2] + 2)/3 +s[2] ;
		}
		else
		{
			int ans = s[0];
			ans += DP(s[1] , s[2] , s[3]);
			fout<<ans;
		}


		fout<<endl;
	}
}	

