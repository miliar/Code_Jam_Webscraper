#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define pb(f) push_back(f)

#define ll long long
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007LL
#define inf 100000000000000009LL

const int N=200005;
using namespace std;
typedef pair<ll,ll> pii;
typedef vector<int> vi;
typedef vector< pii > vpii;
using namespace std;

FILE *fin=freopen("3.in","r",stdin); FILE *fout=freopen("out.txt","w",stdout);
map<ll,ll> M;
int main(){
    int t;
    cin>>t;
    int cas=0;
    while(t--){
        cas++;
        cout<<"Case #"<<cas<<": ";
        ll n,k;
        cin>>n>>k;
        M.clear();
        M[n]=1;
        while(k){
            auto p=M.rbegin();
            auto it=*p;
            ll low=(it.fi-1)/2;
            ll hi=it.fi-1-low;
            if(k<=it.se){
                cout<<hi<<" "<<low<<endl;break;
            }
            k-=it.se;
            M[low]+=it.se;
            M[hi]+=it.se;
            M.erase(it.fi);
        }
    }
}
