#include <iostream>
#include <cstdio>
#include <queue>
#include <map>
#include <set>

void process(int i, long long n, long long k);

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        long long n;
        long long k;
        scanf("%lld %lld", &n, &k);
        { process(i, n, k); }
    }
}

void process(int test, long long n, long long k) {
    std::priority_queue<long long> heap;
    std::map<long long, long long> count;
    std::set<long long> mySet;
    mySet.clear();
    heap.push(n);
    count[n] = 1;
    mySet.insert(n);
    while (count[heap.top()] < k) {
        long long c = heap.top();
        k -= count[heap.top()];
        heap.pop();
        if (mySet.insert(c / 2).second) {
            count[c / 2] = count[c];
            heap.push(c / 2);
        } else {
            count[c / 2] += count[c];
        }
        
        if (mySet.insert(c - c / 2 - 1).second) {
            count[c - c / 2 - 1] = count[c];
            heap.push(c - c / 2 - 1);
        } else {
            count[c - c / 2 - 1] += count[c];
        }
    }
    long long min = (heap.top() - 1) / 2;
    long long max = heap.top() / 2;
    printf("Case #%d: %lld %lld\n", test, max, min);
}
