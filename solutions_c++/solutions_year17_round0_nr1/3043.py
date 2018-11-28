#include <bits/stdc++.h>
using namespace std;

int bad = 1e5;

int getcount (int m) {
    int ret = 0;
    while (m>0) {
        ret += m%2;
        m/=2;
    }
    return ret;
}

string fliprange(string s, int i, int j) {
    for (int k=i; k<=j; k++) {
        if ( s[k] == '+' ) s[k] = '-';
        else s[k] = '+';
    }
    return s;
}

int dumsolve (string s, int k) {

    int ans = bad;
    int dif = s.size()-k+1;
    //cout << "dif : " << dif << endl;
    for (int m=0; m< (1 << dif ); m++ ) {
        int cc = getcount(m);
        string x = string( s.size() , '+' );
        //cout << m << " " << x << " ";
        for (int i=0; i<dif; i++) {
            if ( m&(1<<i) ) {
                x = fliprange(x,i,i+k-1);
            }
        }

        //cout << x << endl;

        if (x==s) {
            ans = min(ans, cc);
            //cout << "here!" << endl;
        }
    }

    return ans;
}

int solve (string s, int k) {

    int dif = s.size()-k+1 , ans = 0;
    for (int i=0; i<dif; i++) {
        if ( s[i] == '-' ) {
            ans++;
            s = fliprange(s,i,i+k-1);
        }
    }

    int sz = s.size();
    for (int i=dif; i<sz; i++) {
        if ( s[i] == '-' ) return bad;
    }

    return ans;
}

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas = 1; cas <= t; cas++) {
        string s; int k;
        cin >> s >> k;

        int ans = solve(s,k);
        if ( ans == bad ) {
            cout << "Case #" << cas << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << cas << ": " << ans << endl;
        }
    }
}
