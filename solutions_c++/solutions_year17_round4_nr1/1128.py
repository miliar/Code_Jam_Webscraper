#include <bits/stdc++.h>

#define ll long long
#define ld long double

#define all(x) x.begin(),x.end()

using namespace std;

const int mod = 1e9+7;
const ld pi = 3.14159265358979;

int n,p;
int g[105];
int m = 0;

int memo[4][105][105][105];

int go(int r, int i, int j, int k)
{
	if (memo[r][i][j][k]!=-1) return memo[r][i][j][k];
	memo[r][i][j][k] = 0;
	if (i) memo[r][i][j][k] = max(memo[r][i][j][k],go((r+1)%p,i-1,j,k));
	if (j) memo[r][i][j][k] = max(memo[r][i][j][k],go((r+2)%p,i,j-1,k));
	if (k) memo[r][i][j][k] = max(memo[r][i][j][k],go((r+3)%p,i,j,k-1));
	return memo[r][i][j][k] + (r==0 && (i+j+k));
}

int main()
{
   	ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cout<<fixed<<setprecision(10);
    
    int testno;
    cin>>testno;
    for(int testi=1; testi<=testno; testi++)
    {	
    	m=0;
    	cin>>n>>p;
    	for (int i=0; i<n; i++)
    		cin>>g[i],g[i]%=p;
    	for (int i=0; i<n; i++)
    		m+=(g[i]==0);
    		
    	for (int i=0; i<p; i++)
    		for (int j=0; j<=n; j++)
    			for (int k=0; k<=n; k++)
    				for (int kk=0; kk<=n; kk++)
	    				memo[i][j][k][kk]=-1;

		int a[3];
		for (int i=0; i<3; i++)
			a[i]=0;
		for (int i=0; i<n; i++)
			if (g[i]) a[g[i]-1]++;
    	
    	m+=go(0,a[0],a[1],a[2]);
    
    	cout<<"Case #"<<testi<<": ";
    	cout<<m;
    	cout<<'\n';
    	
    	cerr<<"Case #"<<testi<<": ";
    	cerr<<m;
    	cerr<<'\n';
    }
    return 0;
}
