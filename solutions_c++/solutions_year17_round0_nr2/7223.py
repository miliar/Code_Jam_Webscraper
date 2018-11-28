#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void io(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cout.precision(15);
}
vector<int> numtovec(long long n){
    vector<int> ret ;
    ret.clear() ;
    if(n == 0){
        ret.push_back(0) ;
    }
    while(n){
        ret.push_back(n%10ll) ;
        n /= 10ll ;
    }
    reverse(ret.begin(), ret.end()) ;
    return ret ;
}
long long vectonum(vector<int>& d){
    long long ret = 0 ;
    for(auto dig:d){
        ret = ret*10ll + dig ;
    }
    return ret ;
}
bool checkvec(vector<int>& d){
    for(int i = 0 ; i < d.size() - 1 ; i++){
        if(d[i] > d[i+1]){
            return 0 ;
        }
    }
    return 1 ;
}
void solve(long long n){
    vector<int> d = numtovec(n) ;
    if(checkvec(d)){
        cout << n << endl ;
        return ;
    }
    int sz = d.size() ;
    d[sz - 1] = 9 ;
    for(int i = sz - 2 ; i >= 0 ; i--){
        if(d[i] > 0){
            d[i]-- ;
        }
        if(checkvec(d)){
            cout << vectonum(d) << endl ;
            return ;
        }
        d[i] = 9 ;
    }
}
int main(int argc,char* argv[]) { 
    io() ;
    #ifndef ONLINE_JUDGE
        freopen("B-large (2).in", "r", stdin) ;
        freopen("B.txt", "w", stdout);
    #endif
    int tc = 0 ;
    int t; 
    cin >> t ;
    long long n ;
    while(t--){
        tc++ ;
        cout << "Case #" << tc << ": " ;
        cin >> n ;
        if(1 <= n && n <= 9){
            cout << n << endl ;
            continue ;
        }
        solve(n) ;
    }
    return 0 ; 
}