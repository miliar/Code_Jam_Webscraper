#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long LL;


LL makeKit(LL ig, LL ig_g, LL min_serve, LL max_serve, vector<LL>& recipe, vector<multiset<LL> >& rest){
    if(rest[ig].find(ig_g) == rest[ig].end()) return 0;

    bool flag = true;
    vector<LL> w(recipe.size());
    for(int i = 0; i < w.size(); ++i){
        if(i == ig){
            w[ig] = ig_g;
            continue;
        }
        LL min_g = recipe[i] * min_serve * 90 / 100;
        if(min_g * 100 < recipe[i] * min_serve * 90) min_g += 1;
        LL max_g = recipe[i] * max_serve * 110 / 100;
        multiset<LL>::iterator it = rest[i].lower_bound(min_g);
        if(it != rest[i].end() && *it <= max_g){
            w[i] = *it;
        }else{
            flag = false;
            break;
        }
    }
    if(flag){
        for(int i = 0; i < w.size(); ++i){
            multiset<LL>::iterator it = rest[i].find(w[i]);
            if(it != rest[i].end()){
                rest[i].erase(it);
            }
        }
        return 1;
    }
    return 0;
}

LL solve(LL N, LL P, vector<LL>& recipe, vector<vector<LL> >& packages){
    vector<pair<double ,pair<LL, LL> > > ord;
    vector<multiset<LL> > rest(N);
    for(int n = 0; n < N; ++n){
        for(int p = 0; p < P; ++p){
            LL w = (double)(packages[n][p]) / recipe[n];
            ord.push_back(pair<LL, pair<LL,LL> >(w, pair<LL,LL>(n, p)));
            rest[n].insert(packages[n][p]);
        }
    }
    sort(ord.begin(), ord.end());


    LL ans = 0;
    for(int i = 0; i < ord.size(); ++i){
        LL ig = ord[i].second.first;
        LL pk = ord[i].second.second;
        LL g = packages[ig][pk];
        LL max_serve = g * 100 / 90 / recipe[ig];
        LL min_serve = g * 100 / 110 / recipe[ig];
        if(g * 100 > min_serve * recipe[ig] * 110) min_serve += 1;
        if(max_serve < min_serve) continue;
        ans += makeKit(ig, g, min_serve, max_serve, recipe, rest);
        //cerr << ig << " , " << g << " , " << ans << " , " << min_serve << " , " << max_serve << endl;
    }

    return ans;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL N, P;
        cin >> N >> P;
        vector<LL> recipe(N);
        for(int i = 0; i < N; ++i){
            cin >> recipe[i];
        }
        vector<vector<LL> > packages(N, vector<LL>(P));
        for(int i = 0; i < N; ++i){
            for(int p = 0; p < P; ++p){
                cin >> packages[i][p];
            }
        }

        cout << "Case #" << t << ": " << solve(N, P, recipe, packages) << endl;
    }
    return 0;
}

