#include "bits.h"
using namespace std;

typedef long long ll;

double min(double a, double b) {
    return a < b ? a : b;
}

double doIt(pair<ll,ll> currentHorse, const vector<ll> &D, const vector<pair<ll,ll> > &horses, int startIndex, map<pair<pair<ll,ll>, int>, double> &memoTable) {
    if (startIndex == D.size()) return 0;
    if (memoTable[make_pair(currentHorse, startIndex)] != 0) {
        return memoTable[make_pair(currentHorse, startIndex)];
    }
    
    // Keep our horse
    double keepTime;
    if (currentHorse.first >= D[startIndex]) {
        double time = D[startIndex] / double(currentHorse.second);
        currentHorse.first -= D[startIndex];
     //   cerr << "**" << time << endl;
        keepTime = time + doIt(currentHorse, D, horses, startIndex+1, memoTable);
    } else { 
        keepTime = numeric_limits<double>::infinity();
    }
    
    // Use the new horse
    double newTime;
    pair<ll,ll> newHorse = horses[startIndex];
    double time = D[startIndex] / double(newHorse.second);
    newHorse.first -= D[startIndex];
    //cerr << "**" << time << endl;
    newTime = time + doIt(newHorse, D, horses, startIndex+1, memoTable);

    double ans = min(keepTime, newTime);
    memoTable[make_pair(currentHorse, startIndex)] = ans;
    return ans;
}

void solve() {
    int N,Q; cin >> N >> Q;

    vector<pair<ll,ll> > horses;
    for (int i = 0; i < N; i++) {
        ll E,S; cin >> E >> S;
        horses.push_back(make_pair(E,S));
    }

    vector<ll> D;
    for (int i = 0; i < N*N; i++) {
        ll newD; cin >> newD;
        if (newD != -1) {
            D.push_back(newD);
        }
    }

    int U,V; cin >> U >> V;

    pair<ll,ll> currentHorse = horses[0];
    double time = D[0] / double(currentHorse.second);
    currentHorse.first -= D[0];
    //cerr << "*" << time << endl;
    map<pair<pair<ll,ll>, int>, double> memoTable;
    cout << setprecision(12) << time + doIt(currentHorse, D, horses, 1, memoTable);
}

int main() {
    int T; cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
