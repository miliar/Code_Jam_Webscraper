#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <tuple>
typedef long long ll;

using namespace std;
int t,k;
string s;

void solve(int cas){
    cin >> s >> k;
    vector<bool> sides;
    int cnt = 0;
    for(char c: s){
        if(c=='+') sides.push_back(true);
        else sides.push_back(false);
    }
    for(int i=0; i<=sides.size()-k; i++){
        if(!sides[i]){
            ++cnt;
            for(int j=0; j<k; j++)sides[i+j] = !sides[i+j];
        }
    }
    cout << "Case #" << cas << ": ";
    for(bool u: sides){
        if(!u){
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << cnt << "\n";
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin >> t;
    for(int i=0; i<t; i++){
        solve(i+1);
    }
    return 0;
}
