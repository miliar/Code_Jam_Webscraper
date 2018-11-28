#include <bits/stdc++.h>
using namespace std;

struct Position {
    long long size, leftCost, rightCost;
    Position(long long _size) {
        size = _size;
        long long mid = size / 2;
        leftCost = max(0LL, mid);
        rightCost = max(0LL, size - mid - 1);
        //cout << size << " " << mid << " " << leftCost << " " << rightCost << endl;
    }

    bool operator < (const Position &other) const {
        if (min(leftCost, rightCost) < min(other.leftCost, other.rightCost))
            return true;
        
        if (min(leftCost, rightCost) == min(other.leftCost, other.rightCost)) {
            if (max(leftCost, rightCost) < max(other.leftCost, other.rightCost))
                return true;
        }

        return false;
    }
};

pair <long long, long long> solve(long long n, long long k) {
    map <Position, long long> mp;
    mp[Position(n)] = 1;

    while (k > 0) {
        Position now = mp.rbegin()->first;
        //cerr << now.size << " " << now.leftCost << " " << now.rightCost << " " << mp[now] << endl;
        
        k -= mp[now];
        if (k <= 0) 
            return make_pair(max(now.leftCost, now.rightCost), min(now.leftCost, now.rightCost));
        
        if (now.leftCost > 0) mp[now.leftCost] += mp[now];
        if (now.rightCost > 0) mp[now.rightCost] += mp[now];
        mp.erase(now);
        //cerr << k << " erase finished\n";
    }

    return make_pair(0, 0);
}

int main() {
    int t;
    scanf ("%d", &t);

    for (int tc = 1; tc <= t; tc++) {
        cerr << tc << "\n";
        long long n, k;
        scanf ("%lld %lld", &n, &k); 
        pair <long long, long long> ans = solve(n, k);
        printf ("Case #%d: %lld %lld\n", tc, ans.first, ans.second);
    }
    return 0;
}