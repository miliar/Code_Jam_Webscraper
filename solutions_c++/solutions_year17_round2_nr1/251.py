#include<iostream>
#include<algorithm>
#include<cstdio>
const int BUF = 1005;
using namespace std;


class Horse {
public:
    double pos;
    double speed;
    Horse(){}
    Horse(double pos, double speed): pos(pos), speed(speed) {}
};

    
int len, nHorse;
Horse horse[BUF];

void read() {
    cin >> len >> nHorse;
    for (int i = 0; i < nHorse; ++i) {
        cin >> horse[i].pos >> horse[i].speed;
    }
}

void work(int cases) {
    double maxTime = 0;
    for (int i = 0; i < nHorse; ++i) {
        maxTime = max(maxTime, (len - horse[i].pos) / horse[i].speed);
    }
    printf("Case #%d: %.10lf\n", cases, len / maxTime);
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
