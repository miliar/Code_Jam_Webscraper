#include <ios>
#include <iostream>
#include <map>
#include <cstdio>
#include <utility>

std::map<long long int, long long int> m;

int main()
{
    //std::ios_base::sync_with_stdio(false);
    //std::cin.tie(NULL);
    //std::cout.tie(NULL);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    long long int n, k;
    std::cin >> tc;
    for (int t = 0; t < tc; t++)
    {
        std::cout << "Case #" << t+1 << ": ";
        std::cin >> n >> k;
        m.clear();
        m[n] = 1;
        while (m.rbegin()->second < k)
        {
            long long int tp = m.rbegin()->first;
            long long int cnt = m.rbegin()->second;

            if (tp & 1)
            {
                if (tp/2 > 0)
                {
                    if (m.find(tp/2) == m.end())
                        m.insert(std::make_pair(tp/2, 2*cnt));
                    else
                        m[tp/2] += 2*cnt;
                }
            }
            else
            {
                if (tp/2 > 0)
                {
                    if (m.find(tp/2) == m.end())
                        m.insert(std::make_pair(tp/2, cnt));
                    else
                        m[tp/2] += cnt;
                }
                if (tp/2-1 > 0)
                {
                    if (m.find(tp/2-1) == m.end())
                        m.insert(std::make_pair(tp/2-1, cnt));
                    else
                        m[tp/2-1] += cnt;
                }
            }
            k -= m.rbegin()->second;
            m.erase(m.rbegin()->first);
        }
        long long int s = m.rbegin()->first;
        if (s & 1)
            std::cout << s/2 << ' ' << s/2 << '\n';
        else
            std::cout << s/2 << ' ' << s/2-1 << '\n';
    }
}
