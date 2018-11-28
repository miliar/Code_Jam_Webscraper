// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

bool can_ride(int N, int C, const vector< vector<int> > &tickets, int rides) {
    //cout << "can_ride " << N << " " << C << " @ " << rides << endl;
    int current_seat = 0, seats_left = rides;
    for (int seat=0; seat<N; ++seat) {
        for (int c=0; c<C; ++c) {
            if (tickets[c][seat] == 0) continue;

            if (seat < current_seat) return false;
            if (seat == current_seat && seats_left < tickets[c][seat]) return false;
            if (seats_left >= tickets[c][seat]) {
                seats_left -= tickets[c][seat];
            } else {
                int remains = tickets[c][seat] - seats_left;
                ++current_seat;
                seats_left = rides;
                if (seat < current_seat) return false;
                if (seat == current_seat && seats_left < remains) return false;
                seats_left -= remains;
            }
        }
    }
    //cout << "can_ride " << N << " " << C << " @ " << rides << " true" << endl;
    return true;
}

int min_prom(int N, int C, const vector< vector<int> > &tickets, int rides) {
    int answer = 0;
    for (int n=0; n<N; ++n) {
        int desired = 0;
        for (int c=0; c<C; ++c) desired += tickets[c][n];
        if (desired > rides) answer += desired - rides;
    }
    return answer;
}

int main() {
    int T; cin >> T;
    for (int t=1; t<=T; ++t) {
        int N, C, M;
        cin >> N >> C >> M;
        vector< vector<int> > tickets(C, vector<int>(N,0) );
        for (int m=0; m<M; ++m) {
            int p, b;
            cin >> p >> b;
            --p; --b;
            ++tickets[b][p];
        }
        int lo = max( accumulate( tickets[0].begin(), tickets[0].end(), 0 ), accumulate( tickets[1].begin(), tickets[1].end(), 0 ) ) - 1;
        int hi = M;
        // lo nestaci, hi staci
        while (hi - lo > 1) {
            int med = (lo+hi) / 2;
            if (can_ride(N,C,tickets,med)) hi = med; else lo = med;
        }
        cout << "Case #" << t << ": " << hi << " " << min_prom(N,C,tickets,hi) << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
