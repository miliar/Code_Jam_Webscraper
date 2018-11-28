#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Lehetoseg{
    bool paratlan;
    ll tav;
    ll darab;
    Lehetoseg(ll h, ll darab) : darab(darab){
        //cout<<"*"<<h<<endl;
        paratlan = h%2 == 0;
        if(h < 1) tav = -10;
        else tav = (h-1)/2;
    }

    bool operator<(const Lehetoseg& masik) const {
        if(tav < 0) return true;
        if(masik.tav < 0) return false;
        return make_pair(tav, paratlan) < make_pair(masik.tav, masik.paratlan);
    }


};

void process(){

    ll n,k;

    cin>>n>>k;
    /*if(n == k){
        cout<<0<<" "<<0;
        return;
    }*/
    auto mentk = k;
    priority_queue<Lehetoseg> options;
    options.push(Lehetoseg(n, 1));
    k--;
    while(k > 0){

        auto top = options.top();
        options.pop();

        while(!options.empty() && make_pair(top.tav, top.paratlan) == make_pair(options.top().tav, options.top().paratlan)){
            top.darab += options.top().darab;
            options.pop();
        }

        ll levesz = min(top.darab, k);

        //if(n == 1000 && mentk == 1000) cout<<top.tav<<endl;

        {auto copyka = top;
        copyka.darab -= levesz;
        if(copyka.darab > 0) options.push(copyka);}

        if(top.paratlan){
            options.push(Lehetoseg(top.tav, levesz));
            options.push(Lehetoseg(top.tav+1, levesz));
        }
        else options.push(Lehetoseg(top.tav, levesz*2));
        k -= levesz;
    }
    auto top = options.top();
    cout<<top.tav+top.paratlan<<" "<<top.tav;
}

int main(){
    ios_base::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("utsooo.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i=1; i<=T; i++){
        cout<<"Case #"<<i<<": "<<flush;
        process();
        cout<<endl;
    }
}
