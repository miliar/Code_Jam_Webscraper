#include <cstdlib>
#include <cstring>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long LL;

int N, R, O, Y, G, B, V;
//char n = 'N', r = 'R', o = 'O', y = 'Y', g = 'G', b = 'B', v = 'V';

typedef std::pair<int, char> IC;
std::vector<IC> input;

void small() {
    sort(input.begin(), input.end(), std::greater<IC>());
    if (input[1].first + input[2].first < input[0].first) {
        cout << " IMPOSSIBLE" << endl;
        return;
    }

    list<char> l;
    for (int i = 0; i < input[1].first; i ++) {
        l.push_back(input[0].second);
        l.push_back(input[1].second);
    }
    input[0].first -= input[1].first;

    for (int i = 0; i < input[0].first; i ++) {
        l.push_back(input[0].second);
        l.push_back(input[2].second);
    }

    auto it = l.begin(); it ++;
    input[2].first -= input[0].first;
    for (int i = 0; i < input[2].first; i ++) {
        l.insert(it, input[2].second);
        it ++; it ++;
    }

    cout << ' ';
    for (auto x : l) cout << x;
    cout << endl;
}

void work() {
    cin >> N >> R >> O >> Y >> G >> B >> V;
    input.clear();
    input.push_back(IC(R, 'R'));
    input.push_back(IC(O, 'O'));
    input.push_back(IC(Y, 'Y'));
    input.push_back(IC(G, 'G'));
    input.push_back(IC(B, 'B'));
    input.push_back(IC(V, 'V'));

    small();
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        work();
    }
    return 0;
}
