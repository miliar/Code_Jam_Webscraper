#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

long long n, k;


int main()
{
    int T_T, t_t;
    std::cin >> T_T;
    for (t_t = 1; t_t <= T_T; ++t_t) {
        std::cout << "Case #" << t_t << ": ";
        std::cin>> n >> k;
        std::map<long long, long long> mp;
        std::priority_queue<long long> que;
        que.push(n);
        mp[n] = 1;
        long long y, z;
        while (false == que.empty()) {
            long long u = que.top();
            // std::cout << "u = " << u << ", mp[u] = " << mp[u] << std::endl;
            que.pop();
            k -= mp[u];
            if (k <= 0) {
                if (u & 1) {
                    y = z = u >> 1;
                } else {
                    z = (y = u>>1) - 1;
                }
                break;
            }
            if (u & 1) {
                if (!mp.count(u>>1)) {
                    que.push(u >> 1);
                }
                mp[u>>1] += 2 * mp[u];
            } else {
                if (!mp.count(u>>1)) {
                    que.push(u>>1);
                }
                mp[u>>1] += mp[u];
                if (!mp.count((u>>1)-1)) {
                    que.push((u>>1)-1);
                }
                mp[(u>>1)-1] += mp[u];
            }
        }
        std::cout << y << " " << z << std::endl;
    }
    return 0;
}
