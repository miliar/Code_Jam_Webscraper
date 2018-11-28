#include <bits/stdc++.h>
using namespace std;



void process(int melyik_case){
    int n, k;
    vector<tuple<double, int, double, double> > t;
    cin>>n>>k;
    for(int i=1; i<=n; i++){
        double aktr, akth;
        cin>>aktr>>akth;
        t.push_back({2*M_PI*akth*aktr, i, aktr, akth});
    }
    sort(begin(t), end(t));
    reverse(begin(t), end(t));
    double res = -1;

    for(int kivalasztot = 0; kivalasztot < t.size(); kivalasztot++){
        double oldalt;
        double kivalasztott_r, kivalasztott_h;
        tie(oldalt, ignore, kivalasztott_r, kivalasztott_h) = t[kivalasztot];
        double subres = oldalt + kivalasztott_r*kivalasztott_r*M_PI;
        int hanyatvett = 1;
        for(int i=0; i<t.size(); i++){
            if(hanyatvett == k) break;
            if(i == kivalasztot) continue;

            double aktr, akth, akt_oldal_terulet;
            tie(akt_oldal_terulet, ignore, aktr, akth) = t[i];
            if(aktr > kivalasztott_r) continue;
            subres += akt_oldal_terulet;
            hanyatvett++;
        }
        if(hanyatvett < k) continue;
        res = max(res, subres);
    }


    cout<<"Case #"<<melyik_case<<": "<<setprecision(17)<<res<<endl;

}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("ki_large_1.txt", "w", stdout);

    int T;
    cin>>T;

    for(int i = 1; i<=T; i++){
        process(i);
    }
}
