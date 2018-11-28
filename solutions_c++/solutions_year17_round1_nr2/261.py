#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inB.txt", "r", stdin);
    freopen("outB.txt", "w", stdout);
    cin.tie(0);ios_base::sync_with_stdio(false);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";
        int N, P;
        cin >> P >> N;
        vector<int64_t> need(P);
        for(auto &e:need) cin >> e;

        vector<vector<int64_t> > food(P, vector<int64_t>(N));

        for(int i=0;i<P;++i){
            for(int j=0;j<N;++j) cin >> food[i][j];
            sort(food[i].rbegin(), food[i].rend());
        }

        int64_t ma = 0;
        for(int i=0;i<P;++i) ma = max(ma, food[i].front());
        ma+=3;

        int out=0;
        for(int64_t s=1;s<ma;++s){
            bool f=false;
            for(int i=0;i<P;++i){
                while(!food[i].empty() && !(100*food[i].back()>=90*s*need[i])){
                    food[i].pop_back();
                }
                if(food[i].empty() || ! (100*food[i].back() <= 110*s*need[i])) f=true;
            }
            if(f) continue;
            else ++out;
            for(int i=0;i<P;++i) food[i].pop_back();
            --s;
        }



        cout << out << "\n";
        cerr << out << "\n";
    }


    return 0;
}

