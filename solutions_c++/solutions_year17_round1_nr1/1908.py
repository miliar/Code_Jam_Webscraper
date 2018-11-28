#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<long long> > vvii;
typedef vector< pair<ll,ll> > vpii;
 
#define boost std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin() , (x).end()
#define out(x) cout<<x<<"\n"
#define sz(x)  (x).size()
#define nl cout<<"\n"
#define INF 1000001
#define F first
#define S second
 
int main()
{
    boost;
    int t,tc=1;
    cin>>t;
    while(t--)
    {
        int n,m,i,j,k,x,y,z;
        cin>>n>>m;
        char a[n][m];
        FOR(i,0,n)
        {
        	string s; cin>>s;
        	FOR(j,0,m) a[i][j]=s[j];
        }
        FOR(i,0,n)
        {
        	bool all=1;
        	FOR(j,0,m)
        	{
        		if(a[i][j]!='?'){
        			all=0; break;
        		}
        	}
        	if(all==0){
        		// cout<<"i = "<<i; nl;
        		j=0;
        		while(a[i][j]=='?') j++;
        		char c=a[i][j];
        		FOR(x,0,j)
        			a[i][x]=c;
        		j++;
        		while(j<m){
        			if(a[i][j]=='?'){
        				a[i][j]=c;
        			}
        			else{
        				c=a[i][j];
        			}
        			j++;
        		}
        	}
        }
        i=0;
        while(a[i][0]=='?') i++;
        FOR(x,0,i)
        {
        	FOR(j,0,m)
        	{
        		a[x][j]=a[i][j];
        	}
        }
        z = i;
        i++;
        while(i<n)
        {
        	if(a[i][0]=='?'){
        		FOR(j,0,m)
        			a[i][j]=a[z][j];
        	}
        	else{
        		z=i;
        	}
        	i++;
        }
        cout<<"Case #"<<tc++<<":\n";
        FOR(i,0,n)
        {
        	FOR(j,0,m) cout<<a[i][j];
        	nl;
        }
    }
    return 0;
}     