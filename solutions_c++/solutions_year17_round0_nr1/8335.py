#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;
using vb = vector<bool>;
int solve(const vb &str, int k){
    set<vb> visited;
    queue<pair<int, vb>> frontier;
    frontier.push(make_pair(0, str));
    while(!frontier.empty()){
        auto obj = frontier.front();
        vb fstr = obj.second;
        int len = obj.first;
        frontier.pop();
        bool found = false;
        for(int i = 0; i < fstr.size(); ++i){
            if(!fstr[i]){
                found = true;
                for(int j = -k + 1; j <= 0; ++j){
                    int start = i + j;
                    int end = i + j + k - 1;
                    if(start >= 0 && end < fstr.size()){
                        vb fstr1(fstr);
                        for(int m = start; m <= end; ++m){
                            fstr1[m] = !fstr1[m];
                        }
                        if(visited.count(fstr1)  == 0){
                            frontier.push(make_pair(len+1, fstr1));
                            visited.insert(fstr1);
                        }       
                    }
                }
            }
        }
        if(!found){
            return len;
        }
    }
    return -1;
}

int main(){
    size_t T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        string str;
        int k;
        cin >> str >> k;
        size_t n = str.size();
        vb strvb(n, true);
        for(int i =0; i < n; ++i){
            if(str[i] == '-'){
                strvb[i] = false;
            }
        } 
        int ret = solve(strvb, k);
        if(ret < 0){
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << t << ": " << ret << endl;
        }
    }
}

