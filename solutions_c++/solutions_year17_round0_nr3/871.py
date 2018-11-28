//
// Created by quuynh on 08/04/17.
//

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <queue>
#include <stack>
#include <climits>
#include <unordered_map>
#include <unordered_set>

using namespace std;

struct Interval {
    long n, quantity;

    Interval(long n, long quantity) {
        this->n = n;
        this->quantity = quantity;
    }
};

string solve(long n, long k) {
    if (k == n) return "0 0";
    priority_queue<long, vector<long>> heap;
    heap.push(n);
    unordered_map<long, long> numbers;
    numbers.insert({n, 1});
    long total = 0;
    while (!heap.empty()) {
        long top = heap.top();
        heap.pop();
        total += numbers[top];
        if (total >= k) {
            if (top % 2 == 1) return to_string(top / 2) + " " + to_string(top / 2);
            else return to_string(top / 2) + " " + to_string(top / 2 - 1);
        }
        if (top % 2 == 1) {
            long newTop = top / 2;
            if (numbers.find(newTop) == numbers.end()) {
                numbers.insert({newTop, 0});
                heap.push(newTop);
            }
            numbers[newTop] += 2 * numbers[top];
        } else {
            long newTop = top / 2 - 1;
            if (numbers.find(newTop) == numbers.end()) {
                numbers.insert({newTop, 0});
                heap.push(newTop);
            }
            numbers[newTop] += numbers[top];
            //second time
            newTop = top / 2;
            if (numbers.find(newTop) == numbers.end()) {
                numbers.insert({newTop, 0});
                heap.push(newTop);
            }
            numbers[newTop] += numbers[top];
        }
    }
    return "";
}

int main() {
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/C-large.in", "r", stdin);
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/GoogleCodejam/output3", "w", stdout);

    int ntest;
    cin >> ntest;
    for (int test = 1; test <= ntest; test++) {
        long n, k;
        cin >> n >> k;
        string result = solve(n, k);
        cout << "Case #" << test << ": ";
        cout << result;
        if (test < ntest) cout << endl;
    }
}
