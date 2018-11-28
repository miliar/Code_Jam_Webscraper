#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int B = 1;
const int R = 2;
const int Y = 4;
const int O = R | Y;
const int G = B | Y;
const int V = R | B;

int n;
int in[8] = {0, };
int out[1000];
vector<vector<int>> cand;

bool ok() {
    int one = in[1] + in[3] + in[5];
    int two = in[2] + in[3] + in[6];
    int four = in[4] + in[5] + in[6];

    //cout << " :: " << one << " " << two << " " << four << endl;
    int maxi = max(max(one, two), four);
    return maxi <= n / 2; 
}

void find(int &a, int &b, int &c) {
    int one = in[1] + in[3] + in[5];
    int two = in[2] + in[3] + in[6];
    int four = in[4] + in[5] + in[6];

    if (one >= two && one >= four) {
        a = 1;
        if (two >= four) { b = 2; c = 4; }
        else { b = 4; c = 2; }
    } else if (two >= four) {
        a = 2;
        if (one >= four) { b = 1; c = 4; }
        else { b = 4; c = 1; }
    } else {
        a = 4;
        if (one >= two) { b = 1; c = 2; }
        else { b = 2; c = 1; }
    }
}

int go(int now, int index) { 
    auto &v = cand[now];
    for (int x : v) {
        while (0 < in[x]) {
            out[index] = x;
            in[x]--;
            index = (index + 2) % n;
            if (out[index] != -1) {
                index = (index + 1) % n;
            }
        }
    }
    return index;
}


void solve() {
    memset(out, 0xFF, sizeof(out));

    cin >> n;
    // B = 1, R = 10, Y = 100
    // R O Y G B V
    cin >> in[R] >> in[O] >> in[Y] >> in[G] >> in[B] >> in[V];

    if (ok()) {
        int a, b, c;
        find(a, b, c);
        //cout << "  --  " << a << " " << b << " " << c << endl;
        int next = go(a, 0);
        next = go(b, next);
        go(c, next);

        const char *P = "-BRVYGO";
        for (int i = 0; i < n; i++) {
            if (out[i] == -1) cout << " !!!!! " << i << endl;
            cout << P[out[i]];
        }
            cout << endl;
    }
    else {
        cout << "IMPOSSIBLE" << endl;
    }
}

void ready() {
    cand.resize(7);
    cand[1].push_back(1);
    cand[1].push_back(3);
    cand[1].push_back(5);

    cand[2].push_back(2);
    cand[2].push_back(3);
    cand[2].push_back(6);

    cand[4].push_back(4);
    cand[4].push_back(5);
    cand[4].push_back(6);
}

int main() {
    ready();
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

