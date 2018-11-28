#include <iostream>
#include <cstdio>
#include <queue>

#define DEBUG false

using namespace std;


struct segment {
    int a;
    int b;

    bool operator<(segment const& x) const {
        int lenX = x.b - x.a;
        int len = b - a;
        if(lenX == len)
            return a > x.a;
        return lenX > len;
    }
};

int n, k;

void read() {

    scanf("%d %d", &n, &k);
}

priority_queue<segment> q[100];

void solve(int t) {

    segment a;
    a.a = 0;
    a.b = n - 1;
    q[t].push(a);


    for(int i = 1; i <= k; i++) {
        a = q[t].top();
        q[t].pop();
        segment left, right;
        DEBUG && printf("Processing segment %d %d\n", a.a, a.b);
        int mid = (a.a + a.b) / 2;
        if((a.b - a.a + 1) % 2 == 0) {
            left.a = a.a;
            left.b = mid - 1;
        }

        left.a = a.a;
        left.b = mid - 1;

        right.a = mid + 1;
        right.b = a.b;

        if(i == k) {
            int lD = mid - a.a;
            int rD = a.b - mid;
            printf("Case #%d: %d %d\n", t, lD > rD ? lD : rD, lD > rD ? rD : lD);
            break;
        }
        DEBUG && printf("Pushing %d %d | %d %d\n", left.a, left.b, right.a, right.b);
        q[t].push(left);
        q[t].push(right);
    }

}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        read();
        solve(i + 1);
    }
}
