#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define MOD (1000000000000007LL)
#define LL long long

#define sqr(x) ((x) * (x))
#define Nmax 113

inline void test_out() {
    static int test_id = 0;
    test_id ++;
    cout << "Case #" << test_id << ": ";
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("answer.txt", "w", stdout);

    int test_number;
    cin >> test_number;
    while (test_number --> 0) {
        int n;
        cin >> n;
        int r,o,y,g,b,v;
        cin >> r >> o >> y >> g >> b >> v;
        set<pair<int, char> > s;

        //int n = r + b + y;
        map<char, int> let;
        let['R'] = r, let['Y'] = y, let['B'] = b;

        string res = "";

        if (b > 0) res += 'B';
        else if (r > 0) res += 'R'; else res += 'Y';
        let[res[0]] --;

        if (let['R'] > 0) s.insert(make_pair(-let['R'], 'R'));
        if (let['Y'] > 0) s.insert(make_pair(-let['Y'], 'Y'));
        if (let['B'] > 0) s.insert(make_pair(-let['B'], 'B'));

        test_out();
        //cerr<<"RRRR";
        while (!s.empty()) {
            char prev = res.back();
            //cerr << prev << endl;
            if (let[prev] > 0) {
                s.erase(s.find(make_pair(-let[prev], prev)));
            }
            if (s.size() == 0) {
                cout << "IMPOSSIBLE\n";
                break;
            }

            char letter = (*s.begin()).second;
            //cerr << letter << endl;
            s.erase(s.begin());
            res += letter;
            let[letter] --;
            if (let[letter] > 0)
                s.insert(make_pair(-let[letter], letter));
            if (let[prev] > 0)
                s.insert(make_pair(-let[prev], prev));

            //cerr << let['R'] << " " << let['Y'] << " " << let['B'] << " " << res.size() << endl;
        }
        if (res.size() == n) {
            if (res[0] == res[res.size() - 1])
                cout << "IMPOSSIBLE\n";
            else
                cout << res << endl;
        }
    }
    return 0;
}
