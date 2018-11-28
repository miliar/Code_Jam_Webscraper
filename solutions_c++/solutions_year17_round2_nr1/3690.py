#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define DEBUG false


using namespace std;

struct horse {
    int pos;
    double v;
};

vector<horse> v[120];

bool cmp(horse a, horse b) {
    return a.pos < b.pos;

}

int d, n;


double h2Time(horse a, horse b) {
    int vDiff = a.v - b.v;
    int dDiff = b.pos - a.pos;
    return (double) dDiff / vDiff;
}


void read(int t) {

    scanf("%d %d", &d, &n);

    for(int i = 0; i < n; i++) {
        horse foo;
        double sp;
        scanf("%d %lf", &foo.pos, &sp);
        //DEBUG && printf("%f\n", sp);
        foo.v = sp;
        v[t].push_back(foo);
    }
}

void solve(int t) {

    sort(v[t].begin(), v[t].end(), cmp);
    double maxSpeed = 0;
    bool flag = true;

    for(int i = 0; i < v[t].size(); i++) {

        horse h = v[t][i];
        DEBUG && printf("Horse: %d %f\n", h.pos, h.v);
        if(h.pos < d) {
            double hTime = ((double)(d - h.pos)) / h.v;
            DEBUG && printf("time: %d %d %f\n", d, h.pos, h.v);
            double hSpeed = d / hTime;
            if(maxSpeed > hSpeed || flag) {
                maxSpeed = hSpeed;
                flag = false;
            }
        } else {
            continue;
        }
        for(int j = i + 1; j < v[t].size(); j++) {
            horse h2 = v[t][j];
            if(h2.v >= h.v) {
                continue;
            }
            double horseMeetTime = h2Time(h, h2);
            double meetDist = h2.pos + horseMeetTime * h2.v;
            double totalTime = horseMeetTime;
            if(meetDist < d) {
                totalTime += ((double) (d - meetDist) / h2.v);
            } else {
                totalTime = (double) (d - h.pos) / h.v;
            }
            double speed = (double) d / totalTime;
            horse fake;
            fake.pos = 0;
            fake.v = speed;
            double beginH = h2Time(fake, h);
            if(beginH < horseMeetTime && beginH > 0) {

                meetDist = h.pos + beginH * h.v;
                totalTime = beginH;
                totalTime += ((double) (d - meetDist) / h2.v);
                DEBUG && printf("SHIIT! %f %f %f\n", meetDist, totalTime, speed);
                speed = (double) d / totalTime;
            }
            DEBUG && printf("Speed for horse %d %d: %f %f %f %f %d %f | %d %f\n", i, j, speed, horseMeetTime, meetDist, totalTime, h.pos, h.v, h2.pos, h2.v);
            if(maxSpeed > speed) {
                maxSpeed = speed;
            }
        }
    }

    printf("Case #%d: %.6f\n", t + 1, maxSpeed);
}

void solveSmall(int t) {
    int sz = v[t].size();

    if(sz == 1) {
        horse h = v[t][0];
        double time = (double) (d - h.pos) / h.v;
        printf("Case #%d: %.6f", t + 1, time);
    } else {
        horse h = v[t][0];
        horse h2 = v[t][1];

        if(h.pos > h2.pos)
            swap(h, h2);
        double horseMeetTime = h2Time(h, h2);
        double meetDist = h2.pos + horseMeetTime * h2.v;
        double totalTime = horseMeetTime;
        if(meetDist < d) {
            totalTime += ((double) (d - meetDist) / h2.v);
        } else {
            totalTime = (double) (d - h.pos) / h.v;
        }

    }
}

int main() {
    int t;
    scanf("%d", &t);
    for(int tt = 0; tt < t; tt++) {
        read(tt);
       // if(tt == 17)
            solve(tt);
    }
}
