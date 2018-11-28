#include<bits/stdc++.h>

using namespace std;

vector<pair<int,char> >v;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        v.clear();
        int n,i;
        cin >> n;
        string ans="",fin="";
        int r,o,y,g,b,v1,x1,y1,x,z1;
        cin >> r >> o >> y >> g >> b >> v1;
        v.push_back(make_pair(r,'R')); v.push_back(make_pair(y,'Y')); v.push_back(make_pair(b,'B'));
        sort(v.begin(),v.end());
        cout << "Case #" << it << ": ";
      //  if(v[2].first <= v[0].first + v[1].first && v[2].first * 2 >= v[0].first + v[1].first) {
            x1 = v[1].first; y1 = v[2].first; z1 = v[0].first;
            while(x1 > 0) {
                ans = ans + v[2].second + v[1].second;
                x1 = x1 - 1; y1 = y1 - 1;
            }
            while(y1 > 0) {
                ans = ans + v[2].second;
                y1 = y1 - 1;
            }
            for(i=ans.length()-1;i>=0;i--) {
                if(ans[i] == v[2].second && z1 > 0) {
                    fin = fin + v[0].second; z1 = z1 - 1;
                }
                fin = fin + ans[i];
            }
            reverse(fin.begin(),fin.end());
           // cout << fin << "\n";
            for(i=0;i<n;i++) {
                if(i == n - 1) x = 0;
                else x = i + 1;
                if(fin[i] == fin[x]) break;
            }
            if(i == n) cout << fin << "\n";
            else cout << "IMPOSSIBLE\n";
        //}
        /*else {
            cout << "IMPOSSIBLE\n";
        } */
    }
    return 0;

}
