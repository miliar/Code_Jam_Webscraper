#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
#include <map>
#include <unordered_map>
#include<utility>
#include<iostream>
#include<math.h>
#include<vector>
#include <queue>

using namespace std;



pair<bool, vector<int> >  canTake(vector<vector<pair<int,int> > >  &V, vector<int> &indexes, int Ct) {
    vector<int> ninds;
    bool ok = true;
    for(int i = 0; i < indexes.size();i++) {
        //int curIdx = indexes[i];
        int fIdx = -1;
        for(int j = indexes[i]; j < V[0].size(); j ++ ) {
            if(Ct >=V[i][j].first &&  Ct<=V[i][j].second) {
                fIdx = j;
                break;
            }
        }
        if(fIdx !=-1) {
            ninds.push_back(fIdx+1);

        }else {
            ok = false;
        }
    }

    return {ok, ninds};
}

int solveCase(vector<vector<pair<int,int> > >  &V) {

    vector<int> cands;
    for(int i = 0; i < V.size();i++) {
        for(int j =0; j < V[0].size();j++) {
            cands.push_back(V[i][j].first);
            cands.push_back(V[i][j].second);
        }
    }

    sort(cands.begin(), cands.end());
    vector<int> indexes(V.size(),0);
    int ans = 0;
    for(int c : cands) {
        auto ctk= canTake(V,indexes,c);
        if(ctk.first) {
            ++ans;
            indexes = ctk.second;
        }
    }
    return ans;

}

pair<int, int > getInterval(long long Need, long long Total) {
    double smallest = 10.0*Total/Need/11.0;
    long long sm = (long long)smallest - 5;
    while(sm * 11* Need  < 10*Total)
        ++sm;

    double largest = 10.0 * Total/Need/9.0;



    long long lm = (long long) largest + 5;
    while(lm * 9* Need  > 10*Total)
        --lm;
    return {sm, lm};

};


int main() {
    int testCases;
    cin >> testCases;
    for(int i=0;i<testCases; i++) {
        int N , P;
        cin >> N >> P;
        vector<int> R(N);
        for(int i = 0 ; i < N ; i++) {
            cin >> R[i];
        }

        vector<vector<pair<int,int> > > Pkg(N);

        for(int i = 0 ; i < N ; i++) {
            Pkg[i].assign(P,{0,0});
            for(int j = 0; j < P ; j ++ ) {
                int sz;
                cin >> sz;
                Pkg[i][j] = getInterval(R[i],sz);
            }
        }

        for(int i = 0 ;i < N ; i++) {
            sort(Pkg[i].begin(), Pkg[i].end());
        }


        cout << "Case #" << (i+1) << ": "  <<solveCase(Pkg)<< endl;
    }

}