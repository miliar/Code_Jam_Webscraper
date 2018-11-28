#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;


void solve(int t){
    set<string> searched;
    queue< pair<string, int> > q;
    string S, s1, s2, s_ans;
    int K, N, d;
    bool possible = false;

    cin >> S >> K;
    N = S.size();
    q.push(make_pair(S, 0));
    s_ans = "";
    for(int i=0; i<N; i++) s_ans += '+';

    while(!q.empty()){
        s1 = q.front().first;
        d = q.front().second;
        q.pop();

        if(s1 == s_ans){
            cout << "Case #" << t << ": " << d << endl;
            possible = true;
            break;
        }
        else{
            for(int i=0; i<=N-K; i++){
                s2 = s1;
                for(int j=i; j<i+K; j++){
                    if(s2[j] == '+') s2[j] = '-';
                    else if(s2[j] == '-') s2[j] = '+';
                }
                if(searched.find(s2) == searched.end()){
                    searched.insert(s2);
                    q.push(make_pair(s2, d+1));
                }
                // cout << s2 << " " << d+1 << endl;
            }
        }
    }
    if(!possible){
        cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
}

int main(){
    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        solve(t);
    }
}
