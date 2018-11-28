/* In the Name of God */
#include <bits/stdc++.h> 
#define F first
#define S second
#define mod 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<int,char> pic;

const int maxn = 100000+10;

ofstream fout("out.out");

ld k[101] , s[101];
ld w[101][101];
ld best[101][101];
ld ans[101];
int  n , q ;

ld abss(ld x)
{
	if(x<0)
		return -x;
	return x;
}

ld findAns(int u , int v)
{

	for(int i = 1 ; i <=n ; i ++ )
		for(int j = 1 ; j <=n ; j ++ )
		{
			if(w[i][j] == -1)
				best[i][j] = 1e15;
			else
				best[i][j] = w[i][j];
		}
	
	for(int i = 0 ; i < 101 ; i ++ )
	{
		ans[i]=1e15;
		best[i][i] = 0 ;
	}

	for(int h = 1 ; h <=n ; h ++ )
		for(int i = 1 ; i <=n ; i ++ )
			for(int j = 1 ; j <=n ; j ++ )
				best[i][j] = min(best[i][j] , best[i][h] + best[h][j]);

	
	ans[u] = 0;

	for(int h =1 ; h <= n ; h ++ )
		for(int i = 1 ; i <= n ; i ++ )
			if(ans[i]!=1e15)
				for(int j = 1 ; j <= n ; j ++ )
					if(k[i] >= best[i][j])
						if(ans[j]>ans[i] + best[i][j]/s[i] )
							ans[j] = ans[i] + best[i][j]/s[i] ;
	return ans[v];

}
int main()
{
	int t ,test = 1 ;
	cin>>t;
	while(t)
	{

		cin>>n>>q;
		for(int i = 1 ; i <= n ; i ++ )
			cin>>k[i]>>s[i];
		for(int i = 1 ; i <=n ; i ++ )
			for(int j = 1 ; j <= n ; j ++ )
				cin>>w[i][j];
		
		fout<<"Case #"<<test<<": ";

		for(int i = 1 ; i <= q ; i ++ )
		{
			int u , v ;
			cin>>u>>v;
			fout<<fixed<<setprecision(6)<<findAns(u,v)<<' ';
		}
		fout<<endl;
		t--;
		test ++ ;
	}	
}	
