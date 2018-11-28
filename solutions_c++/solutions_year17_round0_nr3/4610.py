#include <bits/stdc++.h>

using namespace std;

void solve() {
    long long n; cin>>n;
    long long k; cin>>k;
    long long a = n,b = n;
    map<long long,long long> cnt;
    cnt[n] = 1;
    long long cc = 1;
    while(cc < k) {
        k -= cc;
        cc <<= 1;
        if(a == b) {
            if(a % 2 == 0) {
                cnt[a/2 - 1] += cnt[a];
                cnt[a/2] += cnt[a];
                a = a/2 - 1;
                b = b/2;
            }
            else {
                cnt[a/2] += cnt[a] * 2;
                a = b = a/2;
            }
        }
        else {
            if(a % 2 == 0) {
                cnt[a/2 - 1] += cnt[a];
                cnt[a/2] += cnt[a];
            }
            else {
                cnt[a/2] += cnt[a] * 2;
            }
            if(b % 2 == 0) {
                cnt[b/2 - 1] += cnt[b];
                cnt[b/2] += cnt[b];
            }
            else {
                cnt[b/2] += cnt[b] * 2;
            }
            if(a % 2 == 1) {
                a = a/2;
                b = b/2;
            }
            else {
                a = a/2 - 1;
                b = b/2;
            }
        }
    }
    if(k <= cnt[b]) {
        if(b % 2 == 0) {
            cout<<b/2<<' '<<b/2 - 1<<endl;
        }
        else {
            cout<<b/2<<' '<<b/2<<endl;
        }
    }
    else {
        if(a % 2 == 0) {
            cout<<a/2<<' '<<a/2 - 1<<endl;
        }
        else {
            cout<<a/2<<' '<<a/2<<endl;
        }
    }
}

int main() {
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        cerr<<"Executing Case #"<<i<<endl;
        cout<<"Case #"<<i<<": ";
        solve();
    }

}
