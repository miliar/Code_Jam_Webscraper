//
//  main.cpp
//  Problem C Bathroom Stalls
//
//  Created by Parinthorn Saithong on 4/9/2017.
//  Copyright © 2017 Parinthorn Saithong. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cstdio>
#include <gmpxx.h>

using namespace std;

class Compare {
public:
    bool operator()(pair<mpz_class, mpz_class> n1, pair<mpz_class, mpz_class> n2) {
        return cmp(n1.first, n2.first) < 0 || (cmp(n1.first, n2.first) == 0 && cmp(n1.second, n2.second) > 0);
    }
};

void findTwoSideSpaceOfKthUser(mpz_class n, mpz_class k, mpz_class maxMinSpace[]) {
    priority_queue<pair<mpz_class, mpz_class>, vector<pair<mpz_class, mpz_class> >, Compare> pq;
    mpz_class zeroMpz(0);
    pq.push(make_pair(n, zeroMpz));
    mpz_class counter("0", 10);
    pair<mpz_class, mpz_class> left, right;
    while(cmp(counter, k) < 0) {
        pair<mpz_class, mpz_class> tmp;
        tmp = pq.top();
        mpz_class nSpace = tmp.first;
        mpz_class firstIndex = tmp.second;
        mpz_class nSpaceMinusOne = nSpace - 1;
        int compareRes = mpz_odd_p(nSpaceMinusOne.get_mpz_t());
        if(compareRes) {
            // odd
            left = make_pair(nSpaceMinusOne / 2, firstIndex);
            right = make_pair(nSpaceMinusOne / 2 + 1, firstIndex + nSpaceMinusOne / 2 + 1);
        } else {
            left = make_pair(nSpaceMinusOne / 2, firstIndex);
            right = make_pair(nSpaceMinusOne / 2, firstIndex + nSpaceMinusOne / 2 + 1);
        }
        // cout << "Left: " << left.first.get_mpz_t() << " " << left.second.get_mpz_t() << " ";
        // cout << "Right: " << right.first.get_mpz_t() << " " << right.second.get_mpz_t() << "\n";
        pq.pop();
        pq.push(left);
        pq.push(right);
        counter = counter + 1;
    }
    maxMinSpace[0] = right.first;
    maxMinSpace[1] = left.first;
}

int main(int argc, const char * argv[]) {
    int t, casei = 0;
    scanf("%d", &t);
    while(t--) {
        mpz_t _n, _k;
        mpz_class result[2];
        cin >> _n >> _k;
        mpz_class n = mpz_class(_n);
        mpz_class k = mpz_class(_k);
        findTwoSideSpaceOfKthUser(n, k, result);
        cout << "Case #" << ++casei << ": " << result[0].get_mpz_t() << " " << result[1].get_mpz_t() << "\n";
    }
    return 0;
}
