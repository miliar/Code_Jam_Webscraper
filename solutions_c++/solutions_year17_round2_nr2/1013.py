#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

string solve(int N, int R, int O, int Y, int G, int B, int V){
    int M[6] = {R, O, Y, G, B, V};
    string name = "ROYGBV";
    vector<vector<int>> L(6);
    L[0].push_back(2);
    L[0].push_back(3);
    L[0].push_back(4);
    L[2].push_back(0);
    L[3].push_back(0);
    L[4].push_back(0);
    L[2].push_back(4);
    L[2].push_back(5);
    L[4].push_back(2);
    L[5].push_back(2);
    L[4].push_back(1);
    L[1].push_back(4);

    string ans = "";
    int s = 0;
    for(int i=0; i<6; i++)
        if(M[i]) {
            s = i;
            M[i]--;
            break;
        }
    ans += name[s];

    for(int i=1; i<N; i++){
        int mx = 0;
        int t;
        for(auto edge : L[s]){
            if(M[edge] > mx){
                mx = M[edge];
                t = edge;
            }
            if(M[edge] && (edge == 1 || edge == 3 || edge == 5)){
                t = edge;
                break;
            }
        }
        s = t;
        if(mx == 0) return "IMPOSSIBLE";
        ans += name[s];
        M[s]--;
    }

    for(auto edge : L[s])
        if(ans[0] == name[edge]) return ans;
    return "IMPOSSIBLE";

}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        cout << "Case #" << i+1 << ": ";
        cout << solve(N, R, O, Y, G, B, V) << endl;
    }

    return 0;
}
