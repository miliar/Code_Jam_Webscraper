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

int T, t, K;
string s;

void solve(){
	cin>>s>>K;
	int i, j, count=0;
	for(i=0;i<s.length();i++){
		if(i+K-1>=s.length()) break;
		if(s[i]=='-'){
			count++;
			for(j=i;j<i+K;j++){
				if(s[j]=='+') s[j]='-';
				else s[j]='+';
			}
		}
	}
	for(;i<s.length();i++)
		if(s[i]=='-') break;
	if(i!=s.length()) cout<<"Case #"<<++t<<": "<<"IMPOSSIBLE"<<endl;
	else cout<<"Case #"<<++t<<": "<<count<<endl;
}

int main(){
    ios_base::sync_with_stdio(false);
  	freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);  
    cin>>T;
    while(T--){
    	solve();
    }
    return 0;
}