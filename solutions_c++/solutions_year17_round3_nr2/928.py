#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Interval{
    Interval(){}
    Interval(int _start, int _end, int _belong): start(_start), end(_end),
        belong(_belong), tempBelong(0){
        length = end - start;
    }

    bool operator < (const Interval &i) const{
        return start < i.start;
    }

    int start;
    int end;
    int length;
    int belong;
    int tempBelong;
};

int main(void){
    int tt;
    int nac, naj, n;
    scanf("%d", &tt);
    for(int tc = 1; tc <= tt; tc++){
        vector<Interval> intervals;
        vector<Interval> freeTimes;
        scanf("%d%d", &nac, &naj);
        n = nac + naj;
        int s, e;
        for(int i = 0; i < nac; i++){
            scanf("%d%d", &s, &e);
            intervals.push_back(Interval(s, e, 2));
        }
        for(int i = 0; i < naj; i++){
            scanf("%d%d", &s, &e);
            intervals.push_back(Interval(s, e, 1));
        }
        sort(intervals.begin(), intervals.end());
        int minTime = intervals[0].start;
        for(int i = 0; i < n; i++){
            intervals[i].start -= minTime;
            intervals[i].end -= minTime;
        }

        for(int i = 0; i < n - 1; i++){
            if(intervals[i].end < intervals[i+1].start){
                freeTimes.push_back(Interval(intervals[i].end, intervals[i+1].start, 0));
            }
        }
        if(intervals[n-1].end != 1440){
            freeTimes.push_back(Interval(intervals[n-1].end, 1440, 0));
        }
        intervals.insert(intervals.end(), freeTimes.begin(), freeTimes.end());
        sort(intervals.begin(), intervals.end());
        n = (int)intervals.size();

        int cnt[3] = {0};
        int lastBelong = intervals[0].belong;
        int cntTimes = 0;
        for(int i = 0; i < n; i++){
            if(intervals[i].belong != 0){
                cnt[intervals[i].belong] += intervals[i].length;
                if(intervals[i].belong != lastBelong){
                    lastBelong = intervals[i].belong;
                    cntTimes++;
                }
            }else{
                cnt[lastBelong] += intervals[i].length;
                intervals[i].tempBelong = lastBelong;
            }
        }
        if(intervals[0].belong != lastBelong){
            cntTimes++;
        }

        while(cnt[1] > 720){
            int maxFreeLen = 0;
            int maxFreeInd = 0;
            for(int i = 0; i < n; i++){
                if(intervals[i].tempBelong == 1 &&
                   intervals[i].length > maxFreeLen){
                    maxFreeLen = intervals[i].length;
                    maxFreeInd = i;
                }
            }
            if(maxFreeLen <= cnt[1] - 720){
                cnt[2] += maxFreeLen;
                cnt[1] -= maxFreeLen;
                intervals[maxFreeInd].tempBelong = 0;
            }else{
                cnt[2] += cnt[1] - 720;
                cnt[1] = 720;
                intervals[maxFreeInd].tempBelong = 0;
            }
            if(intervals[maxFreeInd-1].belong == intervals[(maxFreeInd+1)%n].belong){
                cntTimes += 2;
            }
        }
        while(cnt[2] > 720){
            int maxFreeLen = 0;
            int maxFreeInd = 0;
            for(int i = 0; i < n; i++){
                if(intervals[i].tempBelong == 2 &&
                   intervals[i].length > maxFreeLen){
                    maxFreeLen = intervals[i].length;
                    maxFreeInd = i;
                }
            }
            if(maxFreeLen <= cnt[2] - 720){
                cnt[1] += maxFreeLen;
                cnt[2] -= maxFreeLen;
                intervals[maxFreeInd].tempBelong = 0;
            }else{
                cnt[1] += cnt[2] - 720;
                cnt[2] = 720;
                intervals[maxFreeInd].tempBelong = 0;
            }
            if(intervals[maxFreeInd-1].belong == intervals[(maxFreeInd+1)%n].belong){
                cntTimes += 2;
            }
        }
        printf("Case #%d: %d\n", tc, cntTimes);
    }
    return 0;
}
