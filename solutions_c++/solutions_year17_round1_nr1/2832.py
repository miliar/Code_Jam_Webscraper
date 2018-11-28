#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <string>
using namespace std;

int n, m;
struct Node {
    int u, d, l, r;
    Node(){}
    Node(int _u, int _d, int _l, int _r): u(_u), d(_d), l(_l), r(_r){}
};

int main()
{
    int T_T, t_t;
    std::cin >> T_T;
    std::string a[26];
    for (t_t = 1; t_t <= T_T; ++t_t) {
        std::cin >> n >> m;
        std::cout << "Case #" << t_t << ":" << std::endl;
        for (int i = 0; i < n; ++i) {
            std::cin >> a[i];
        }
        std::map<char, std::set<int>> mp;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (a[i][j] == '?') {
                    continue;
                }
                mp[a[i][j]].insert(i*m+j);
            }
        }
        std::map<char, struct Node> mm;
        for (auto it: mp) {
            int u = 26, d = -1, l = 26, r = -1;
            for (auto ele: it.second) {
                u = std::min(u, ele / m);
                d = std::max(d, ele / m);
                l = std::min(l, ele % m);
                r = std::max(r, ele % m);
            }
            mm[it.first] = Node(u, d, l, r);
            for (int i = u; i <= d; ++i) {
                for (int j = l; j <= r; ++j) {
                    a[i][j] = it.first;
                    //it.second.insert(i*m+j);
                }
            }
        }
        for (std::map<char, struct Node>::iterator it = begin(mm); it != end(mm); ++it) {
            while (it->second.u > 0) {
                bool tag = true;
                for (int i = it->second.l; i <= it->second.r; ++i) {
                    if(a[it->second.u-1][i] != '?') {
                        tag = false;
                        break;
                    }
                }
                if (false == tag) {
                    break;
                }
                for (int i = it->second.l; i <= it->second.r; ++i) {
                    a[it->second.u-1][i] = it->first;
                }
                it->second.u--;
            }
            while (it->second.d < n-1) {
                bool tag = true;
                for (int i = it->second.l; i <= it->second.r; ++i) {
                    if(a[it->second.d+1][i] != '?') {
                        tag = false;
                        break;
                    }
                }
                if (false == tag) {
                    break;
                }
                for (int i = it->second.l; i <= it->second.r; ++i) {
                    a[it->second.d+1][i] = it->first;
                }
                it->second.d++;
            }
        }
        for (std::map<char, struct Node>::iterator it = begin(mm); it != end(mm); ++it) {
            while (it->second.l > 0) {
                bool tag = true;
                for (int i = it->second.u; i <= it->second.d; ++i) {
                    if(a[i][it->second.l-1] != '?') {
                        tag = false;
                        break;
                    }
                }
                if (false == tag) {
                    break;
                }
                for (int i = it->second.u; i <= it->second.d; ++i) {
                    a[i][it->second.l-1] = it->first;
                }
                it->second.l--;
            }
            while (it->second.r < m-1) {
                bool tag = true;
                for (int i = it->second.u; i <= it->second.d; ++i) {
                    if(a[i][it->second.r+1] != '?') {
                        tag = false;
                        break;
                    }
                }
                if (false == tag) {
                    break;
                }
                for (int i = it->second.u; i <= it->second.d; ++i) {
                    a[i][it->second.r+1] = it->first;
                }
                it->second.r++;
            }
        }


        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                std::cout << a[i][j];
            }
            std::cout << std::endl;
        }
    }
}

