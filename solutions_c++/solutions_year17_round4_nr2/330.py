#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

int is_solvable(int rides, const vector<vector<int>>& seats, int n)
{
    vector<int> times_needed(n, 0);
    for (auto& v: seats) {
        for (int i: v) ++times_needed[i];
    }

    int possible_promotions = 0;
    int promotions = 0;
    for (int i: times_needed) {
        if (i > rides) {
            if (i <= rides + possible_promotions) {
                promotions += (i - rides);
            } else {
                return -1; // too few rides
            }
        }
        possible_promotions += (rides - i);
    }

    return promotions;
}

void solve(int)
{
    int n, c, m;
    cin >> n >> c >> m;
    vector<vector<int>> seats(c);
    for (int i = 0; i < m; ++i) {
        int p, b;
        cin >> p >> b;
        --p; --b;
        seats[b].push_back(p);
    }

    size_t min_rides = 0;
    for (auto& v: seats) min_rides = max(min_rides, v.size());

    size_t max_rides = m + 5;

    while (min_rides < max_rides) {
        int mm = (max_rides + min_rides) / 2;
        bool b = is_solvable(mm, seats, n) != -1;
        if (b) {
            max_rides = mm;
        } else {
            min_rides = mm + 1;
        }
    }
    assert(max_rides == min_rides);

    cout << min_rides << " " << is_solvable(min_rides, seats, n) << endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
