#include <iostream>
#include <cmath>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cstdlib>
#include <deque>
using namespace std;

double eps = 1e-6;

struct segment
{
    int start;
    int end;
    int line;
};

bool cmp(segment& s1, segment& s2)
{
    if (s1.start == s2.start && s1.end == s2.end)
        return s1.line < s2.line;
    if (s1.start == s2.start)
        return s1.end < s2.end;
    return s1.start < s2.start;
}

segment getseg(int q, int r, int l)
{
    int start = ceil(q / (double) r / 1.1 - eps);
    int end = floor(q / (double) r / 0.9 + eps);
    segment s;
    s.start = start;
    s.end = end;
    s.line = l;
    return s;
}

void solve() 
{
    int n, p;
    cin >> n >> p;

    vector<int> r(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> r[i];
    }

    vector<deque<segment> > segq(n);
    vector<segment> allseg;

    int cnt = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < p; ++j)
        {
            int q;
            cin >> q;
            segment s = getseg(q, r[i], i);
            if (s.start > s.end)
                continue;
            allseg.push_back(s);
        }
    }
    sort(allseg.begin(), allseg.end(), cmp);

    for (int i = 0; i < allseg.size(); ++i)
    {
        segment s = allseg[i];
        for (int j = 0; j < n; ++j)
        {
            while (!segq[j].empty())
            {
                if (segq[j].front().end < s.start)
                    segq[j].pop_front();
                else
                    break;
            }
        }
        segq[s.line].push_back(s);

        bool flag = true;
        for (int j = 0; j < n; ++j)
        {
            if (segq[j].empty())
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            ++cnt;
            for (int j = 0; j < n; ++j)
            {
                segq[j].pop_front();
            }
        }
    }

    cout << cnt << endl;
}



int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
