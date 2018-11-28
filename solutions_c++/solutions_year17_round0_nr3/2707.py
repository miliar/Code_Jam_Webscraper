using namespace std;

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <queue>

typedef pair<long long, long long> ii;
typedef vector<int> vi;

int t;
long long n, k;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C.txt", "w", stdout);
    scanf("%d", &t);
    for (int r = 1; r <= t; r++) {
        scanf("%lld %lld", &n, &k);
        map<long long, long long> pq;
        pq[n] = 1;
        ii temp;
        while (k >= 1) {
            temp = *(pq.rbegin());
            pq.erase(temp.first);
            k -= temp.second;
            if (temp.first % 2 == 1) {
                if (!pq.count(temp.first/2)) pq[temp.first/2] = 0;
                pq[temp.first/2] += temp.second * 2;
            }
            else {
                if (!pq.count(temp.first/2)) pq[temp.first/2] = 0;
                if (!pq.count((temp.first - 1)/2)) pq[(temp.first - 1)/2] = 0;
                pq[temp.first/2] += temp.second;
                pq[(temp.first - 1)/2] += temp.second;
            }
        }
        long long ma = temp.first/2;
        long long mi = (temp.first-1)/2;
        printf("Case #%d: ", r);
        printf("%lld %lld\n", ma, mi);
    }
}

