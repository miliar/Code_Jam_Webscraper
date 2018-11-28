#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <cmath>
using namespace std;



struct Interval {
    int left;
    int right;
    Interval(int l, int r): left(l), right(r) {}
};

int main()
{
    int T;
    string input;
    cin >> T;
    int N, K;
    auto cmp = [](const Interval& left, const Interval& right) -> bool{
        int llen = left.right - left.left;
        int rlen = right.right - right.left;

        if(llen != rlen) {
            return llen < rlen;
        }

        return left.left > right.left;


    };

    for(int n = 1; n <= T; ++n)
    {
        priority_queue<Interval, vector<Interval>, decltype(cmp)> pq(cmp);
        cin >> N >> K;
        pq.push(Interval(0, N+1));
        for(int i = 1; i < K; ++i) {
            auto interval = pq.top();
            pq.pop();
            int len = interval.right - interval.left - 1;
            int llen = (len - 1) / 2;
            pq.push(Interval(interval.left, interval.left + llen + 1));
            pq.push(Interval(interval.left + llen + 1, interval.right));
        }
        auto interval = pq.top();
        pq.pop();
        int len = interval.right - interval.left - 1;
        int llen = (len - 1) / 2;
        int rlen = len - 1 - llen;
        cout << "Case #" << n << ": " << rlen << " " << llen << endl;

    }




}