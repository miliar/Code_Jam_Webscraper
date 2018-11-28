#include <bits/stdc++.h>

using namespace std;

int intervalsNo[2];
int careTime[2];

int diff(int ret) {
    if (ret < 0) {
        return ret + 24 * 60;
    }
    return ret;
}

bool cmp(pair<int, int> a, pair<int, int> b) {
    return diff(a.second - a.first) > diff(b.second - b.first);
}

void solveTest() {
    scanf("%d %d", &intervalsNo[0], &intervalsNo[1]);
    
    careTime[0] = careTime[1] = 0;
    vector<pair<pair<int, int>, int> > intervals;
    
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < intervalsNo[i]; j++) {
            int a, b;
            scanf("%d %d", &a, &b);
            intervals.push_back({{a, b}, i});
        }
    }
    
    sort(intervals.begin(), intervals.end());
    
    vector<pair<int, int> > specialIntervals[2];
    int ans = 0;
    int betweenTime = 0;
    for (int i = 0; i < intervals.size(); i++) {
        int start = intervals[i].first.first;
        int finish = intervals[i].first.second;
        int type = intervals[i].second;
        careTime[type] += finish - start;
        int nextStart = intervals[(i + 1) % intervals.size()].first.first;
        int nextFinish = intervals[(i + 1) % intervals.size()].first.second;
        int nextType = intervals[(i + 1) % intervals.size()].second;
        if (type == nextType) {
            specialIntervals[type].push_back({finish, nextStart});
            careTime[type] += diff(nextStart - finish);
        } else {
            ans++;
            betweenTime += diff(nextStart - finish);
        }
    }
    
    assert(careTime[0] + careTime[1] + betweenTime == 24 * 60);
    if (careTime[0] <= 12 * 60 && careTime[1] <= 12 * 60) {
        printf("%d\n", ans);
        return;
    }
    
    for (int i = 0; i < 2; i++) {
        sort(specialIntervals[i].begin(), specialIntervals[i].end(), cmp);
    }
    if (careTime[0] <= 12 * 60) {
        careTime[0] += betweenTime;
        for (int i = 0; i < specialIntervals[1].size(); i++) {
            ans += 2;
            int length = diff(specialIntervals[1][i].second - specialIntervals[1][i].first);
            careTime[0] += length;
            if (careTime[0] >= 12 * 60) {
                break;
            }
        }
    } else {
        careTime[1] += betweenTime;
        for (int i = 0; i < specialIntervals[0].size(); i++) {
            ans += 2;
            int length = diff(specialIntervals[0][i].second - specialIntervals[0][i].first);
            careTime[1] += length;
            if (careTime[1] >= 12 * 60) {
                break;
            }
        }
    }
    
    printf("%d\n", ans);
}

int main() {

    int t;
    scanf("%d", &t);
    for (int test = 1; test <= t; test++) {
        printf("Case #%d: ", test);
        solveTest();
    }
    
    return 0;
}