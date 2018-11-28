#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    int cas = 0;
    cin >> t;
    while( t-- ){
        string a;
        cin >> a;
        string ans;
        ans += a[a.size()-1];
        for( int i=a.size()-2 ; i>=0 ; i-- ){
            if( a[i]>ans[0] ){
                for( int i=0 ; i<=ans.size() ; i++ ) ans[i] = '9';
                ans = (char)(a[i]-1) + ans;
                a[i] -= 1;
            }
            else{
                ans = (char)(a[i])+ans;
            }
        }
        while(ans[0]=='0') ans.erase(ans.begin());
        printf("Case #%d: ", ++cas);
        cout << ans << endl;
    }
    return 0;
}