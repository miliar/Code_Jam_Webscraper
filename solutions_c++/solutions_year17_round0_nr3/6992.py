//
//  main.cpp
//  CodeJam.0.Stalls
//
//  Created by David Song on 4/8/17.
//  Copyright © 2017 David Song. All rights reserved.
//

#include <iostream>
#include <vector>
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::sort;

vector<int> stalls(vector<int> v, int k) {
    if (k == 1) {
        vector<int> m(2, 0);
        sort(v.begin(), v.end());
        //for (int i = 0; i < v.size(); i++) {
        //    cout << v[i] << endl;
        //}
        if (v[v.size() - 1] == 0) {
            m[0] = 0;
            m[1] = 0;
        } else if ((v[v.size() - 1]) % 2 == 0) {
            m[0] = v[v.size() - 1] / 2;
            m[1] = v[v.size() - 1] / 2 - 1;
        } else {
            m[0] = v[v.size() - 1] / 2;
            m[1] = v[v.size() - 1] / 2;
        }
        return m;
    } else {
        sort(v.begin(), v.end());
        if (v[v.size() - 1] == 0) {
            v[v.size() - 1] = 0;
            v.push_back(0);
        } else if (v[v.size() - 1] % 2 == 0) {
            v.push_back(v[v.size() - 1] / 2 - 1);
            v[v.size() - 2] /= 2;
        } else {
            v.push_back(v[v.size() - 1] / 2);
            v[v.size() - 2] /= 2;
        }
        return stalls(v, k-1);
    }
}

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, k;
        cin >> n >> k;
        if (n == k) {
            cout << "Case #" << i + 1 << ": 0 0" << endl;
        } else {
            vector<int> v (1, n);
            cout << "Case #" << i + 1 << ": " << stalls(v, k)[0] << " " << stalls(v, k)[1] << endl;
        }

    }
}
