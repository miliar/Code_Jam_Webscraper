#include <bits/stdc++.h>
using namespace std;

int t,nc,nj,xin,sisac,sisaj,a,b,ganti;
int tadi;
vector<bool> state;
bool flag;
vector<pair<int,int> > c,ja;

int main(){
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        scanf("%d %d", &nc, &nj);
        c.clear(); ja.clear();
        sisac = 720; sisaj = 720;
        for (int j = 0; j < nc; j++){
            scanf("%d %d", &a, &b);
            c.push_back(make_pair(a,b));
            sisac -= (b-a);
        }
        for (int j = 0; j < nj; j++){
            scanf("%d %d", &a, &b);
            ja.push_back(make_pair(a,b));
            sisaj -= (b-a);
        }
        sort(c.begin(),c.end());
        sort(ja.begin(),ja.end());
        state.assign(20005,0);
        if (c.size() == 1 or ja.size() == 1){
            ganti = 2;
        } else if (c.size() == 0){
            if (ja[1].first-ja[0].second <= sisaj or 1440-ja[1].second+ja[0].first <= sisaj) ganti = 2;
            else ganti = 4;
        } else if (ja.size() == 0){
            if (c[1].first-c[0].second <= sisac or 1440-c[1].second+c[0].first <= sisac) ganti = 2;
            else ganti = 4;
        } else {
            ganti = 2;
        }
        printf("Case #%d: %d\n", i,ganti);
    }
}
