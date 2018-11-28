#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef map<string,int> msi;
typedef set<int> si;

#define INF LONG_LONG_MAX
#define loop(i,a,b) for(ll i=(ll)a;i<=(ll)b;i++)
#define bloop(i,a,b) for(ll i=(ll)b;i>=(ll)a;i--)
#define forit(i, a) for ( __typeof( (a).begin() ) i = (a).begin(); i != (a).end(); i++ )
#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define mem(a, v) memset(a, v, sizeof a)
#define pb push_back
#define mp make_pair
#define MAXN 1000009
#define MOD 1000000007
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define left(x) x<<1
#define right(x) (x<<1)|1
#define PI acos(-1.0)
#define EPS 1e-9

int T,k,n;
string s;

int solve(){
	cin>>s>>k;
	n=s.size();
	int cnt=0;
	for(int i=0;i<n;i++){
	    if(s[i]=='-'){
	        if(i+k>n)
	            return -1;
	        for(int j=i;j<i+k;++j){
	            if(s[j]=='-')
	                s[j]='+';
	            else
	                s[j]='-';
	        }
	        cnt++;
	    }
	}
	return cnt;
}

int main(){
    ios_base::sync_with_stdio(false);
  	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);  
    cin>>T;
    for(int i=1;i<=T;++i){
    	cout<<"Case #"<<i<<": ";
    	int ans=solve();
    	if(ans!=-1)
    	    cout<<ans<<endl;
    	else    
    	    cout<<"IMPOSSIBLE"<<endl;
    	 
    }
    return 0;
}
