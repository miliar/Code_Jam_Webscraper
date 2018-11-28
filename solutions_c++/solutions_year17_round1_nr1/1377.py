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

string mm[30];

bool isIn(vector<char> v, char c){
    for(int i=0;i<v.size();i++){
        if(v[i] == c) return true;
        
    }
    return false;
}
void fill(int x1,int y1,int x2,int y2){
    vector<char> v,a,b;
    for(int i=x1;i<x2;i++){
        for(int j=y1;j<y2;j++){
            if(mm[i][j] != '?' && !isIn(v,mm[i][j])){
                v.push_back(mm[i][j]);
            }
        }
    }
    if(v.size() == 1){
        for(int i=x1;i<x2;i++){
            for(int j=y1;j<y2;j++){
                mm[i][j] = v[0];
            }
        }
        return;
    }
    // ---
    for(int i=x1;i<x2;i++){
        for(int j=y1;j<y2;j++){
            if(mm[i][j] != '?' && !isIn(a,mm[i][j])){
                a.push_back(mm[i][j]);
            }
        }
        if(a.size() > 0 && a.size() != v.size()) {
            fill(x1,y1,i+1,y2);
            fill(i+1,y1,x2,y2);
            return;
        }
    }
    
    // |
    
    for(int j=y1;j<y2;j++){
        for(int i=x1;i<x2;i++){
            if(mm[i][j] != '?' && !isIn(b,mm[i][j])){
                b.push_back(mm[i][j]);
            }
        }
        if(b.size() > 0 && b.size() != v.size()) {
            fill(x1,y1,x2,j+1);
            fill(x1,j+1,x2,y2);
            return;
        }
    }
}
int main(){
    
    int T;
    
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++){
        
        int N,M;
        cin >> N >> M;
        for(int i=0;i<N;i++){
            cin >> mm[i];
        }
        
        fill(0,0,N,M);
        
        printf("Case #%d:\n",t);
        for(int i=0;i<N;i++){
            cout << mm[i] << endl;
        }
    }
    
    
    return 0;
}

