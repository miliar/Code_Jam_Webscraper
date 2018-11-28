#include<bits/stdc++.h>
#define __SUBMIT__ ios_base::sync_with_stdio(0); \
                   cin.tie(0);
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int MOD = 1e9 + 7;
const int MAX = 1e9;

int main()
{
    __SUBMIT__
    //freopen("in.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int TC; cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
        ll x; cin >> x;
        stringstream ss;
        ss << x;
        string s;
        s = ss.str();
        for (int i=s.size()-1; i>0; i--) {
            if (s[i-1] > s[i]) {
                s[i-1]--;
                for (int j=i; j<s.size(); j++) {
                    s[j] = '9';
                }
            }
        }
        for (int i=0; i<s.size(); i++) {
            if (s[i] != '0') {
                s = s.substr(i);
                break;
            }
        }
        cout << "Case #" << tc << ": " << s << "\n";
    }
}
