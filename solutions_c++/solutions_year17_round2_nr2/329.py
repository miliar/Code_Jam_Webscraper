#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef pair<int, char> pic;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}



void solve_small(int R, int Y, int B){
    vector<pic> v = {pic(R, 'R'), pic(Y, 'Y'), pic(B, 'B')};
    sort(v.begin(), v.end());
    if(v[2].first > v[0].first + v[1].first){
        cout << "IMPOSSIBLE" << endl;
    }
    else{
        string ans;
        for(int i = 0; i < v[2].first; i++){
            ans += v[2].second;
            if(v[1].first){
                v[1].first--;
                ans += v[1].second;
            }
            else if(v[0].first){
                v[0].first--;
                ans += v[0].second;
            }
        }
        // 余った分は, 余った分だけ適当に出す
        for(char c : ans){
            cout << c;
            if(v[0].first){
                v[0].first--;
                cout << v[0].second;
            }
        }
        cout << endl;
    }
}

int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        int R, O, Y, G, B, V, N;
        cin >> N;
        cin >> R >> O >> Y >> G >> B >> V;
        solve_small(R, Y, B);
    }
    return 0;
}
