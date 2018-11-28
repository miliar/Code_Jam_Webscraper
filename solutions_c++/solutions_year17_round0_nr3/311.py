// Google Code Jam Qualification Round 2017
// Problem C. Bathroom Stalls
// Solution in C++
// By Smithers

#include <cstdio>
#include <map>

int main()
{
    int t;
    
    std::scanf("%d", &t);
    for (int x = 1; x <= t; x++)
    {
        long long n, k;
        std::scanf("%lld%lld", &n, &k);
        std::map<long long, long long> chains;
        chains[n] = 1;
        
        long long maxdist, mindist;
        while (k > 0)
        {
            std::pair<long long, long long> c = *chains.rbegin();
            if (k >= c.second)
            {
                chains.erase(c.first);
            }
            else
            {
                chains[c.first] -= k;
                c.second = k;
            }
            maxdist = c.first / 2;
            mindist = (c.first - 1) / 2;
            if (chains.count(maxdist))
                chains[maxdist] += c.second;
            else
                chains[maxdist] = c.second;
            if (chains.count(mindist))
                chains[mindist] += c.second;
            else
                chains[mindist] = c.second;
            k -= c.second;
        }
        
        std::printf("Case #%d: %lld %lld\n", x, maxdist, mindist);
    }
    return 0;
}
