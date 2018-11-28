#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

/**
 * If there is only one seat, then we need M rides.
 * If there are two seats, we count the number of 1 tickets, and number of 2 tickets.
 * We need c1 rides at least to accommodate those 1 tickets. For the remaining of the 2 tickets...
 * We can promote half of them.
 * However, this is possible ONLY if those were not the same customer.
 * If the same customer bought all M tickets, we need M rides.
 * Let's say there is no promotion, how many rides are needed?
 * Is this a greedy?
 */

multiset<int> customers[1024];
int ticket_counts[1024];
int main() {
    int num_cases;
    cin >> num_cases;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        int N, C, M;
        cin >> N >> C >> M;
        // Conjecture...
        // The number of rides R... must satisfy certain things.
        for (int i = 0; i < C; ++i) {
            customers[i].clear();
        }
        for (int i = 0; i < N; ++i) ticket_counts[i] = 0;
        for (int i = 0; i < M; ++i) {
            int p, b;
            cin >> p >> b;
            --p; --b;
            customers[b].insert(p);
            ++ticket_counts[p];
        }
        int R = 0;
        for (int i = 0; i < C; ++i) {
            if (customers[i].size() > R) R = customers[i].size();
        }
        int acc = 0;
        for (int i = 0; i < N; ++i) {
            acc += ticket_counts[i];
            if ((i + 1) * R < acc) {
                R = (acc + i) / (i + 1);
            }
        }

        int promotions = 0;
        for (int i = 0; i < N; ++i) {
            if (ticket_counts[i] > R) promotions += ticket_counts[i] - R;
        }
        // This should be the minimal R we can do.
        cout << "Case #" << case_index << ": " << R << ' ' << promotions << endl;
    }
    return 0;
}
