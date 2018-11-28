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
    double ans;
    int tc,i;
    ll D,N;
    cin>>tc;
    for(int tc1=1;tc1<=tc;tc1++){
        cin>>D>>N;
        vii ar(N);
        f(i,0,N)
            cin>>ar[i].F>>ar[i].S;
        sort(ar.begin(),ar.end());
        ans = (double)INF;
        /*
        for(i=N-1;i>=0;i--){
            double tim,temp;
            for(j=i+1;j<N;j++){
                temp = ((double)D-ar[j].F)/(double)ar[j].S;
                if(temp<tim)
            }
            ans = min(ans,(double)D/tim);
        }*/
        double temp = 0.0;
        f(i,0,N)
            temp = max(temp,((double)D-ar[i].F)/(double)ar[i].S);
        ans = (double)D/temp;
        cout<<"Case #"<<tc1<<": ";
        printf("%.6lf\n",ans);
    }
	return 0;
}
