#include <bits/stdc++.h>
using namespace std;


void process(int melyik_case){
    int n, k;
    double U;
    cin>>n>>k>>U;
    vector<double> chances;
    for(int i=1; i<=n; i++){
        double akt;
        cin>>akt;
        chances.push_back(akt);
    }
    sort(begin(chances), end(chances));
    int eljutott = 1;
    for(int eljutott = 1; eljutott <chances.size(); eljutott++){
        if(U < double(eljutott) * (chances[eljutott]- chances[eljutott-1])) break;
        double novelo = chances[eljutott]- chances[eljutott-1];
        for(int i=0; i<eljutott; i++){
            chances[i] = chances[eljutott];
        }
        U -= double(eljutott) * novelo;
    }
    while(eljutott < n && abs(chances[eljutott] - chances[eljutott-1]) < 0.00001) eljutott++;
    double peldany = chances[1];
    double novel = min(U/eljutott, 1 - peldany);
    for(int i=0; i<eljutott; i++){
        chances[i] += novel;
    }
    double res = 1.0;
    for(double akt : chances){
        res *= akt;
    }
    cout<<"Case #"<<melyik_case<<": "<<setprecision(17)<<res<<endl;
}


int main(){
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("ki_small_1.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i=1; i<=T; i++){
        process(i);
    }

}
