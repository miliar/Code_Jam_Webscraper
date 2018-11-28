#include <iostream>
#include <string>
using namespace std;

void solve(const int &tc) {
    int k;
    string a;
    cin >> a >> k;
    int ans = 0;
    for(int i=0;i<=a.length()-k;i++) {
        if(a[i] == '-') {
            for(int j=i;j<i+k;j++) {
                a[j] = a[j] == '+' ? '-' : '+';
            }
            ans++;
        }
    }
    if(all_of(a.begin(),a.end(),[](char x) {return x=='+';})) {
        printf("Case #%d: %d\n",tc,ans);
    } else printf("Case #%d: IMPOSSIBLE\n",tc);
}

int main() {
    int t; cin >> t;
    for(int i=1;i<=t;i++) solve(i);
}

