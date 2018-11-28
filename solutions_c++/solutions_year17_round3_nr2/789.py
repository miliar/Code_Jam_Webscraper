#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

int solve(int AC, int AJ, vector<pair<int, int>> &CD, vector<pair<int, int>> &JK){
    if(AC == 1 && AJ == 1) return 2;

    sort(CD.begin(), CD.end());
    sort(JK.begin(), JK.end());

    if(AC == 2){
        int span = CD[1].second - CD[0].first;
        span = min(span, 1440 - (CD[1].first - CD[0].second));
        if(span > 720) return 4;
        else return 2;
    }
    if(AJ == 2){
        int span = JK[1].second - JK[0].first;
        span = min(span, 1440 - (JK[1].first - JK[0].second));
        if(span > 720) return 4;
        else return 2;
    }
    return 2;
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int AC, AJ;
        cin >> AC >> AJ;
        vector<pair<int, int>> CD(AC), JK(AJ);
        for(int i=0; i<AC; i++) cin >> CD[i].first >> CD[i].second;
        for(int i=0; i<AJ; i++) cin >> JK[i].first >> JK[i].second;

        cout << "Case #" << i+1 << ": " << solve(AC, AJ, CD, JK) << endl;
        
    }

    return 0;
}
