#include <bits/stdc++.h>
#define _CRT_SECURE_NO_DEPRECATE
#define REP(i, a, b) for (int i = int(a); i <= int(b); i++)

using namespace std;

typedef long long ll;
typedef pair<int, char> ii;
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

ii arr[3];

int main(){
    ios_base::sync_with_stdio(0);
    
    int t;
    cin>>t;

    for(int tc = 1;tc <= t;tc++){

        int n,r,o,y,g,b,v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        string ans = "";
        REP(i,1,n)ans += '$';
        if(r > n/2 || y > n/2 || b > n/2){
            cout<<"Case #"<<tc<<": IMPOSSIBLE\n";
            continue;
        }
        arr[0] = ii(r,'R');
        arr[1] = ii(y,'Y');
        arr[2] = ii(b,'B');
        sort(arr,arr+3,cmp);
        int cnt = arr[0].first;
        for(int i= 0;i < n;i += 2){
            if(cnt == 0)break;
            ans[i] = arr[0].second;
            cnt--;
        }
        for(int i = 0;i < n;i++){
            if(ans[i] == '$'){
                if(ans[i-1] == arr[1].second){
                    ans[i] = arr[2].second;
                    arr[2].first--;
                }
                else if(ans[i-1] == arr[2].second){
                    ans[i] = arr[1].second;
                    arr[1].first--;
                }
                else{
                    if(arr[1].first > arr[2].first){
                        ans[i] = arr[1].second;
                        arr[1].first--;
                    }
                    else{
                        ans[i] = arr[2].second;
                        arr[2].first--;
                    }
                }
            }
        }
        cout<<"Case #"<<tc<<": "<<ans<<"\n";
        //cout<<"Case #"<<tc<<": "<<ans<<"\n";
    }

    return 0;
}