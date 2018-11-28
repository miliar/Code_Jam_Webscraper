#include <bits/stdc++.h>

using namespace std;

int minix=-1, n, w;

bool complete(vector<bool> const &str){
    for(char c: str) if(!c) return false;
    return true;
}

void dfs(vector<bool> state, int d, int l){
    if(complete(state)) {
        if(minix == -1 || minix > d) minix = d;
        return;
    }
    if(l+w > n) return;
    for(int i=0; i<w; i++)
        state[l+i] = !state[l+i];
    dfs(state, d+1, l+1);
    for(int i=l+1; i+w <= n; i++){
        state[i-1] = !state[i-1];
        state[i+w-1] = !state[i+w-1];
        dfs(state, d+1, i+1);
    }



}

int main(){
    int t;
    cin >> t;
    string str;
    vector<bool> state;
    for(int i=1; i<=t; i++){
        minix = -1;
        cin >> str >> w;
        state.resize(n = str.size());
        for(int i=0; i<str.size(); i++)
            state[i] = str[i]=='+';
        dfs(state, 0, 0);
        cout << "Case #" << i << ": ";
        if(minix == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << minix << endl;

    }

    return 0;
}


