#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

double readprob() {
    double x;
    cin >> x;
    return x;
    //double a, b;
    //char dot;
    //cin >> a >> dot >> b;
    //return a * 10000 + b;
}

void doit() {
    int N, K;
    cin >> N >> K;
    double U;
    U = readprob();
    vector<double> P(N);

    double needed = 10000 * N;
    for (int i = 0; i < N; ++i) {
        double Pi = readprob();
        P[i] = Pi;
        needed -= Pi;
    }

    if (K != N) {
        cout << "INVALID" << endl;
        return;
    }

    sort(P.begin(), P.end());

    double uleft = U;
    for (int i = 0; i < N-1; ++i) {
        double pdiff = (P[i+1] - P[i]);
        double tospend = uleft / (i+1);
        double add = min(pdiff, tospend);
        //cerr << "Adding " << add << endl;
        for (int j = 0; j <= i; ++j) {
            P[j] += add;
            //cerr << "P[" << j << "] = " << P[j] << endl;
        }
        uleft -= add * (i+1);
    }

    for (int i = 0; i < N; ++i) {
        P[i] += uleft / N;
    }

    double c = 1.0;
    for (int i = 0; i < N; ++i) {
        //cerr << i << " " << P[i] << endl;
        c *= P[i];
    }
    cout << c << endl;
}

int main() {
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
