#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

bool checkImpossible(vector<bool> T, int K);
long BFS(vector<vector<bool>> T, unordered_set<vector<bool>> used, int K, long steps);


int main() {
    int S;
    cin >> S;
    for(int i = 0; i < S; i++){
        string T;
        int K;
        cin >> T >> K;
        int a = T.size();
        vector<bool> b;
        for(int j = 0; j < a; j++) b.push_back(T[j] == '+');
        //cout << "Input :";
        //for(int j = 0; j < a; j++) cout << b[j];
        //cout <<"\n";
        cout << "Case #" << i + 1 << ": ";
            //cout << "reached 1\n";
        vector<vector<bool>> A;
        unordered_set<vector<bool>> B;
        A.push_back(b);
        long tz = BFS(A, B, K, 0);
        if(tz >= 0) cout << tz << "\n";
        else cout << "Impossible\n";
        //cout << BFS(A, B, K, 0) << endl;
    }
    return 0;
}

bool winning(vector<vector<bool>> k) {
    long b = k[0].size();
    vector<bool> c;
    for(long i = 0; i < b; i++) c.push_back(true);
    return find(k.begin(), k.end(), c) != k.end();
}

vector<bool> flip(vector<bool> c, int start, int size) {
    for(int i = start; i < start + size; i++) {
        c[i] = !c[i];
    }
    return c;
}

long BFS(vector<vector<bool>> T, unordered_set<vector<bool>> used, int K, long steps) {
    //cout << "reached beginning of BFS " << steps << " \n";
    if(T.size() == 0) return -1;
    if(winning(T)) return steps;

    //cout << "past winning \n";
    long a = T.size();
    long b = T[0].size();
    //cout << a << " " << b - K << " " << a * (b - K + 1) <<  "\n";
    vector<vector<bool>> op;
    for(int i = 0; i < a; i++) {
        for(int j = 0; j <= b - K; j++) {
            vector<bool> c = flip(T[i], j, K);
            int w = 0;
            for(int r = 0; r < b; r++) w += !c[b];
            if(w == 1) return -1;
            if(find(used.begin(), used.end(), c) == used.end()) {
                used.insert(c);
                op.push_back(c);
            }
        }
    }
            //cout << "reached end of BFS " << steps << " \n";
    return BFS(op, used, K, steps + 1);
}