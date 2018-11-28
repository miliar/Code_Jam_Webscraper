#include<iostream>
#include<queue>
#include<set>
#include<map>
using namespace std;
void p(long long _) {
    long long n, k;
    cin >> n >> k;
    map<long long, long long> c;
    c[n] = 1;
    while(k > 0) {
        long long maxk = c.rbegin()->first;
        //cout << maxk << " " << c[maxk] << endl;
        if(c[maxk] < k) {
            k -= c[maxk];
            if((maxk - 1) / 2 > 0)
                if(c.find((maxk - 1) / 2) != c.end()) c[(maxk - 1) / 2] += c[maxk];
                else    c[(maxk - 1) / 2] = c[maxk];
            if(maxk - 1 - (maxk - 1) / 2 > 0)
                if(c.find(maxk - 1 - (maxk - 1) / 2) != c.end()) c[maxk - 1 - (maxk - 1) / 2] += c[maxk];
                else    c[maxk - 1 - (maxk - 1) / 2] = c[maxk];
            c.erase(--c.end());
        } else {
            cout << "Case #" << _ << ": " << maxk - 1 - (maxk - 1) / 2 << " " << (maxk - 1) / 2;
            return;
        }
    }
}
int main() {
    long long t;
    cin >> t;
    for(long long i = 0; i < t; i ++) {
        p(i + 1);
        cout << endl;
    }
}
