#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    ifstream input;
    ofstream output;
    input.open("data/C-small-2-attempt0.in");
    output.open("data/C-small-2.out");
    input >> n;
    for (int test = 0; test < n; test++)
    {
        long long n, k;
        input >> n >> k;
        set<long long> occupied;
        set<pair<long long, long long>> open;
        occupied.insert(0);
        occupied.insert(n + 1);
        open.insert(pair<long long, long long>(-n, 1));
        for (int s = 0; s < k; s++)
        {
            pair<long long, long long> space = *open.begin();
            open.erase(open.begin());
            long long pos = -space.first / 2L + space.second;
            if (space.first % 2 == 0)
            {
                pos--;
            }
            auto it = occupied.insert(pos).first;
            long long before = *(--it);
            it++;
            long long after = *(++it);
            open.insert(pair<long long, long long> (-(pos - before - 1), before + 1));
            open.insert(pair<long long, long long> (-(after - pos - 1), pos + 1));
            if (s == k - 1)
            {
                output << "Case #" << (test + 1) << ": " << max(pos - before - 1, after - pos - 1) << " " << min(pos - before - 1, after - pos - 1) << endl;
            }
        }
    }
}
