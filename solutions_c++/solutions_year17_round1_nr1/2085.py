#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


char field[30][30];
int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ":";
        int R, C;
        cin >> R >> C;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                cin >> field[i][j];
            }
        }
        // 各行について調べていく
        map<int, map<int, char> > m;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                if(field[i][j] != '?'){
                    m[i][j] = field[i][j];
                }
            }
        }
        int prv_row = -1;
        int nxt_row = -1;
        for(auto it = m.begin(); it != m.end(); it++){
            // 次の行を計算しておく
            if(it == --m.end()){
                nxt_row = R;
            }
            else{
                auto iit = it;
                iit++;
                nxt_row = iit->first;
            }
            auto m2 = it->second;

            int prv_col = -1;
            int nxt_col = -1;
            for(auto it2 = m2.begin(); it2 != m2.end(); it2++){
                // 次の列を計算
                if(it2 == --m2.end()){
                    nxt_col = C;
                }
                else{
                    auto iit = it2;
                    iit++;
                    nxt_col = iit->first;
                }
                // を塗る
                for(int y = prv_row + 1; y < nxt_row; y++){
                    for(int x = prv_col + 1; x < nxt_col; x++){
                        field[y][x] = it2->second;
                    }
                }

                prv_col = nxt_col - 1;
            }

            prv_row = nxt_row - 1;
        }

        cout << endl;
        for(int i = 0; i < R; i++){
            for(int j = 0; j < C; j++){
                cout << field[i][j];
            }
            cout << endl;
        }

    }
    return 0;
}
