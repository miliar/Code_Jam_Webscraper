#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,p,g,c[5],ans;
    cin >> n >> p;
    memset(c,0,sizeof c);
    for(int i=1; i<=n; i++){
        cin >> g;
        c[g%p]++;
    }
    ans = c[0];
    if(p==2){
        if(c[1]>0){
            ans += (c[1]-1)/2+1;
        }
    }
    else if(p==3){
        int m = min(c[1],c[2]);
        ans += m;
        c[1] -= m;
        c[2] -= m;
        if(c[1]>0){
            ans += (c[1]-1)/3+1;
        }
        if(c[2]>0){
            ans += (c[2]-1)/3+1;
        }
    }
    else if(p==4){
        int m = min(c[1],c[3]);
        ans += m;
        c[1] -= m;
        c[3] -= m;
        ans += c[2]/2;
        int t = c[1]+c[3];
        if(c[2]%2){
            ans++;
            t-=2;
        }
        if(t>0){
            ans += (t-1)/4+1;
        }
    }
    cout << ans;
}

int main(){
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
