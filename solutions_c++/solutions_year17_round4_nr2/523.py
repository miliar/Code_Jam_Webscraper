#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define PRECISION 8

struct Ticket {
    int pos, id, cnt;
    bool operator< (const Ticket & ticket) const {
        if (pos != ticket.pos)
            return pos < ticket.pos;
        return id < ticket.id;
    }
};

struct Train {
    int firstFree = 0;
    int seatsCount = 0;
    vector < bool > places;
    bool isFull() {
        return firstFree == seatsCount;
    }
    void increase() {
        while (!isFull() && places[firstFree]) {
            ++firstFree;
        }
    }
    int getNext() {
        if (places[firstFree]) {
            increase();
        }
        return firstFree;
    }
};

void solve() {
    int n, c, m;
    cin >> n >> c >> m;
    vector < Ticket > tickets(m);
    vector <int> cust(c, 0);
    for (int i = 0; i < m; ++i) {
        cin >> tickets[i].pos >> tickets[i].id;
        tickets[i].pos -= 1;
        tickets[i].id -= 1;
        cust[tickets[i].id] += 1;
    }
    for (int i = 0; i < m; ++i) {
        tickets[i].cnt = cust[tickets[i].id];
    }
    sort(tickets.begin(), tickets.end());
    int minTrainsCount = *max_element(cust.begin(), cust.end()), maxTrainsCount = m + 1;
    int minPromotions = 0;
    while (minTrainsCount < maxTrainsCount) {
        int trainsCount = (minTrainsCount + maxTrainsCount) / 2;
        bool possible = true;
        vector < Train > trains(trainsCount);
        for (auto & train : trains) {
            train.seatsCount = n;
            train.places = vector <bool>(n, false);
        }
        int promotions = 0;

        for (const auto & ticket : tickets) {
            bool hold = false;
            for (int i = 0; i < trainsCount && !hold; ++i) {
                if (!trains[i].places[ticket.pos]) {
                    hold = true;
                    trains[i].places[ticket.pos] = true;
                }
            }
            if (!hold) {
                for (int i = 0; i < trainsCount && !hold; ++i) {
                    int place = trains[i].getNext();
                    if (!trains[i].isFull() && place <= ticket.pos) {
                        trains[i].places[place] = true;
                        hold = true;
                        promotions += 1;
                    }
                }
            }
            if (!hold) {
                possible = false;
                break;
            }
        }

        if (possible) {
            maxTrainsCount = trainsCount;
            minPromotions = promotions;
        } else {
            minTrainsCount = trainsCount + 1;
        }

    }
    cout << maxTrainsCount << " " << minPromotions;

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifdef FALSE
    cout << setprecision(PRECISION) << std::fixed;
#endif
    int numberOfTestCases;
    cin >> numberOfTestCases;
    for (int testCase = 1; testCase <= numberOfTestCases; ++testCase) {
        cout << "Case #" << testCase << ": ";
        if (testCase == 82) {
            int stop = 1;
        }
        solve();
        cout << endl;
    }
    return 0;
}