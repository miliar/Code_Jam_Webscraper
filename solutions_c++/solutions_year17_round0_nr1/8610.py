#include <iostream>
#include <string>
using namespace std;

int t, k, x = 1, y, z;
string s;

// if you can flip, this returns x( >= 0). if not, returns -1.
int solve() {
    string::size_type index = s.find("-");
    int ret = 0, pre = -1;

    while (index != string::npos) {
        //cin >> z;
        //cout << s << endl;
        if (pre > (int)index) {
           ret = -1;
           break; 
        }

        if (s.size() - (int)index < k) {
            ret = -1;
            break;
        }

        for (int i = (int)index; i < (int)index + k; ++i) {
            if (s[i] == '-') {
                s[i] = '+';
            }
            else {
                s[i] = '-';
            }
        }

        ret++;
        pre = (int)index;
        index = s.find("-");
    }

    //cout << "terminated\n";

    return ret;
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> t;

    while (t--) {
        cin >> s >> k;

        y = solve();

        if (y != -1) cout << "Case #" << x << ": " << y << "\n";
        else cout << "Case #" << x << ": IMPOSSIBLE\n"; 

        x++;
    }

    return 0;
}