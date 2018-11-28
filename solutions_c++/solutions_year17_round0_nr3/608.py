/*
Will Long
Google Code Jam 2017
Qualification - Problem 3

April 7, 2017
*/

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
    string filename = argv[1];
    freopen((filename+".in").c_str(), "r", stdin);
    freopen((filename+".out").c_str(), "w", stdout);

    int cases;
    cin >> cases;

    for (int c = 1; c <= cases; c++) {
        uint64_t n, k;
        cin >> n >> k;
        map<uint64_t, uint64_t> smap;
        priority_queue<uint64_t> squeue;
        uint64_t occupied=0, min, max;
        squeue.push(n);
        smap[n] = 1;
        while(occupied < k) {
            uint64_t slot_size = squeue.top();
            uint64_t slot_num = smap[slot_size];
            squeue.pop();
            smap.erase(slot_size);
            occupied += slot_num;
            min = (slot_size-1)/2;
            max = slot_size/2;
            //cout << slot_size << " " << slot_num << " " << occupied << " " << min << " " << max << endl;
            if(smap.find(min) == smap.end()) {
                smap[min]=0;
                squeue.push(min);
            }
            if(smap.find(max) == smap.end()) {
                smap[max]=0;
                squeue.push(max);
            }
            smap[min]+=slot_num;
            smap[max]+=slot_num;
        }
        cout << "Case #" << c << ": " << max << " " << min << endl;
    }
    return 0;
}
