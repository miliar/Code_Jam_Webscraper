# include <bits/stdc++.h>
using namespace std;

struct interval{
    int from, to;
    bool operator < (const interval &n) const{
        return from < n.from;
    }
};

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-out.txt", "w", stdout);
    int cases, caseno=0, ans, aC, aJ;
    vector <interval> busy;
    interval busyTime;
    cin >> cases;
    while(cases--){
        busy.clear();
        cin >> aC >> aJ;
        for (int i=0; i<aC+aJ; i++){
            cin >> busyTime.from >> busyTime.to;
            busy.push_back(busyTime);
        }
        if (aC==1 || aJ==1) ans = 2;
        else{
            sort(busy.begin(), busy.end());
            int gap1 = busy[1].from - busy[0].to, gap2 = busy[0].from - busy[1].to + 60*24;
            if (gap1 >= 720 | gap2 >= 720) ans = 2;
            else ans = 4;
        }
        cout << "Case #" << ++caseno << ": " << ans << endl;
    }
    return 0;
}
