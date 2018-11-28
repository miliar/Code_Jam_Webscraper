#include <bits/stdc++.h>
using namespace std;
char enl = '\n';
#define rep(i, from, to) for (int i = from; i < (to); ++i)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<pair<int, int>> vii;

ull ten = 10;

string solve() {

    vector<ll> digits;
    ll n;
    cin >> n;
    ll on = n;
    while (n > 0) {
        digits.push_back((n%ten));
        n /= ten;
    }
    reverse(digits.begin(), digits.end());
    int s = digits.size();


    vector<ll> startdigits;
    ll samenum = -1;
    ll numsamenum = 0;

    rep(i,0,s) {
        if (samenum < digits[i]) {
            rep(j,0,numsamenum) {
                startdigits.push_back(samenum);
            }
            samenum = digits[i];
            numsamenum = 1;
        } else if (samenum == digits[i]) {
            numsamenum++;
        } else {
            string ans;
            if (samenum == 1) {
                rep(j,0,numsamenum-1) {
                    ans += "9";
                }
            } else {
                for (auto w : startdigits) {
                    ans += to_string(w);
                }
                if (numsamenum > 0) {
                    ans += to_string(samenum-1);
                }
                rep(j,0,numsamenum-1) {
                    ans += "9";
                }
            }
            rep(j,i,s) {
                ans += "9";
            }
            return ans;
        }
    }
    return to_string(on);
}




    
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin.exceptions(cin.failbit);

    int t;
    cin >> t;
    rep(i,0,t) {
        cout << "Case #" << (i+1) << ": " << solve() << endl;
    }


    return 0;
}
