//
// Created by 007 on 09.04.2017.
//
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <list>
#include <fstream>
#include <queue>

using namespace std;

int main() {
    ifstream myReadFile;
    myReadFile.open("C:\\Users\\007\\CLionProjects\\untitled\\text.txt");
    ofstream myReadFile1;
    myReadFile1.open("C:\\Users\\007\\CLionProjects\\untitled\\text1.txt");
    int t;
    myReadFile >> t;
    for(int i = 0; i < t; ++i) {
        long long k;
        long long n;
        myReadFile >> n >> k;
        priority_queue<long long> ranges;
        ranges.push(n);
        long long mi, ma;
        for(int j = 0; j < k; ++j)
        {
            long long cur_r = ranges.top();
            ranges.pop();
            mi = (cur_r - 1) / 2;
            ma = mi + (cur_r - 1) % 2;
            ranges.push(ma);
            ranges.push(mi);
        }
        myReadFile1 << "Case #" << i + 1 << ": " << ma << " " << mi << endl;
    }
    return 0;
}
