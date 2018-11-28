#include <bits/stdc++.h>

using namespace std;

const int N = 55;
int a[N][N];
int r[N];
int cp[N];
int ll[N];
int rr[N];

int n,p;

int valid() {
    for(int i = 1;i <= n;i++)
        if(cp[i] > p) return 0;
    return 1;
}

void solve() {
    cin>>n>>p;
    for(int i = 1;i <= n;i++) {
        cin>>r[i];
    }
    for(int i = 1;i <= n;i++) {
        for(int j = 1;j <= p;j++) {
            cin>>a[i][j];
        }
        sort(a[i]+1,a[i]+1+p);
        cp[i] = 1;
    }
    int ans = 0;
    while(valid()) {
        int mx = -1,mn = -1;
        int flag = 0;
        for(int i = 1;i <= n;i++) {
            ll[i] = -1,rr[i] = -1;
            for(int j = 1;0.9 * j * r[i] <= a[i][cp[i]];j++) {
                if(1.1 * j * r[i] >= a[i][cp[i]]) {
                    if(ll[i] == -1)
                        ll[i] = j;
                    rr[i] = j;
                }
            }
            if(ll[i] == -1) {
                flag = 1;
                cp[i]++;
                break;
            }
            if(mx == -1 || ll[i] > mx)
                mx = ll[i];
            if(mn == -1 || rr[i] < mn)
                mn = rr[i];
        }
        if(flag)
            continue;
        if(mx <= mn) {
            ans++;
            for(int i = 1;i <= n;i++)
                cp[i]++;
        }
        else {
            for(int i = 1;i <= n;i++) {
                if(rr[i] == mn)
                    cp[i]++;
            }
        }
    }
    cout<<ans<<endl;


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
