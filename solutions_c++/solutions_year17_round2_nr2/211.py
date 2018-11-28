#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <limits>
#include <algorithm>
#include <utility>
#include <array>
#include <unordered_map>
#include <map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef long long ull;

ifstream inputStream;

int t;
int n;
int r;
int y;
int b;
int o;
int g;
int v;

bool fr;
bool fy;
bool fb;

char first;
char last;

void coutr() {
    last = 'R';
    if(first == 'x') first = last;
    cout << last;
}

void couty() {
    last = 'Y';
    if(first == 'x') first = last;
    cout << last;
}

void coutb() {
    last = 'B';
    if(first == 'x') first = last;
    cout << last;
}

void couto() {
    last = 'O';
    if(first == 'x') first = last;
    cout << last;
}

void coutg() {
    last = 'G';
    if(first == 'x') first = last;
    cout << last;
}

void coutv() {
    last = 'V';
    if(first == 'x') first = last;
    cout << last;
}

void printr() {
    if(fr) {
        coutr();
        for(int i=0; i<g; i++) {
            coutg();
            coutr();
        }
        fr = false;
    } else {
        coutr();
    }
}

void printy() {
    if(fy) {
        couty();
        for(int i=0; i<v; i++) {
            coutv();
            couty();
        }
        fy = false;
    } else {
        couty();
    }
}

void printb() {
    if(fb) {
        coutb();
        for(int i=0; i<o; i++) {
            couto();
            coutb();
        }
        fb = false;
    } else {
        coutb();
    }
}

void solve(int t) {
    cout << "Case #" << t << ": ";

    inputStream >> n >> r >> o >> y >> g >> b >> v;
    fr = true;
    fy = true;
    fb = true;
    first = 'x';
    last = 'y';

    if(o == 0 && y == 0 && b == 0 && v == 0) {
        if(r == g) {
            for(int i=0; i<r; i++) {
                coutr();
                coutg();
            }
        } else {
            cout << "IMPOSSIBLE";
        }
    } else if(r == 0 && g == 0 && y == 0 && v == 0) {
        if(b == o) {
            for(int i=0; i<b; i++) {
                coutb();
                couto();
            }
        } else {
            cout << "IMPOSSIBLE";
        }
    } else if(r == 0 && g == 0 && b == 0 && o == 0) {
        if(y == v) {
            for(int i=0; i<y; i++) {
                couty();
                coutv();
            }
        } else {
            cout << "IMPOSSIBLE";
        }
    } else if(o != 0 && o >= b) {
        cout << "IMPOSSIBLE";
    } else if(g != 0 && g >= r) {
        cout << "IMPOSSIBLE";
    } else if(v != 0 && v >= y) {
        cout << "IMPOSSIBLE";
    } else {

        b -= o;
        r -= g;
        y -= v;

        if(r == 0) {

            if(y == b) {
                for(int i=0; i<y; i++) {
                    printy();
                    printb();
                }
            } else {
                cout << "IMPOSSIBLE";
            }

        } else {

            if (r > 1 && y + b < r) {
                cout << "IMPOSSIBLE";
            } else if (y - b > r) {
                cout << "IMPOSSIBLE";
            } else if (b - y > r) {
                cout << "IMPOSSIBLE";
            } else {
                for (int i = 0; i < r - 1; i++) {
                    printr();
                    if (y > b) {
                        printy();
                        y--;
                    } else {
                        printb();
                        b--;
                    }
                }
                printr();
                if (y == b) {
                    for (int i = 0; i < b; i++) {
                        printy();
                        printb();
                    }
                } else if (y > b) {
                    printy();
                    y--;
                    for (int i = 0; i < b; i++) {
                        printb();
                        printy();
                    }
                } else {
                    printb();
                    b--;
                    for (int i = 0; i < b; i++) {
                        printy();
                        printb();
                    }
                }
            }

        }

    }

    cout << endl;
}

int main(int argc, char** argv) {

    if(argc == 1) {

    } else {
        inputStream = ifstream(argv[1]);
    }

    inputStream >> t;

    for(int i=0; i<t; i++) {
        solve(i + 1);
    }

}