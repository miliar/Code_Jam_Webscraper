#include <iostream>
#include <string>
#include <queue>
#include <map>
using namespace std;

string flip(string cake, int where, int K) {
    string ret = cake;
    if(where+K>ret.size()) return "";

    for(int i=0;i<K;++i) {
        char &t = ret[i+where];
        if(t=='+') t = '-'; else t = '+';
    }
    return ret;
}

int solve(const string &cake, int K) {
    queue<string> que;
    que.push(cake);
    map<string,int> cnt;
    cnt[cake] = 0;

    const string goal = string(cake.size(), '+');
    //cerr << goal << endl;
    while(!que.empty()) {
        string top = que.front(); que.pop();
        //cerr << top << endl;
        if(top == goal) {
            return cnt[top];
        }
        for(int i=0;i+K<=top.size();++i) {
            string t = flip(top, i, K);
            // cerr << t << endl;
            if(cnt.count(t)>0) continue;
            cnt[t] = cnt[top]+1;
            que.push(t);
        }
    }

    return -1;
}

int main() {
    int ncase;
    cin >> ncase;
    for(int caseno=1;caseno<=ncase;++caseno) {
        string cake;
        int K;
        cin >> cake >> K;
        int ret = solve(cake,K);
        cout << "Case #";
        if( ret == -1 ) cout << caseno << ": IMPOSSIBLE" << endl;
        else cout << caseno << ": " << ret << endl;
    }

    return 0;
}
