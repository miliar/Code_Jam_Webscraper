#include <cstdio>
#include <algorithm>

std::pair<std::pair<int, int>, bool> przedzialy[300];
std::vector<int> v0, v1, v2; //type, length

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int N, M;
        scanf("%d%d", &N, &M);
        int a, b;
        int sumA = 0;
        v0.clear();
        v1.clear();
        v2.clear();
        for (int i = 0; i < N; i++) {
            scanf("%d%d", &a, &b);
            sumA += b - a;
            przedzialy[i] = {{a, b}, false};
        }
        for (int i = 0; i < M; i++) {
            scanf("%d%d", &a, &b);
            przedzialy[i + N] = {{a, b}, true};
        }
        std::sort(przedzialy, przedzialy + N + M);
        int wyn = 0;
        for (int i = 0; i < N + M; i++) {
            if (i == 0) {
                int l = przedzialy[0].first.first + 1440 - przedzialy[N + M - 1].first.second;
                int type = (int) przedzialy[0].second + (int) przedzialy[N + M - 1].second;
                if (l != 0) {
                    //printf("Dodaje przedzial o dlugosci %d typu %d (%d do %d)\n", l, type, przedzialy[N + M - 1].first.second, przedzialy[0].first.first);
                    if (type == 0)
                        v0.push_back(l);
                    else if (type == 1)
                        v1.push_back(l);
                    else
                        v2.push_back(l);
                } else if (type == 1) {
                    wyn++;
                }
                continue;
            }
            int l = przedzialy[i].first.first - przedzialy[i - 1].first.second;
            int type = (int) przedzialy[i].second + (int) przedzialy[i - 1].second;
            if (l != 0) {
                //printf("Dodaje przedzial o dlugosci %d typu %d (%d do %d)\n", l, type, przedzialy[i - 1].first.second, przedzialy[i].first.first);
                if (type == 0)
                    v0.push_back(l);
                else if (type == 1)
                    v1.push_back(l);
                else
                    v2.push_back(l);
            } else if (type == 1) {
                wyn++;
            }
        }
        std::sort(v0.begin(), v0.end());
        std::sort(v1.begin(), v1.end());
        std::sort(v2.begin(), v2.end());
        for (int i = 0; i < v0.size(); i++) {
            if (sumA + v0[i] > 720) {
                wyn += (v0.size() - i) * 2;
                sumA = 720;
                break;
            }
            sumA += v0[i];
        }
        for (int i = 0; i < v1.size(); i++) {
            if (sumA + v1[i] > 720) {
                wyn += v1.size() - i;
                sumA = 720;
                break;
            }
            sumA += v1[i];
            wyn++;
        }
        for (int i = v2.size() - 1; i >= 0; i--) {
            if (sumA + v2[i] > 720) {
                wyn += (sumA != 720) * 2;
                break;
            }
            sumA += v2[i];
            wyn += 2;
        }
        printf("Case #%d: %d\n", t, wyn);
    }
    return 0;
}