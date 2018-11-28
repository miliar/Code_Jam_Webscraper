#include <bits/stdc++.h>
using namespace std;
//make_tuple emplace_back next_permutation push_back make_pair second first setprecision

#if MYDEBUG
#include "lib/cp_debug.h"
#else
#define DBG(...) ;
#endif

using LL = long long;
constexpr LL LINF=334ll<<53;
constexpr int INF=15<<26;
constexpr LL  MOD=1E9+7;

struct Problem{
    int r,c;
    vector<vector<char>> cake;
    vector<tuple<int,int,char>> pos;
    Problem(int r,int c):r(r),c(c),cake(r,vector<char>(c)){};

    void solve(){
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                cin >> cake[i][j];
                if(cake[i][j]!='?')pos.emplace_back(i,j,cake[i][j]);
            }
        }
        sort(pos.begin(),pos.end());
        //top
        auto it= pos.begin();
        int filled=-1;
        while(1){
            int cr=get<0>(*it);
            vector<tuple<int,int,char>> tmp;
            while(it<pos.end()){
                tmp.push_back(*it);
                if((it+1)==pos.end() or get<0>(*it)<get<0>(*(it+1))){it++;break;}
                ++it;
            }
            tmp.emplace_back(cr,c,'?');
            if(it==pos.end())cr=r-1;
            for(int k= 0,lb=0; k<(int)tmp.size()-1; ++k){
                int rb=get<1> (tmp[k+1]);
                for(int i=filled+1; i<=cr; ++i){
                    for(int j=lb; j<rb; ++j){
                        cake[i][j]=get<2>(tmp[k]);
                    }
                }
                lb= get<1>(tmp[k])+1;
            }
            if(it==pos.end())break;
            filled=cr;
        }
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                cout << cake[i][j];
            }
            cout <<"\n";
        }

    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ":\n";
        int r,c;
        cin >> r >> c;
        Problem p(r,c);
        p.solve();
    }

    return 0;
}

