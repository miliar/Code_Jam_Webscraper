#include <cstdio>
#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

typedef std::pair<int, int> activity;
typedef std::pair<int, activity> uactivity;

int T, Cas = 1;
int ac, aj;

std::vector<activity> cameron;
std::vector<activity> jamie;
std::vector<uactivity> partners;

int work_time(activity a) {
    return a.second - a.first;
}

void Small_test() {
    if (cameron.size() == 0 && jamie.size() == 1) {
        printf("2\n");
    }
    if (cameron.size() == 1 && jamie.size() == 0) {
        printf("2\n");
    }
    if (cameron.size() == 1 && jamie.size() == 1) {
        printf("2\n");
    }
    if ((cameron.size() == 0 && jamie.size() == 2) || 
        (cameron.size() == 2 && jamie.size() == 0)) {
        int a = (partners[0].second.first - 0) + (1440 - partners[1].second.second);
        int b = work_time(partners[0].second);
        int c = partners[1].second.first - partners[0].second.second;
        int d = work_time(partners[1].second);
        if (b + c + d <= 720 || d + a + b <= 720) {
            printf("2\n");
        } else {
            printf("4\n");
        }
    }
}

void UnitTest(int CaseID) {
    cameron.clear(), jamie.clear(), partners.clear();
    printf("Case #%d: ", CaseID);
    scanf("%d %d", &ac, &aj);
    for (int i = 1; i <= ac; i ++) {
        int ci, di;
        scanf("%d %d", &ci, &di);
        cameron.push_back(activity(ci, di));
        partners.push_back(uactivity(0, activity(ci, di)));
    }
    for (int i = 1; i <= aj; i ++) {
        int ji, ki;
        scanf("%d %d", &ji, &ki);
        jamie.push_back(activity(ji, ki));
        partners.push_back(uactivity(1, activity(ji, ki)));
    }
    std::sort(cameron.begin(), cameron.end());
    std::sort(jamie.begin(), jamie.end());
    std::sort(partners.begin(), partners.end(), [](const uactivity &ua, const uactivity &ub) {
        return ua < ub;
    });
    for (auto i : partners) {
//        std::cout << i.second.first << ' ' << i.second.second << '\n';
    }
    Small_test();
}

int main() {
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++) {
        UnitTest(i);
    }
    return 0;
}
