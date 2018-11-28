#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <bitset>
#include <set>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

map<vector<bool>,int64_t> mem;
map<vector<bool>,bool> seen;
int T, K, S;

int64_t solve(vector<bool> &b){
    if(mem.find(b) != mem.end()){
        return mem[b];
    }

    for(int i = 0; i < (S-K); i++){
        for(int j = i; j < i+K; j++){
            b[j].flip();
        }

    }
}

bool done(vector<bool> &b){
    bool res = true;
    for(int i = 0; i < b.size(); i++){
        res &= b[i];
    }
    return res;
}

int main()
{
    cin >> T;
    int cnt = 0;
    while(T--){
        cnt++;
        string s;
        cin >> s;
        S = s.size();
        vector<bool> b (S);
        for(int i = 0; i < s.size(); i++){
            b[i] = (s[i] == '+');
        }

        cin >> K;
        queue<vector<bool> > Q;
        int ans = -1;
        mem[b] = 0;
        Q.push(b);
        while(!Q.empty()){
            vector<bool> b = Q.front();
            Q.pop();
            if(done(b)){
                ans = mem[b];
                break;
            }
            if(seen[b]) continue;
            seen[b] = true;

            for(int i = 0; i < S-K+1; i++){
                vector<bool> c = b;
                for(int j = i; j < K+i; j++){
                    c[j] = !c[j];
                }
                if(seen[c]) continue;
                mem[c] = mem[b] + 1;
                Q.push(c);
            }
        }
        cout << "Case #" << cnt << ": ";
        if(ans == -1){
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
        mem.clear();
        seen.clear();
    }
    return 0;
}
