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
#define pb push_back

vi v;
int T,a[25];
ll N;

ll solve(){
    ll n;
	cin>>n;
	N=n;
	v.clear();
	while(n>0)
	{
	   v.push_back(n%10);
	   n/=10;
	}
	memset(a,0,sizeof a);
	int dig=v.size();
	//reverse(v.begin(),v.end());
	for(int p=0;p<dig;p++)
	for(int i=0;i<dig;++i){
	    for(int j=i;j<dig;++j){
	        if(v[i]<v[j]){
	            int k;
	            for(k=i;k<j;++k){
	                v[k]=9;
	                a[k]=1;
	            }
	            while(v[k]==0&&k<dig)     
	                v[k++]=9; 
	            if(k<dig){
	                if(v[k]==9&&a[k]==1)
	                    continue;
	                v[k]--;
	            }
	        }
	    }
	}
	n=0;
	reverse(v.begin(),v.end());
	for(int i=0;i<v.size();++i){
	    n*=10;
	    n+=v[i];
	}
	return n;
}

int main(){
    ios_base::sync_with_stdio(false);
  	freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);  
    cin>>T;
    for(int i=1;i<=T;++i){
        cout<<"Case #"<<i<<": ";
    	cout<<solve()<<endl;
    }
    return 0;
}
