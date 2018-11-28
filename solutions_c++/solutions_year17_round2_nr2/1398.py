#include <bits/stdc++.h>

using namespace std;


int main()
{
//    ios_base::sync_with_stdio(false);
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++){
        int n;
//        int R,O,Y,G,B,V;
        cin >> n;
        vector<pair<int, char> > x(7);
        for(int j=0;j<6;j++){
            cin >> x[j].first;
        }
        cout << "Case #" << tc << ": ";
        x[0].second = 'R';
        x[1].second = 'O';
        x[2].second = 'Y';
        x[3].second = 'G';
        x[4].second = 'B';
        x[5].second = 'V';
//        vector<char> ans;
//        ans.resize(n);
        string ans;
        ans.resize(n);
        sort(x.begin(), x.end());
        reverse(x.begin(),x.end());
        if(x[0].first > n/2){
            cout << "IMPOSSIBLE\n";
            continue;
        }
        int cur = 0;
        int i = 0;
        for(;i<6;i++){
            int sz = 0;
            for(int j=0; j<x[i].first && cur < n;j++){
                ans[cur] = x[i].second;
                cur += 2;
                sz++;
            }
            if(cur >= n){
                x[i].first -= sz;
                break;
            }
        }
        cur = 1;
        for(;i<6;i++){
            for(int j=0; j<x[i].first;j++){
                ans[cur] = x[i].second;
                cur += 2;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
