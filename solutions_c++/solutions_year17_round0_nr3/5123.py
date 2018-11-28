#include <iostream>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

struct data
{
    int left, right, index;

    int l() const
    {
        return index - left;
    }

    int r() const
    {
        return right - index;
    }

    friend bool operator<(const data& lhs, const data& rhs);
};

bool operator<(const data& lhs, const data& rhs)
{
    int lhs_l = lhs.index - lhs.left, rhs_l = rhs.index - rhs.left;
    int lhs_r = lhs.right - lhs.index, rhs_r = rhs.right - rhs.index;

    int min_l = min(lhs_l, lhs_r), max_l = max(lhs_l, lhs_r);
    int min_r = min(rhs_l, rhs_r), max_r = max(rhs_l, rhs_r);

    if (min_l > min_r)
        return true;
    else if (min_l < min_r)
        return false;

    if (max_l > max_r)
        return true;
    else if (max_l < max_r)
        return false;

    return lhs.index < rhs.index;
}

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test < T + 1; ++test)
    {
        int N, K;
        cin >> N >> K;
        set<data> s;

        s.insert({0, N - 1, (N - 1)/ 2});

        int y, z;
        for (int i = 0; i < K; ++i)
        {
            auto it = s.begin();
            data d = *it;
            s.erase(it);
            y = max(d.l(), d.r());
            z = min(d.l(), d.r());

            if (d.index - 1 >= d.left)
            {
                s.insert({d.left, d.index - 1, (d.left + d.index - 1) / 2});
            }
            if (d.index + 1 <= d.right)
            {
                s.insert({d.index + 1, d.right, (d.index + 1 + d.right) / 2});
            }
        }

        cout << "Case #" << test << ": " << y << " " << z << endl;
    }

    return 0;
}
