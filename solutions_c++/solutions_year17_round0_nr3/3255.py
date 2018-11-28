#include<bits/stdc++.h>
#define MOD 1000000007
#define SIZE 1000007
#define ll long long
#define INF LLONG_MAX
#define in(x) scanf("%d",&x)
#define llin(x) scanf("%lld",&x)
#define pr(x) printf("%d",x)
#define llpr(x) printf("%lld",x)
#define line() printf("\n");
#define spc() printf(" ");
#define f(i,a,b) for(i=a;i<b;i++)
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define F first
#define S second
#define boost ios::sync_with_stdio(false)
using namespace std;

typedef pair<ll,ll> ii;
typedef vector<ii> vii;
typedef vector<ll> vi;

ll N,K;
bool flag;
ii ans;
ii TWO = ii(0,1);
ii THREE = ii(1,1);
ii FOUR = ii(1,2);

int mn_depth(ll x){
    if(x==2||x==3) return 1;
    if(x==4) return 2;
    x--;
    return mn_depth(x/2)+1;
}

int mx_depth(ll x){
    if(x==2||x==3) return 1;
    if(x==4) return 2;
    x--;
    return mx_depth(x-x/2)+1;
}

void solve(ii mn,ll count_mn,ii mx,ll count_mx,ll total){
    //cout<<"("<<mn.first<<","<<mn.second<<")x"<<count_mn<<" ("<<mx.first<<","<<mx.second<<")x"<<count_mx<<" "<<total<<"\n";
    if(K<=total+count_mx){
        flag = true;
        ans = mx;
        return;
    }
    if(K<=total+count_mn+count_mx){
        flag = true;
        ans = mn;
        return;
    }
    //check if min and max are 2 and 3 only
    if((mn==TWO||mn==THREE)&&(mx==TWO||mx==THREE))
        return;
    if(mn==FOUR&&mx==FOUR){
        solve(TWO,count_mn,TWO,count_mx,total+count_mn+count_mx);
        return;
    }
    if(mn==THREE&&mx==FOUR){
        // THREE will end and FOURs -> TWOs
        total += (count_mn+count_mx);
        if(K<=total+count_mx){
            flag = true;
            ans = TWO;
        }
        return;
    }
    ll NLL = mn.first;
    ll NLR = mn.second;
    ll NRL = mx.first;
    ll NRR = mx.second;
    NLL--;NLR--;NRL--;NRR--;
    // construct next level minimum
    ll count_mn1 = count_mn;
    if(NLR==NLL) count_mn1 += count_mn;
    if(NRL==NLL) count_mn1 += count_mx;
    if(NRR==NLL) count_mn1 += count_mx;
    ii mn1 = ii(NLL/2,NLL-NLL/2);
    // construct next level maximum
    ll count_mx1 = count_mx;
    if(NLL==NRR) count_mx1 += count_mn;
    if(NLR==NRR) count_mx1 += count_mn;
    if(NRL==NRR) count_mx1 += count_mx;
    ii mx1 = ii(NRR/2,NRR-NRR/2);
    // check if both min,max same
    if(NLL==NRR){
        count_mx1/=2;
        count_mn1/=2;
    }
    solve(mn1,count_mn1,mx1,count_mx1,total+count_mx+count_mn);
}

int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //boost;
    int tc,i,mn,mx;
    ll tmp,NL,NR;
    ii l,r;
    cin>>tc;
    for(int tc1=1;tc1<=tc;tc1++){
        cin>>N>>K;
        if(N==1){
            cout<<"Case #"<<tc1<<": 0 0\n";
            continue;
        }
        else if(K==1){
            N--;
            cout<<"Case #"<<tc1<<": ";
            cout<<N-N/2<<" "<<N/2<<"\n";
            continue;
        }
        tmp = N;
        N--;
        NL = N/2;
        NR = N-N/2;
        NL--;NR--;
        flag = false;
        solve(ii(NL/2,NL-NL/2),1,ii(NR/2,NR-NR/2),1,1);
        cout<<"Case #"<<tc1<<": ";
        if(flag) cout<<ans.second<<" "<<ans.first;
        else cout<<"0 0";
        cout<<"\n";
    }
	return 0;
}
