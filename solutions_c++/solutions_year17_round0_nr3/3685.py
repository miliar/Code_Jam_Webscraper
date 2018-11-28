#include <iostream>
#include <map>
#include <functional>

std::pair<long long,long long> solve(long long n, long long k)
{
    std::map<long long,long long,std::greater<long long>> m;
    m[n] = 1;

    while (k > 0)
    {
        auto it = m.begin();
        long long nn = it->first;
        long long kk = it->second;
        //std::clog << k << " / " << nn << " : " << kk << std::endl;

        long long r = nn / 2;
        long long l = nn - r - 1;
        if (kk >= k)
            return std::make_pair(r,l);

        k -= kk;
        m.erase(it);
        m[l] += kk;
        m[r] += kk;
    }
}

int main(int argc, char **argv)
{
    int T;
    std::cin >> T;
    for (int i=1;i<=T;++i)
    {
        long long n,k;
        std::cin >> n >> k;
        auto res = solve(n,k);
        std::cout << "Case #" << i << ": " << res.first << " " << res.second << "\n";
    }
    return 0;
}