#include <stdio.h>
#include <map>
#define lli long long int
using namespace std;

struct elem {
    lli left;
    lli right;

    elem() {}
    elem(lli left, lli right):left(left), right(right) {}
};

map <elem, lli> mapa;

bool operator <(const elem &a, const elem &b) {
    return a.right - a.left > b.right - b.left;
}

int main(void) {
    int t;
    lli n, k;
    lli r1, r2;
    r1 = r2 = 0;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        lli got = 0;
        mapa.clear();
        scanf(" %lld %lld", &n, &k);
        mapa[elem(1, n + 2)]++;

        while(got < k) {
            elem aux = (*mapa.begin()).first;
            lli qt =(*mapa.begin()).second;
            lli a = (aux.left + aux.right) / 2;
            mapa.erase((*mapa.begin()).first);
            mapa[elem(aux.left, a)] += qt;
            mapa[elem(a, aux.right)] += qt;

            if (got + qt >= k) {
                mapa[elem(aux)] = 1;
            }
            got += qt;
            if (got >= k) {
                aux = (*mapa.begin()).first;
                r1 = (aux.right - aux.left - 1) / 2;
                r2 = (aux.right - aux.left - 2) / 2;
                break;
            }
        }
        printf("Case #%d: %lld %lld\n", caso, r1, r2);
    }
    return 0;
}
