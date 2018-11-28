#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
using namespace std;



void solve(int t) {

    ll x, n;
    cin>>x;
    n = x;
    vector<int>v;
    while(n > 0) {
        v.push_back(n%10);
        n/=10;
    }
    reverse(v.begin(), v.end());
    
    int flag=1;
    
    while (true) {
        int flag = 1;
        for(int i=1; i<v.size(); i++) {
            if (v[i] < v[i-1]) {
                v[i-1]--;
                for(int j = i; j<v.size(); j++) {
                    v[j] = 9;
                }
                flag = 0;
                break;
            }
        }

        if (flag == 1) {
            break;
        }
    }

    ll ans = 0;
    for(int i=0; i<v.size(); i++) {
        ans = ans*10 + v[i];
    }


//*

    cout<<"Case #"<<t<<": "<<ans<<endl;
    
    //*/
}


int main() {
    //A-small-attempt0 (1).in
    freopen("B-large (1).in", "r", stdin); freopen("output.txt", "w", stdout);

    int tc = 1;
    cin>>tc;
    
    for(int t=1; t<=tc; t++) {
        solve(t);
    }

}