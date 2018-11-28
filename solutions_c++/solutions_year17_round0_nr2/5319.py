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

int64_t T, N, nine;
vector<int> start;
vector<int> ans;


bool dfs(vector<int> &pos, int p, int m){
    if(p >= start.size()) return true;
    if(pos[p] >= m){
        if( dfs(pos,p+1,pos[p]) ) return true;
        if( pos[p] == m) {
            nine = p;
            return false;
        }
        else { ans[p] = pos[p] - 1; }
    } else {
        nine = p;
        return false;
    }
}


int main()
{
    cin >> T;
    int cnt = 0;
    while(T--){
        cnt++;
        string s;
        cin >> s;
        vector<int> pos (s.size());


        for(int i = 0; i < s.size(); i++){
            pos[i] = (int)s[i] - (int)'0';
        }

        nine = pos.size();
        start = pos;
        ans = pos;

        cout << "Case #" << cnt << ": ";
        if(!dfs(pos, 0, 0)){
            for(int i = 0; i < pos.size() -1 ; i++){
                cout << 9;
            }
        } else {
            for(int i = 0; i < nine; i++){
                cout << ans[i];
            }
            for(int i = nine; i < pos.size(); i++){
                cout << 9;
            }
        }
        cout << endl;
    }
    return 0;
}
