#include <bits/stdc++.h>
#define _CRT_SECURE_NO_DEPRECATE
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)

using namespace std;

typedef long long ll;
typedef pair<int, char> ii;
typedef pair<ll,ll> lii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef map<int, int> mii;
const int MAXN = 1000007;
const ll INF = 1e15;

    bool cmp(const ii &a,const ii &b){
        return a.first > b.first;
    }

priority_queue < int > Q;

bool pr[MAXN];
vector<int> primes;
vector <vector<ll> > K;
void sieve(){
    REP(i,2,1000000){
        if(!pr[i]){
            primes.push_back(i);
            for(int j = i+i;j <= 1000000;j += i){
                pr[j] = 1;
            }
        }
    }
}

int arr[103][103],n;
ll dist[103],speed[103];
double dp[103];

double solve(int pos,int dis,int spd){
    if(pos == n)return 0;
    double ans;
    if(dp[pos] >= 0)ans = dp[pos];
    else{
        ans = 1e15;
    }
    if(dis < arr[pos][pos+1]){
        return ans;
    }
    //if(pos == 2)cerr<<ans<<endl;
    double temp = (arr[pos][pos+1])*1.0/spd;
    ans = min(ans,temp + solve(pos+1,dis - arr[pos][pos+1],spd));
    return ans;
}


int main(){
    ios_base::sync_with_stdio(0);
    
    int t;
    cin>>t;

    for(int tc = 1;tc <= t;tc++){

        int q,u,v;
        cin>>n>>q;

        REP(i,1,n){
            cin>>dist[i]>>speed[i];
        }

        REP(i,1,n){
            REP(j,1,n){
                cin>>arr[i][j];
            }
        }
        memset(dp,-1,sizeof(dp));
        dp[n] = 0;
        for(int i = n-1;i > 0;i--){
            if(arr[i][i+1]  >  dist[i])continue;
            double temp = (arr[i][i+1])*1.0/speed[i];
            //cerr<<i<<' '<<temp<<endl;
            dp[i] = temp + solve(i+1,dist[i] - arr[i][i+1],speed[i]);
        }
        while(q--){
            cin>>u>>v;
            printf("Case #%d: %.9lf\n",tc,dp[1]);
        }
        //cout<<"Case #"<<tc<<": "<<ans<<"\n";
    }

    return 0;
}