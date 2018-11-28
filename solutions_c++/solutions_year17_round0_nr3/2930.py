#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <map>

using namespace std;

inline void make_step(map <long long, long long> &m, long long &sum)
{
    map <long long, long long> ret;

    sum = 0;
    for (auto a : m)
    {
        ret[(a.first + 1) / 2] += a.second;
        ret[a.first / 2] += a.second;
        sum += 2 * a.second;
    }

    m = ret;
}

inline long long find_segment(map <long long, long long> &m, long long k)
{
    long long now = 0;
    for (auto a : m)
    {
        if (now + a.second >= k)
            return -1 * a.first;
        now += a.second;
    }
}

long long sum;
map <long long, long long> m;

int t;

int main()
{
    ifstream cin("C-large.in");
    ofstream cout("C-small-1-attempt0.out");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);

    cin >> t;
    for (int num = 0; num < t; num++)
    {
        m.clear();
        long long n, k;

        cin >> n >> k;

        m[-1 * n] = sum = 1;
        while (sum < k)
        {
            k -= sum;
            make_step(m, sum);
        }

        long long seg = find_segment(m, k);
        cout << "Case #" << num + 1 << ": " << seg / 2 << ' ' << (seg - 1) / 2 << endl;
    }
    return 0;
}
