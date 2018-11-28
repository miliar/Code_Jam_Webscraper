#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define fori(i, n) for (int i = 0; i < (int)(n); ++i)
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define DEBUG
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

char ryb[3];
char ogv[3];
int RYB[3];
int OGV[3];
int neigh[3];
deque<string> A[3];
int N;

void mysort(char a[3], int b[3]) {
    if (b[1] < b[2]) {
        swap(b[1], b[2]);
        swap(a[1], a[2]);
    }
    if (b[0] < b[1]) {
        swap(b[0], b[1]);
        swap(a[0], a[1]);
    }
    if (b[1] < b[2]) {
        swap(b[1], b[2]);
        swap(a[1], a[2]);
    }
}

void mysort(deque<string> A[3]) {
    if (A[1].size() < A[2].size()) {
        swap(A[1], A[2]);
    }
    if (A[0].size() < A[1].size()) {
        swap(A[0], A[1]);
    }
    if (A[1].size() < A[2].size()) {
        swap(A[1], A[2]);
    }
}

void mymap() {
    fori(i, 3) {
        char &a = ogv[i];
        switch (a) {
            case 'O':
                fori(j, 3) {
                    if (ryb[j] == 'B') {
                        neigh[i] = j;
                        break;
                    }
                }
                break;
            case 'G':
                fori(j, 3) {
                    if (ryb[j] == 'R') {
                        neigh[i] = j;
                        break;
                    }
                }
                break;
            case 'V':
                fori(j, 3) {
                    if (ryb[j] == 'Y') {
                        neigh[i] = j;
                        break;
                    }
                }
                break;
        }
    }
}

string genBOB(char a, char b, int m, bool flag) {
    string out;
    out.resize(2*m + flag);
    char ch = a;
    fori(i, out.size()) {
        out[i] = ch; // ababababa
        ch = (ch == a)? b: a;
    }
    return out;
}

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif

    int i, j, k;
    int T, TT;
    cin >> TT;
    for (T = 1; T <= TT; T++)
    {
        printf("Case #%d: ", T);
        ryb[0] = 'R'; ryb[1] = 'Y'; ryb[2] = 'B';
        ogv[0] = 'O'; ogv[1] = 'G'; ogv[2] = 'V';
        A[0].clear(); A[1].clear(); A[2].clear();

        cin >> N;
        cin >> RYB[0] >> OGV[0] >> RYB[1] >> OGV[1] >> RYB[2] >> OGV[2];
        mysort(ryb, RYB);
        mysort(ogv, OGV);
        mymap();

        #ifdef DEBUG1
            cout << endl;
            for(auto a: ryb) cout << a; cout << endl;
            for(auto a: RYB) cout << a << ' '; cout << endl;
            for(auto a: ogv) cout << a; cout << endl;
            for(auto a: OGV) cout << a << ' '; cout << endl;
            for(auto a: neigh) cout << a; cout << endl;
        #endif

        if (OGV[1] == 0) {
            // only one of OGV
            int j = neigh[0];
            if (RYB[j] < OGV[0]) {
                printf("IMPOSSIBLE\n");
                continue;
            } else if (RYB[j] == OGV[0]) {
                if (RYB[1] == 0){
                    // only one of RYB
                    cout << genBOB(ryb[j], ogv[0], OGV[0], false) << endl;
                    continue;
                } else {
                    printf("IMPOSSIBLE\n");
                    continue;
                }
            }
        }
        // other cases
        int j;
        char a, b;
        fori(i, 3) {
            a = ogv[i];
            j = neigh[i];
            b = ryb[j];
            if (OGV[i] > 0) {
                RYB[j] = RYB[j] - OGV[i] - 1;
                if (RYB[j] < 0) {
                    printf("IMPOSSIBLE\n");
                    break;
                }
                A[i].push_back(genBOB(b, a, OGV[i], true));
            }
            fori(k, RYB[j]) {
                A[i].push_back(string(1, b));
            }
        }
        if (RYB[j] < 0) {
            continue;
        }

        mysort(A);
        #ifdef DEBUG1
            cout << endl;
            for(auto a: A) cout << a.size() << ' '; cout << endl;
        #endif



        if (A[0].size() > A[1].size() + A[2].size()) {
            printf("IMPOSSIBLE\n");
            continue;
        } else {
            int len = A[1].size() + A[2].size() - A[0].size(); // !!!
            fori(i, len) {
                string a = A[2].back();
                string b = A[1].front();
                string c = b + a;
                A[2].pop_back();
                A[1].pop_front();
                A[1].push_back(c);
            }
            auto it = A[0].begin();
            #ifdef DEBUG1
                cout << A[1].size() + A[2].size() - A[0].size() << endl;
            #endif
            for(auto a: A[1]) {
                cout << a;
                cout << *it;
                it++;
            }
            for(auto a: A[2]) {
                cout << a;
                cout << *it;
                it++;
            }
            printf("\n");
        }
    }
	return 0;
}
