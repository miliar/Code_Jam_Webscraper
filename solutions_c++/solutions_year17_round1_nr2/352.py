#include <bits/stdc++.h>
using namespace std;
            
            

int get_min(vector<vector<pair<int, int> > > &packs, vector<int> &pos) {
    int res = -1000000000;
    for (unsigned int i = 0; i<pos.size(); i++){
        if (pos[i] == (int) packs[i].size()) {
            return 1000000000;
        }
        res = max(res, packs[i][pos[i]].second);
    }
    return res;
}

int get_max(vector<vector<pair<int, int> > > &packs, vector<int> &pos) {
    int res = 1000000000;
    for (unsigned int i = 0; i<pos.size(); i++){
        if (pos[i] == (int) packs[i].size()) {
            return -1000000000;
        }
        res = min(res, packs[i][pos[i]].first);
    }
    return res;
}

// excluding value
void rem_until(vector<vector<pair<int, int> > > &packs, vector<int> &pos, int val){
    for (unsigned int i=0; i<pos.size(); i++){
        while (pos[i] < (int) packs[i].size() && packs[i][pos[i]].first < val){
            pos[i]++;
        }
    }
}

void solve(){
    int res = 0;
    int N; //ingredients
    int P; // packages for each ingredient
    cin >> N >> P;
    vector<int> ing = vector<int>(N, 0);
    for (int i=0; i<N; i++){
        cin >> ing[i];
    }
    
    vector<vector<pair<int, int> > > packs = vector<vector<pair<int, int> > >(N, vector<pair<int, int> >());
    for (int i=0; i<N; i++){
        for (int j=0; j<P; j++){
            int val;
            cin >> val;
            int maxi = (10 * val) / (9 * ing[i]);
            int mini = (10 * val) / (11 * ing[i]);
            if ((10 * val) % (11 * ing[i]) != 0){
                mini++;
            }
            if (mini <= maxi) {
                packs[i].push_back(make_pair(maxi, mini));
            }
        }
        sort(packs[i].begin(), packs[i].end());
    }
    
    vector<int> pos = vector<int>(N, 0);
    
    int mini = 0, maxi = 0;
    mini = get_min(packs, pos);
    maxi = get_max(packs, pos);
    while (mini != 1000000000){
        if (mini > maxi){
            rem_until(packs, pos, maxi + 1);
        } else {
            res++;
            for (unsigned int i=0; i<pos.size(); i++){
                pos[i]++;
            }
        }
        mini = get_min(packs, pos);
        maxi = get_max(packs, pos);
    }
    cout << res << endl;
}
    
    
    

int main(){
    int T;
    cin >> T;
    for (int i=1; i<=T; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}
    
