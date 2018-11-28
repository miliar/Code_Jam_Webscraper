#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <iomanip>
#include <functional>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;


typedef long long lint, ll;
typedef long double ldouble, ld;

#ifdef LOCAL
	#define dbg(expr) cerr << "[" << __LINE__ << "] " << #expr << " = " << (expr) << '\n';
#else
	#define dbg(expr) (void) 0;
#endif


bool is_problem(int number, int place, const vector<int> & number_by_place) {
    int s = 0;
    for (int i = place + 1; i < (int)number_by_place.size(); i++) {
        s += number_by_place[i];
        if (s >= number)
            return false;
    }
    return s < number;
}

void solve(int test_number) {
    int n, c, tickets_number;
    cin >> n >> c >> tickets_number;
    vector<pair<int, int>> tickets;
    vector<deque<int>> by_passenger(c);
    vector<vector<int>> number_by_place(2);
    for (int i = 0; i < 2; i++)
        number_by_place[i].resize(n);
    for (int i = 0; i < tickets_number; i++) {
        int place, id;
        cin >> place >> id;
        place--;
        id--;
        tickets.emplace_back(place, id);
        by_passenger[id].push_back(place);
        number_by_place[id][place]++;
    }
    for (int i = 0; i < c; i++)
        sort(by_passenger[i].begin(), by_passenger[i].end());
    cout << "Case #" << test_number + 1 << ": ";
    int tours_number = 0, promotions = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < c; j++) {
            int cnt = 0;
            for (int k = 0; k < number_by_place[j][i]; k++) {
                int ind = -1;
                int not_zero = -1;
                for (int place = i + 1; place < n; place++) {
                    if (is_problem(number_by_place[j ^ 1][place], place, number_by_place[j])) {
                        ind = place;
                        break;
                    }
                    if (number_by_place[j ^ 1][place] > 0 && not_zero == -1)
                        not_zero = place;
                }
                if (ind != -1) {
                    number_by_place[j ^ 1][ind]--;
                    tours_number++;
                    cnt++;
                } else if (not_zero != -1) {
                    number_by_place[j ^ 1][not_zero]--;
                    tours_number++;
                    cnt++;
                } else
                    break;
            }
            number_by_place[j][i] -= cnt;
        }
        //cerr << '*' << number_by_place[0][i] << ' ' << number_by_place[1][i] << endl;
        if (i != 0) {
            tours_number += max(number_by_place[0][i], number_by_place[1][i]);
            promotions += min(number_by_place[0][i], number_by_place[1][i]);
        } else
            tours_number += number_by_place[0][i] + number_by_place[1][i];
        number_by_place[0][i] = 0;
        number_by_place[1][i] = 0;
    }
    cout << tours_number << ' ' << promotions << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
