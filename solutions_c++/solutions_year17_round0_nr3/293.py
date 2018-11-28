#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>

using namespace std;

void doit() {
    long long N, K;
    cin >> N >> K;

    map<long long, long long> curlevel, nextlevel;

    long long left = K;
    curlevel[N] = 1;

    //cerr << "== New round! " << N << ' ' << K  << endl;
    while (left > 0) {
        //cerr << "== Left " << left << endl;
        for (auto it = curlevel.rbegin(); it != curlevel.rend(); ++it) {
            //cerr << "Size " << it->first << ", count " << it->second << endl;
            
            long long splitsize = it->first;
            long long splitcount = it->second;

            if (left <= splitcount) {
                if (splitsize % 2 == 1) {
                    cout << splitsize  / 2 << ' ' << splitsize / 2 << endl;
                }
                else {
                    cout << splitsize  / 2 << ' ' << splitsize /  2 -1 << endl;
                }
                return;
            }
            left -= splitcount;
            if (splitsize % 2 == 1) {
                nextlevel[(splitsize - 1) / 2] += splitcount * 2;
            }
            else {
                nextlevel[splitsize / 2] += splitcount;
                nextlevel[splitsize / 2 - 1] += splitcount;
            }
        }

        curlevel = nextlevel;
        nextlevel.clear();
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
