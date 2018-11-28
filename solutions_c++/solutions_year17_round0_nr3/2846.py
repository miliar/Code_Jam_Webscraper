/**
 * http://code.google.com/codejam/contest/3264486/dashboard#s=p2
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct interval
{
    ll size;
    ll count;
    interval(ll s = 0, ll c = 0) : size(s), count(c) {}
};

void unify_intervals(deque<interval>& i)
{
    sort(i.begin(), i.end(), [](const interval& l, const interval& r) { return l.size > r.size; });

    int j = -1;
    for (size_t k = 0; k < i.size(); ++k)
    {
        if (i[k].size == 0) continue;

        if (j != -1 && i[j].size == i[k].size)
        {
            i[j].count += i[k].count;
        }
        else
        {
            i[++j] = i[k];
        }
    }
    i.resize(j + 1);
}

pair<interval, interval> split_interval(const interval& i)
{
    return i.size % 2 == 0
           ? make_pair(interval{i.size / 2, i.count}, interval{i.size / 2 - 1, i.count})
           : make_pair(interval{i.size / 2, i.count * 2}, interval{});
}

pair<ll, ll> solve(ll N, ll K)
{
    deque<interval> i {{N, 1}};

    while (K > i[0].count)
    {
        K -= i[0].count;

        auto split = split_interval(i[0]);

        i[0] = split.first;
        i.push_back(split.second);

        unify_intervals(i);

        assert(!i.empty() && i.size() <= 3);
    }

    auto split = split_interval(i[0]);

    return make_pair(split.first.size, split.second.count != 0 ? split.second.size : split.first.size);
};

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        ll N, K;
        cin >> N >> K;

        auto answer = solve(N, K);

        cout << "Case #" << t << ": " << answer.first << ' ' << answer.second << '\n';
    }

    return 0;
}
