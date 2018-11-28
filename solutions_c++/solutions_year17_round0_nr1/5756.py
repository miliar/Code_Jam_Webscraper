#include<bits/stdc++.h>
#define inf 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define MAX_BITS 10 
using namespace std;

int T, N, K;
unordered_map< bitset<MAX_BITS>, int>dp;

bitset<MAX_BITS> reverse(const bitset<MAX_BITS> &set) {
    bitset<MAX_BITS> result;
    for(int i = 0; i < MAX_BITS; i++){
        result[i] = set[MAX_BITS - i - 1];
    }
    return result;
}


string pancakes_repr(const bitset<MAX_BITS> &set){
    string ret(MAX_BITS-2,'-');
    for(int i = 0;i < MAX_BITS-2;i++){
        if(set[i]){
            ret[i]='+';
        }
    }
    return ret;
}
int bfs(bitset<MAX_BITS> state){
    queue< pair< bitset<MAX_BITS>,int> >q;
    q.push(mp(state, 0));
    dp[state] = 0;
    while(!q.empty()){
        pair< bitset<MAX_BITS> ,int> st = q.front();
        q.pop();
        //cout << pancakes_repr(st.first) << " " << st.second << endl;
        for(int i = 0;i < N;i++){
            if(i+K <= N){
                bitset<MAX_BITS>nst= st.first;
                for(int j = i;j < i+K;j++){
                    nst[j] = 1-nst[j];
                }
                if(!dp.count(nst) || dp[nst] > 1+st.second){
                    dp[nst] = 1+st.second;
                    q.push(mp(nst, 1+st.second));
                }
            }
        }
    }
    bitset<MAX_BITS> fs; 
    for(int i = 0;i < N;i++)fs[i] = 1; 
    return dp.count(fs) ? dp[fs]:inf;
}


int main(){
    cin >> T;
    for(int t = 1; t <= T;t++){
        string state;
        cin >> state >> K;
        N = state.size();
        bitset<MAX_BITS>bs;
        for(int i = 0;i < N;i++){
            bs[i] = (state[i] == '+');
        }
        int ans = bfs(bs);
        //int ans = bfs(state);
        if (ans != inf)
            cout << "Case #" << t << ": " << ans << endl;
        else
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        dp.clear();
    }
    return 0;
}
