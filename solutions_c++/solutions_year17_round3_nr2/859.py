#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

const int MAX_NUM = 100;
int T;
int Ac, Aj;

struct interval {
    int start, end;
    bool operator < (const interval & that) const {
        return (start < that.start);
    }
} cameron[MAX_NUM], jamie[MAX_NUM], *curr;

int minStart(interval curr[], int num, int &start) {
    int minTime = 1440;
    
    for (int i = 0; i < num; i++) {
        int last = (i == 0) ? num - 1 : i - 1;
        
        int currTime = curr[last].end - curr[i].start;
        if (currTime < 0) currTime += 1440;
        
        if (currTime < minTime) {
            minTime = currTime;
            start = i;
        }
    }
    
    return minTime;
}

int solve(interval curr[], int num) {
    sort(curr, curr + num);
    if (num == 1) return 1;
    
    priority_queue<int> pq;
    int start = 0;
    int tot = minStart(curr, num, start);
    int prev = curr[start].end;
    
    for (int i = start + 1, j = 0; j < num; j++, i++) {
        if (i == num) i -= num;
        
        int temp = curr[i].start - prev;
        if (temp < 0) temp += 1440;
        pq.push(temp);
        prev = curr[i].end;
    }
    
    int change = 1;
    while (tot > 720) {
        tot -= pq.top();
        pq.pop();
        change++;
    }
    
    return change;
}

int main() {
    freopen("1b.in", "r", stdin);
    
    scanf("%d\n", &T);
    
    for (int test = 1; test <= T; test++) {
        scanf("%d %d\n", &Ac, &Aj);
        for (int i = 0; i < Ac; i++) {
            scanf("%d %d\n", &cameron[i].start, &cameron[i].end);
        }
        for (int i = 0; i < Aj; i++) {
            scanf("%d %d\n", &jamie[i].start, &jamie[i].end);
        }
        
        int num = max(Ac, Aj);
        if (Ac < Aj) curr = jamie;
        else         curr = cameron;
        
        
        printf("Case #%d: %d\n", test, 2 * solve(curr, num));
    }
}
