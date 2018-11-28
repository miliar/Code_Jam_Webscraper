#include <bits/stdc++.h>

using namespace std;

map<long long,long long,greater<long long> > mapa;

pair<long long,long long> caso() {
    mapa.clear();
    long long n, k;
    cin >> n >> k;
    mapa[n] = 1;
    while(k>0) {
        pair<long long,long long> t = (*mapa.begin());
        k -= t.second;
        long long tf = t.first-1;
        //cerr << tf-tf/2 << " "<< tf/2 <<" "<< k << endl;
        if(k <= 0) {
            return make_pair(tf-tf/2,tf/2);
        }
        if(mapa.find(tf/2) == mapa.end()) {
            mapa[tf/2] = 0;
        }
        if(mapa.find(tf-tf/2) == mapa.end()) {
            mapa[tf-tf/2] = 0;
        }
        mapa.erase(t.first);
        mapa[tf/2] += t.second;
        mapa[tf-tf/2] += t.second;
    }
}

int main() {
    int cases;
    cin >> cases;
    for(int i=1;i<=cases;i++) {
        pair<long long,long long> par = caso();
        cout << "Case #" << i << ": " << par.first <<" "<< par.second << endl;
    }
    return 0;
}