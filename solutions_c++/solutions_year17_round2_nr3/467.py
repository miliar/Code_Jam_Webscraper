#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <set>
#include <string>
using namespace std;
typedef long long ll;

#define MOD 1000000007ll
#define oo 1000000000007ll
#define PI 3.141592653589793238462643
#define MAXN 30
#define TT 61

ll gcd(ll a,ll b){
    if(!a) return b;
    return gcd(b%a, a);
}
pair<ll, ll> extended_gcd(ll a, ll b) {
    if (b == 0) return make_pair(1, 0);
    pair<ll, ll> t = extended_gcd(b, a % b);
    return make_pair(t.second, t.first - t.second * (a / b));
}
ll modinverse(ll a, ll m) {
    return (extended_gcd(a, m).first % m + m) % m;
}

bool isPrime(int X){
    if(X==1) return true;
    for(int i=2;i*i<=X;i++){
        if(X%i==0) return false;
    }
    return true;
}

int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        
        double anss[101];
        ll E[101],S[101];
        ll mm[101][101];
        int N,Q;
        cin >> N >> Q;
        for(int i=0;i<N;i++){
            scanf("%lld%lld",&E[i],&S[i]);
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                scanf("%lld",&mm[i][j]);
                if(mm[i][j] == -1) mm[i][j] = oo;
            }
        }
        for(int k=0;k<N;k++){
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if(mm[i][j] > mm[i][k] + mm[k][j]) {
                        mm[i][j] = mm[i][k] + mm[k][j];
                    }
                }
            }
        }
        for(int q=0;q<Q;q++){
            int start, end;
            cin >> start >> end;
            start --, end--;
            priority_queue<pair<double,int>, vector<pair<double,int>>, greater<pair<double,int>>> que;
            que.push(make_pair(0,start));
            
            double diss[101];
            for(int i=0;i<N;i++) diss[i] = oo;
            diss[start] = 0;
            while(!que.empty()){
                double dis = que.top().first;
                int now = que.top().second;
                que.pop();
                
                for(int i=0;i<N;i++){
                    if(mm[now][i] <= E[now] && diss[i] > dis + (1.0/S[now]) * mm[now][i]){
                        diss[i] = dis + (1.0/S[now]) * mm[now][i];
                        que.push(make_pair(dis + (1.0/S[now]) * mm[now][i], i));
                    }
                }
            }
            anss[q] = diss[end];
        }
        
        printf("Case #%d: ",t);
        for(int i=0;i<Q;i++) printf("%.7lf ",anss[i]);
        cout << endl;
        
    }
    
    
    return 0;
}

