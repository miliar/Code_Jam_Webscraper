#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;
void pp1(int i, int n, int k);

int main(int argc, const char * argv[]) {
    int t;
    cin>>t;
    for (int i = 1; i <= t; i++) {
        int n;
        int k;
        cin>>n>>k;
        pp1(i, n, k);
    }
}

void pp1(int test, int n, int k) {
    std::priority_queue<int> heap;
    heap.push(n);
    for (int i = 0; i < k - 1; i++) {
        int c = heap.top();
        heap.pop();
        heap.push(c / 2);
        heap.push(c - c / 2 - 1);
    }
    int mns = (heap.top() - 1) / 2;
    int mxs = heap.top() / 2;
    printf("Case #%d: %d %d\n", test, mxs, mns);
}
