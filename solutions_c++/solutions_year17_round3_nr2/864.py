#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <cmath>
#include <functional>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;
typedef pair<int,int> pii;

const double PI = acos(-1);

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        int Ac, Aj;
        cin >> Ac >> Aj;
        vector<pii> CD(Ac);
        vector<pii> JK(Aj);
        REP (i, 0, Ac) cin >> CD[i].first >> CD[i].second;
        REP (i, 0, Aj) cin >> JK[i].first >> JK[i].second;
        int ans = 0;
        if (Ac + Aj == 1) ans = 2;
        else if (Ac == 1 && Aj == 1) ans = 2;
        else {
            vector<pii> data;
            if (Ac == 0) data = JK;
            else data = CD;
            sort(data.begin(), data.end());
            int temp = min(data[1].second - data[0].first , 1440 - data[1].first + data[0].second);
            if (temp <= 720) ans = 2;
            else ans = 4;
        }
        cout << "Case #" << _ + 1 << ": " << ans << endl;
    }
    return 0;
}
