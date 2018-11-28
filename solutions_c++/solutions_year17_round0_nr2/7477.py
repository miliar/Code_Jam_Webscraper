#include <bits/stdc++.h>

using namespace std;

const int maxn = 1e6 + 1;
int ans[maxn];

bool f(int x){
    int prev = 11;
    while(x > 0){
        if(x%10 > prev)
            return false;
        prev = x%10;
        x = x/10;
    }
    return true;
}

void pre(){
    int _min = 0,val;
    for(int i = 1;i <= maxn; i++){
        if(f(i)){
            ans[i] = i;
        }
        else
            ans [i] = ans[i-1];
        if(i - ans[i] > _min){
            _min = i - ans[i];
            val = i;
        }
    }
    //cerr << _min << " " << val << " "<< ans[val] <<endl;
}

void solve() {
    int n;
    cin >> n;
    cout << ans[n] << endl;
}

int main() {
    pre();
    assert(freopen("./input.txt","r",stdin));
    assert(freopen("./output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": ";
        solve();
    }

}
