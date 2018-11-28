#include<iostream>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef vector<int> State;
const int BUF = 105;
const int INF = 1<<30;

int N, P;
int group[BUF];

void read() {
    cin >> N >> P;
    for (int i = 0; i < N; ++i) {
        cin >> group[i];
    }
}


int rec(int remain, State &st, map<State, int> dp[4]) {
    
    if (dp[remain].count(st)) {
        return dp[remain][st];
    }
    if (count(st.begin(), st.end(), 0) == P) {
        return dp[remain][st] = 0;
    }
    
    int minV = INF;
    for (int i = 0; i < P; ++i) {
        if (st[i] > 0) {
            --st[i];
            minV = min(minV, rec((remain + P - i) % P, st, dp) + (remain > 0));
            ++st[i];
        }
    }

    return dp[remain][st] = minV;
}


void work(int cases) {
    State init(P, 0);
    for (int i = 0; i < N; ++i) {
        ++init[group[i] % P];
    }
    
    map<State, int> dp[4];
    
    cout << "Case #" << cases << ": " << N - rec(0, init, dp) << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
