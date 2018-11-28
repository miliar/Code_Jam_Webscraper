#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

string flip(const string &S, const int &idx, const int &K) {
    string T = S;
    for(int i = 0; i < K; ++i) {
        if((idx+i) >= S.size())
            cout << "NOOOOOOOOOO" << endl;
        if(S[idx+i] == '-')
            T[idx+i] = '+';
        else
            T[idx+i] = '-';
    }
    return T;
}

int main() {
    int T, K;
    int n;
    string S;
    cin >> T;
for(int kase = 1; kase <= T; ++kase) {
    cin >> S >> K;
    n = (int)S.size();
    unordered_map<string,int> d;
    d[S] = 0;
    queue<string> q;
    q.push(S);
    while(!q.empty()) {
        string u = q.front();
        q.pop();
        for(int i = 0; i <= n-K; ++i) {
            string v = flip(u,i,K);
            if(d.count(v) == 0) {
                d[v] = d[u] + 1;
                q.push(v);
                //cout << v << endl;
            }
        }
    }
    string goal;
    for(int i = 0; i < n; ++i)
        goal += "+";
    cout << "Case #" << kase << ": ";
    if(d.count(goal) == 0)
        cout << "IMPOSSIBLE" << endl;
    else
        cout << d[goal] << endl;
}
    return 0;
}
