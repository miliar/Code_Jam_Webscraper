#include <bits/stdc++.h>
using namespace std;
inline void solve();
int main() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
    int t,i=0;
    cin >> t;

    while (i<t) {
        cout<<"Case #"<<i+1<<": ";
        solve();
        cout<<endl;
        i++;
    }
    return 0;
}




#define int long long

const int ost =1e9+7;
/*bool f(int n){
    string s=to_string(n);
    for(int i=0;i<s.size()-1;i++){
        if(s[i]>s[i+1])
            return false;
    }
    return true;
}*/
inline void solve() {
    int n;
    cin>>n;
    string s =to_string(n);
/*
    while(!f(n)){
        n--;
    }
    cout<<n<<" ";
*/
    char ch[21]="01234567890123456789";
    bool t=false;
    for(int j=0;j<s.size();j++) {
        for (int i = s.size() - 1; i > 0; i--) {
            if (s[i - 1] > s[i]) {
                int a = s[i] - '0';
                while (s[i - 1] > ch[10 + a])
                    a--;
                s[i] = ch[10 + a];
                if(!t)
                    s[i - 1] -= 1;
            }
        }
        t=true;
        if(s[0]=='0')
            s.erase(s.begin());
    }
    cout<<s;
}





















