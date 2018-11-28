#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<queue>
#include<set>
#include<sstream>
#include<complex>
#include<map>
using namespace std;
long long n, k;
void getinput() {
    cin >> n >> k;
}
void process() {
    long long minL = 1LL << 62;
    long long maxL = 0;
    priority_queue<long long> heap;
    map<long long, long long> countSegment;
    heap.push(n);
    countSegment[n] = 1;
    while (k > 0) {
        long long l = heap.top();
        heap.pop();
        k -= countSegment[l];
        if (l % 2 == 0) {
            minL = l / 2 - 1;
            maxL = l / 2;
        }
        else {
            minL = l/2;
            maxL = l/2;
        }
        if (minL > 0) {
            if (!countSegment.count(minL)) heap.push(minL);
            countSegment[minL] += countSegment[l];
        }
        if (maxL > 0) {
            if (!countSegment.count(maxL)) heap.push(maxL);
            countSegment[maxL] += countSegment[l];
        }
    }
    cout << maxL << " " << minL << endl;
}
int main() {
//    freopen("D:\\Projects\\GGCodeJam\\bai3.inp", "r", stdin);
//    freopen("D:\\Projects\\GGCodeJam\\bai3.out", "w", stdout);
    int t; cin >> t;
    for(int test = 0; test < t; test ++) {
        getinput();
        cout << "Case #" << test + 1 << ": ";
        process();
    }
    return 0;
}
