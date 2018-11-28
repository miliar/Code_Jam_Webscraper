#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector < pair < int64_t , int64_t > > heap;

bool cmp(const pair<int64_t , int64_t>& a, const pair<int64_t, int64_t> &b) {
    return a.second - a.first < b.second - b.first;
}

int main()
{
    freopen("txt.in", "r", stdin);
    freopen("txt.out", "w", stdout);

    int t, n, k;

    cin >> t;
    for(int tst = 1; tst <= t; ++tst) {
        cin >> n >> k;

        heap.push_back({1 , n + 2});
        for(int i = 1; i < k; ++i) {
            auto interval = heap.front();
            pop_heap(heap.begin(), heap.end(), cmp);
            heap.pop_back();

            if(interval.second - interval.first == 2)
                continue;

            int64_t aux = (interval.second - interval.first) / 2;
            if((interval.second - interval.first + 1) % 2 == 1) {
                heap.push_back({interval.first , interval.first + aux});
                push_heap(heap.begin(), heap.end(), cmp);

                heap.push_back({interval.first + aux, interval.second});
                push_heap(heap.begin(), heap.end(), cmp);
            } else {
                heap.push_back({interval.first , interval.first + aux});
                push_heap(heap.begin(), heap.end(), cmp);

                heap.push_back({interval.first + aux, interval.second});
                push_heap(heap.begin(), heap.end(), cmp);
            }
        }
        auto fin = heap.front();
        int64_t midd = fin.first + (fin.second - fin.first) / 2;
        if((fin.second - fin.first + 1) % 2 == 1){
            cout << "CASE #" << tst << ": " << fin.second - midd - 1 << " " << fin.second - midd - 1 << "\n";
        } else {
            cout << "CASE #" << tst << ": " << fin.second - midd - 1 << " " << midd - fin.first - 1 << "\n";
        }

        heap.clear();
    }

    return 0;
}
