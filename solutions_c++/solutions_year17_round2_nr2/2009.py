#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;

struct Node{
    vector<char> list;
    vector<int> nums;
    int color;
    bool operator< (const Node &r) const{
        return list.size() < r.list.size();
    }
};

map<int, int> colorMap;
char keys[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
map<char, int> colorIndices;
map<int, set<int>> can;
int r = 0, o = 1, y = 2, g = 3, b = 4, v = 5;
vector<int> colors(6, 0);

int main(){
    int t;
    cin >> t;
    colorIndices['R'] = 0;
    colorIndices['O'] = 1;
    colorIndices['Y'] = 2;
    colorIndices['G'] = 3;
    colorIndices['B'] = 4;
    colorIndices['V'] = 5;
    can[r] = {y, b, g};
    can[o] = {b};
    can[y] = {r, b, v};
    can[g] = {r};
    can[b] = {r, y, o};
    can[v] = {y};

    rep(times, t){
        int n;
        cin >> n;
        rep(i, 6)   cin >> colors[i];

        vector<set<int>> list(6);
        cout << "Case #" << times+1 << ": ";

        colors[b] -= colors[o];
        colors[r] -= colors[g];
        colors[y] -= colors[v];
        n -= colors[o] + colors[g] + colors[v];

        int maxC = max(colors[b], max(colors[r], colors[y]));
        if(colors[b] + colors[r] + colors[y] - maxC < maxC){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            vector<char> ans;
            int before = -1;
            for(int i = 0; i < n-2; i++){
                int mx;
                if(colors[r] <= colors[b] && colors[y] <= colors[b])      mx = b;
                else if(colors[b] <= colors[r] && colors[y] <= colors[r]) mx = r;
                else mx = y;
                if(mx == before){
                    if(mx == b){
                        if(colors[r] <= colors[y])  mx = y;
                        else                        mx = r;
                    }
                    else if(mx == r){
                        if(colors[b] <= colors[y])  mx = y;
                        else                        mx = b;
                    }
                    else{
                        if(colors[r] <= colors[b])  mx = b;
                        else                        mx = r;
                    }
                }

                before = mx;
                if(mx == b){
                    ans.push_back(keys[b]);
                    colors[b]--;
                    if(0 < colors[o]){
                        ans.push_back(keys[o]);
                        ans.push_back(keys[b]);
                        colors[o]--;
                    }
                }
                else if(mx == r){
                    ans.push_back(keys[r]);
                    colors[r]--;
                    if(0 < colors[g]){
                        ans.push_back(keys[g]);
                        ans.push_back(keys[r]);
                        colors[g]--;
                    }
                }
                else{
                    ans.push_back(keys[y]);
                    colors[y]--;
                    if(0 < colors[v]){
                        ans.push_back(keys[v]);
                        ans.push_back(keys[y]);
                        colors[v]--;
                    }
                }
            }
            if(colors[r] == 0){
                if(colorIndices[ans[0]] == b){
                    ans.push_back(keys[b]);
                    ans.push_back(keys[y]);
                }
                else{
                    ans.push_back(keys[y]);
                    ans.push_back(keys[b]);
                }
            }
            else if(colors[b] == 0){
                if(colorIndices[ans[0]] == r){
                    ans.push_back(keys[r]);
                    ans.push_back(keys[y]);
                }
                else{
                    ans.push_back(keys[y]);
                    ans.push_back(keys[r]);
                }
            }
            else{
                if(colorIndices[ans[0]] == b){
                    ans.push_back(keys[b]);
                    ans.push_back(keys[r]);
                }
                else{
                    ans.push_back(keys[r]);
                    ans.push_back(keys[b]);
                }
            }
            for(auto e : ans)   cout << e;
            cout << endl;
        }


    }

    return 0;
}
