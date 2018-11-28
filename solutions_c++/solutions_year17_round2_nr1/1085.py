#include <bits/stdc++.h>
#define _CRT_SECURE_NO_DEPRECATE
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)

using namespace std;

typedef long long ll;
typedef pair<ll, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef map<int, int> mii;
const int MAXN = 1000007;
const ll INF = 1e15;

struct cmp{
    bool operator()(const ii &a,const ii &b){
        return a.second < b.second;
    }
};
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

int arr[1003][1003],cost[1003][1003];

int main(){
    ios_base::sync_with_stdio(0);
    
    int t;
    cin>>t;

    for(int tc = 1;tc <= t;tc++){

        ll d,n,x,s;
        double ans = 0;
        cin>>d>>n;
        while(n--){
            cin>>x>>s;
            ans = max(ans,(d-x)*1.0/s);
        }
        ans = d*1.0/ans;
        printf("Case #%d: %.9lf\n",tc,ans);
        //cout<<"Case #"<<tc<<": "<<ans<<"\n";
    }

    return 0;
}