#include <stdio.h>
#include <vector>
#include <map>
#include <queue>
#include <string.h>
using namespace std;

const int MAXN = 102;
const int MAX_MOD = 5;

int mod[5];
int n, p;
vector <int> state(5, 0);
map <vector <int>, int> mapa;

int solve(vector <int> a) {
    int done = 1;
    for (int i = 1; i < p; i++) {
        if (a[i] != 0) {
            done = 0;
            break;
        }
    }

    if (done) {
        return 0;
    }
    if (mapa.find(a) != mapa.end()) {
        return mapa[a];
    }

    /*printf("debug\n");
    for (int i = 0; i < (int)a.size(); i++) {
        printf("%d ", a[i]);
    }
    printf("\nend debug\n"); */
    int res = 0;
    for (int i = 1; i < p; i++) {
        int n_mod = (a[0]+ i) % p;
        if (a[i] > 0) {
            vector <int> aux = a;
            aux[0] = n_mod;
            aux[i]--;
            res = max(res, (a[0] == 0) + solve(aux));
            aux[i]++;
        }
    }

    mapa[a] = res;
    return res;
}

int main(void) {
    int t;
    int x;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d", &n, &p);
        for (int i = 0; i < 5; i++) {
            mod[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            scanf(" %d", &x);
            mod[x % p]++;
        }

        vector <int> aux(5, 0);
        for (int i = 0; i < 5; i++) {
            aux[i] = mod[i];
        }
        aux[0] = 0;

        mapa.clear();
        int res = mod[0] + solve(aux);
        printf("Case #%d: %d\n", caso, res);
    }

    return 0;
}
