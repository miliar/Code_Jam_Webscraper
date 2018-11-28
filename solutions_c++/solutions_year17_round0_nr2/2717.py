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
ll t,n;

void out(vector<int> d){
    int ind = 0;
    while(ind<d.size() && d[ind]==0)++ind;
    while(ind<d.size()) cout << d[ind++];
    cout << "\n";
    return;
}

void solve(int cas){
    cin >> n;
    vector<int> digs;
    while(n>0){
        digs.push_back(n%10);
        n/=10;
    }
    reverse(digs.begin(), digs.end());
    int prev = digs[0];
    int ind = 0;
    while(ind<digs.size() && digs[ind]>= prev){
        prev = digs[ind];
        ++ind;
    }
    cout << "Case #" << cas << ": ";
    if(ind==digs.size()){
        out(digs);
        return;
    }

//    for(int i = ind; i<digs.size(); i++){
//        digs[i] = 9;
//    }
    int cur;
    for(int i = 0; i<ind; i++){
        if(digs[i] == digs[ind-1]){
            cur = i;
            break;
        }
    }
    --digs[cur];
    for(int i=cur+1; i<digs.size(); i++){
        digs[i] = 9;
    }

    out(digs);
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
