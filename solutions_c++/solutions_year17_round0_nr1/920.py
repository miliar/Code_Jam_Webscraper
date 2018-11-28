#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi, ll>
#define f first
#define s second
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define fre freopen("in.txt","r",stdin)
int cnt = 1;
void print(string s) {
    cout << "Case #"<<cnt<<": "<<s<<"\n";
    cnt++;
}
void print(int x) {
    cout << "Case #"<<cnt<<": "<<x<<"\n";
    cnt++;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    while(t--) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        rep(i,s.size()) {

            if(i+k-1 < s.size()) {
                if(s[i]=='-') {
                    for(int j=i;j<=i+k-1;j++) s[j] = (s[j]=='-'?'+':'-');
                    ans++;
                }
            }
            if(s[i]=='-') ans = -1;
        }
        if(ans == -1) {
            print("IMPOSSIBLE");
        }
        else{
            print(ans);
        }
    }
}
