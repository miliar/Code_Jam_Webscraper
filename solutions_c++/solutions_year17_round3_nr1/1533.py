#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

const long double PI = 3.141592653589793238L;

class Pancake{
public:
    long long int r;
    long long int h;
    Pancake (long long int r, long long int h) {
        this->r = r;
        this->h = h;
    }
    long long int area() {
        return r * r;
    }
    long long int cyl() {
        return 2.0 * r * h;
    }
};

bool compare(Pancake* a, Pancake* b) {
    return a->cyl() < b->cyl();
}

bool compare2(Pancake* a, Pancake* b) {
    return a->r < b->r;
}

int main() {
    fstream cin("A-large-in.txt", fstream::in);
    fstream cout("A-large-out.txt", fstream::out);

    int t; cin >> t;
    for (int c = 1; c <= t; c++) {
        int n, k; cin >> n >> k;
        Pancake* P[n];
        for (int i = 0; i < n; i++) {
            int r, h; cin >> r >> h;
            P[i] = new Pancake(r, h);
        }
        sort(P, P+n, compare2);
        sort(P, P+k, compare);
        int maxr = 0, maxri;
        for (int i = 0; i < k; i++) {
            if (P[i]->r > maxr) {
                maxr = P[i]->r;
                maxri = i;
            }
        }
        for (int i = k; i < n; i++) {
            for (int j = 0; j < k; j++) {
                if (P[i]->area() + P[i]->cyl() > P[maxri]->area() + P[j]->cyl()) {
                    P[j] = P[i];
                    maxr = 0;
                    sort(P, P+k, compare);
                    for (int i = 0; i < k; i++) {
                        if (P[i]->r > maxr) {
                            maxr = P[i]->r;
                            maxri = i;
                        }
                    }
                    break;
                }
            }
        }

        double out = P[maxri]->area();
        for (int i = 0; i < k; i++) {
            out += P[i]->cyl();
        }
        cout << "Case #" << c << ": " << setprecision(9) << fixed << (PI * out) << endl;
    }

    return 0;
}
