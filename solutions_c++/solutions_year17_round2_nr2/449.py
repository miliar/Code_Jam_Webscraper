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
#define oo 1000000007ll
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
        
        string res = "";
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        int ans = 1;
        if(R > Y + B || Y > R + B || B > R + Y) {
            ans = -1;
        }
        pair<int, char> C[3];
        C[0] = make_pair(R, 'R');
        C[1] = make_pair(Y, 'Y');
        C[2] = make_pair(B, 'B');
        
        sort(C, C+3);
        
        int to = 0;
        int cnt = 0;
        
        for(int i=0;i<C[2].first;i++){
            res += C[2].second;
            if(to) {
                if(C[1].first){
                    res += C[1].second;
                    C[1].first -= 1;
                } else {
                    res += C[0].second;
                    C[0].first -= 1;
                }
            } else {
                if(C[0].first){
                    res += C[0].second;
                    C[0].first -= 1;
                } else {
                    res += C[1].second;
                    C[1].first -= 1;
                    
                }
            }
            to = !to;
        }
        int ttt = C[0].first;
        for(int i=0;i<ttt;i++){
            if(res[res.size()-1] != C[1].second) {
                res += C[1].second;
                res += C[0].second;
            } else {
                res += C[0].second;
                res += C[1].second;
            }
            C[1].first --;
            C[0].first --;
        }
        if(C[1].first > 0){
            for(int i=0;i<C[1].first;i++){
                for(int j=0;j<res.size() - 1;j++){
                    if(res[j] != C[1].second && res[j+1] != C[1].second){
                        string temp = res;
                        res = "";
                        for(int k=0;k<=j;k++) res += temp[k];
                        res += C[1].second;
                        for(int k=j+1;k<temp.size();k++) res += temp[k];
                        break;
                    }
                }
            }
        }
        
        printf("Case #%d: ",t);
        if(ans < 0) res = "IMPOSSIBLE";
        cout << res << endl;
        
    }
    
    
    return 0;
}

