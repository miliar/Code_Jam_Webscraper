#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++) {
        int n;
        pair<int,char>a[6];
        cin >> n;
        for(int i=0; i<6;++i){
            cin >> a[i].first;
        }
        a[0].second = 'R';
        a[1].second = 'O';
        a[2].second = 'Y';
        a[3].second = 'G';
        a[4].second = 'B';
        a[5].second = 'V';
        sort(a+6,a);
        string s;
        if(a[0].first > a[1].first + a[2].first){
            cout << "Case #" << tc  << ": IMPOSSIBLE\n";
            continue;
        }
        if((a[1].first + a[2].first - a[0].first) % 2 == 1) {
            s.push_back(a[1].second);
            a[1].first--;
        }
        int diff = (a[1].first + a[2].first - a[0].first) / 2;
        for(int i=0; i<a[0].first;i++){
            s.push_back(a[0].second);
            if (a[0].first - i + diff > a[2].first)
                s.push_back(a[1].second);
        	else
                s.push_back(a[2].second);
        }
        for(int i=0;i<diff;i++){
            s.push_back(a[1].second);
            s.push_back(a[2].second);
        }
        cout << "Case #" << tc  << ": "<< s << "\n";
    }
    return 0;
}