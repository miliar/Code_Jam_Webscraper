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

int main() {
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //boost;
    int tc,i,j,n,k,ans,ans1;
    bool flag;
    string str,tmp;
    cin>>tc;
    for(int tc1=1;tc1<=tc;tc1++){
        ans = 0;ans1=0;
        cin>>str>>k;
        n = str.length();
        tmp = str;
        flag = true;
        for(i=0;i<n-k+1;i++)
            if(str[i]=='-'){
                for(j=0;j<k;j++)
                    str[i+j]=(str[i+j]=='+'?'-':'+');
                ans++;
            }
        for(i=0;i<n;i++)
            if(str[i]=='-')
                break;
        if(i<n) flag = false;
        str = tmp;
        reverse(str.begin(),str.end());
        for(i=0;i<n-k+1;i++)
            if(str[i]=='-'){
                for(j=0;j<k;j++)
                    str[i+j]=(str[i+j]=='+'?'-':'+');
                ans1++;
            }
        for(i=0;i<n;i++)
            if(str[i]=='-')
                break;
        cout<<"Case #"<<tc1<<": ";
        if(i<n){
            if(!flag) cout<<"IMPOSSIBLE";
            else cout<<ans;
        }
        //else cout<<ans<<" "<<ans1;
        else cout<<min(ans,ans1);
        cout<<"\n";
    }
	return 0;
}
