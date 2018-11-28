#include <iostream>
#include <string>
#include <map>

using namespace std;
typedef unsigned long long ull;
void f(ull cc, ull k){
    map<ull,ull> m;
    m[cc] = 1;
    k--;
    while (k) {
        auto r = m.rbegin();
        if ( k < r->second ) break;
        ull cnt = r->second;
        ull w = r->first;
        m.erase(w);
        if (w==1) {

        }
        else if (w % 2 == 0) {
            m[w/2]+= (cnt);
            m[w/2-1]+= (cnt);
        }
        else {
            m[w/2] += (cnt *2);
        }
        k -= cnt;
/*        printf("\n", k);
        for (auto t:m) {
            printf("%lld,%lld \t", t.first, t.second);
        }
        printf("%lld\n", k);*/

    }
    printf("%lld %lld\n", m.rbegin()->first/2, (m.rbegin()->first-1)/2);
}
int main() {
    int nn;
    cin >> nn;
    for (int i = 1 ; i <= nn; i++) {
        printf("Case #%d: ",i);
        unsigned long long cc, k;
        cin >> cc >> k;
        f(cc,k);
    }
}
