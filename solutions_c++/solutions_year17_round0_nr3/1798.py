//
// Created by Denis Mukhametianov on 08.04.17.
//

#include <iostream>
#include <set>
#include <map>


using namespace std;


set<long long> st;
map<long long, long long> counter;


void solveC(int testNumber) {
    st.clear();
    counter.clear();
    long long n, k;
    cin >> n >> k;
    st.insert(-n);
    counter[n] = 1;
    int iterations = 0;
    while (true) {
        iterations++;
        long long biggest = -*st.begin();
        long long count = counter[biggest];
        long long a = (biggest - 1) / 2;
        long long b = biggest - 1 - a;
        if (count < k) {
            k -= count;
            if(a != 0) {
                st.insert(-a);
                counter[a] += count;
            }
            if(b != 0) {
                st.insert(-b);
                counter[b] += count;
            }
            st.erase(st.begin());
            continue;
        } else {
            printf("Case #%d: %lld %lld\n", testNumber, b, a);
            break;
        }
    }
    fprintf(stderr, "%d\n", iterations);
}


void runC() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++) {
        solveC(i + 1);
    }
}