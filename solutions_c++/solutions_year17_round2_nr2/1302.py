 #include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

const string S = "RYBGVO";
int N;

string solve(vector<int> rem, int start){
    int prev_idx = start;
    string res = "";
    for(int i=0; i<N; i++){
        if(prev_idx>=3){
            prev_idx -= 3;
            res += S[prev_idx];
            rem[prev_idx]--;
            continue;
        }
        if(prev_idx >= 0 && rem[prev_idx+3]>0){
            prev_idx += 3;
            rem[prev_idx]--;
            res += S[prev_idx];
            continue;
        }
        int max_idx = -1;
        REP(j, 3){
            if(prev_idx==j)continue;
            if(max_idx==-1 || rem[max_idx] < rem[j]){
                max_idx = j;
            }
        }
        rem[max_idx]--;
        res += S[max_idx];
        prev_idx = max_idx;
    }
    bool ok = true;
    if(prev_idx>=3){
        ok = ok && (res[0]==S[prev_idx-3]);
    }else{
        ok = ok && (res[0]!=S[prev_idx]);
    }
    REP(i, 6){
        ok = ok && (rem[i]==0);
    }
    if(!ok)res = "";
    return res;
}

int main(){
    int T;
    cin >> T;
    REP(tc, T){
        int R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        vector<int> rem;
        rem.push_back(R);
        rem.push_back(Y);
        rem.push_back(B);
        rem.push_back(G);
        rem.push_back(V);
        rem.push_back(O);
        string res = "IMPOSSIBLE";
        REP(i, 3){
            string ans = solve(rem, i);
            if(ans.size()>0)res = ans;
        }
        cout << "Case #" << tc+1 << ": " + res << endl;
    }
    return 0;
}
