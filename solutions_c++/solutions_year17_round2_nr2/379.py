#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n,r,o,y,g,b,v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    if(b<o || b==o && b>0 && b+o<n){
        cout << "IMPOSSIBLE";
        return;
    }
    if(y<v || y==v && y>0 && y+v<n){
        cout << "IMPOSSIBLE";
        return;
    }
    if(r<g || r==g && r>0 && r+g<n){
        cout << "IMPOSSIBLE";
        return;
    }
    if(b==o && b+o==n){
        for(int i=1; i<=b; i++){
            cout << "BO";
        }
        return;
    }
    if(y==v && y+v==n){
        for(int i=1; i<=y; i++){
            cout << "YV";
        }
        return;
    }
    if(r==g && r+g==n){
        for(int i=1; i<=r; i++){
            cout << "RG";
        }
        return;
    }
    b -= o;
    y -= v;
    r -= g;
    if(max({b,y,r})>b+y+r-max({b,y,r})){
        cout << "IMPOSSIBLE";
        return;
    }
    string t;
    if(max({b,y,r})==b){
        for(int i=1; i<=b; i++){
            t += 'B';
        }
        for(int i=1; i<=y; i++){
            t += 'Y';
        }
        for(int i=1; i<=r; i++){
            t += 'R';
        }
    }
    else if(max({b,y,r})==y){
        for(int i=1; i<=y; i++){
            t += 'Y';
        }
        for(int i=1; i<=r; i++){
            t += 'R';
        }
        for(int i=1; i<=b; i++){
            t += 'B';
        }
    }
    else{
        for(int i=1; i<=r; i++){
            t += 'R';
        }
        for(int i=1; i<=b; i++){
            t += 'B';
        }
        for(int i=1; i<=y; i++){
            t += 'Y';
        }
    }
    string tt;
    int cnt = t.size()/2;
    int shift = t.size()-cnt;
    for(int i=0; i<cnt; i++){
        tt += t[i];
        tt += t[shift+i];
    }
    if(t.size()%2){
        tt += t[cnt];
    }
    string ans;
    for(char c : tt){
        ans += c;
        if(c=='B' && o>0){
            while(o>0){
                cout << "OB";
                o--;
            }
        }
        if(c=='Y' && v>0){
            while(v>0){
                cout << "VY";
                v--;
            }
        }
        if(c=='R' && g>0){
            while(g>0){
                cout << "GR";
                g--;
            }
        }
    }
    cout << ans;
}

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    for(int c=1; c<=t; c++){
        cout << "Case #" << c << ": ";
        solve();
        cout << endl;
    }
}
