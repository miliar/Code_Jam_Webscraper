//
// Created by Xuren Zhou on 8/4/2017.
//

#include <iostream>
#include <queue>
using namespace std;


long bathroomStalls(long n, long k) { // return the size
    deque<pair<long, long>> q;
    q.push_back(make_pair(n, 1));

    long cur_num = 0L;
    while(true) {
        pair<long, long>& elem = q.front();
        if(elem.second + cur_num >= k)
            break;

        cur_num += elem.second;
        long r = elem.first;
        long y = r/2L;
        long z = (r-1L)/2L;

        if(y == q.back().first) {
            q.back().second += elem.second;
        }
        else {
            q.push_back(make_pair(y, elem.second));
        }

        if(z == q.back().first) {
            q.back().second += elem.second;
        }
        else {
            q.push_back(make_pair(z, elem.second));
        }

        q.pop_front();
    }

    return q.front().first;
}

int main() {
    int t;
    cin >> t;
    for(int i=1; i <= t; i++) {
        long n, k;
        cin >> n >> k;
        long y, z, size;
        size = bathroomStalls(n ,k);
        y = size/2L;
        z = (size-1L)/2L;
        cout << "Case #" << i << ": " << y << " " << z << endl;
    }
    return 0;
}