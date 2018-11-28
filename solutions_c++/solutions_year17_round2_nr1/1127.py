#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int> > horses;

int main() {
    int t;
    scanf("%d", &t);

    for(int c = 0 ; c < t ; c++) {
        int d, n;
        scanf("%d %d", &d, &n);

        horses.resize(n);
        int k, s;
        while(n--) {
            scanf("%d %d", &k, &s);
            horses[n] = make_pair(k, s);
        }

        sort(horses.begin(), horses.end());

        double min_time = double(d - horses[horses.size() - 1].first) / double(horses[horses.size() - 1].second);
        for(int i = horses.size() - 2 ; i >= 0 ; i--) {
            pair<int, int> p = horses[i];
            k = p.first;
            s = p.second;
            min_time = max(min_time, double(d - k) / double(s));
        }

        printf("Case #%d: %.6f\n", c+1, double(d) / min_time);
    }

    return 0;
}
