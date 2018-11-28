//
//  bathroom.cpp
//  
//
//  Created by John Nevard on 4/8/17.
//
//

#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::cerr;
using std::vector;
using std::swap;

typedef vector<long> VL;

struct Gr {
    Gr(long g = 0, long r = 0) : g(g), r(r) { }
    
    long g, r;
};

typedef vector<Gr> VG;

/*
VL h(long ns, long np) {
    VL a;
    a.push_back(ns);
    long gl, gr;
    while (np) {
        int ng = a.size();
        int i0 = 0;
        for (int i = 1; i < ng; ++i)
            if (a[i] > a[i0])
                i0 = i;
        swap(a[i0], a[ng - 1]);
        gl = a[ng - 1];
        gr = gl - gl / 2 - 1;
        gl /= 2;
        a[ng - 1] = gl;
        a.push_back(gr);
        --np;
    }
    return VL {gl, gr};
}
*/

VL f(long ns, long np) {
    VG a;
    a.push_back(Gr {ns, 1});
    while (np) {
        Gr b = a[0];
        int i0 = 0;
        for (int i = 1; i < a.size(); ++i)
            if (a[i].g > a[i0].g)
                i0 = i;
        swap(a[0], a[i0]);
        long gl = a[0].g / 2;
        long gr = a[0].g - gl - 1;
        long nr = a[0].r;
        if (np > nr) {
            np -= nr;
            a[0].g = gl;
            if (gl == gr)
                a[0].r = 2 * nr;
            
            int k = -1;
            for (int j = 1; j < a.size() && k < 0; ++j)
                if (a[j].g == gl)
                    k = j;
            
            if (k >= 0) {
                a[0].r += a[k].r;
                a[k] = a[a.size() - 1];
                a.resize(a.size() - 1);
            }
            
            if (gl > gr) {
                k = -1;
                for (int j = 1; j < a.size() && k < 0; ++j)
                    if (a[j].g == gr)
                        k = j;
                if (k >= 0)
                    a[k].r += nr;
                else
                    a.push_back(Gr {gr, nr});
            }
        } else {
//            for (int j = 0; j < a.size(); ++j)
//                cout << a[j].g << ' ' << a[j].r << '\n';
//            cout << '\n';
            
            return VL {gl, gr};
        }
    }
}

int main() {
    int n_cases;
    cin >> n_cases;
    for (int i = 1; i <= n_cases; ++i) {
        long ns, np;
        cin >> ns >> np;
        VL p = f(ns, np);
        cout << "case #" << i << ": " << p[0] << ' ' << p[1] << '\n';
    }
    return 0;
}
