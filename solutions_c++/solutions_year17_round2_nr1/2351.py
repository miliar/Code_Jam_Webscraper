#include <bits/stdc++.h>
using namespace std;

void process(int casee){
    long long D;
    int n;
    double res = -1;
    cin>>D>>n;
    for(int i=1; i<=n; i++){
        double k,s;
        cin>>k>>s;
        double not_bigger = D / ((D-k) / s);
        if(res < 0) res = not_bigger;
        else res = min(res, not_bigger);
    }
    cout<<"Case #"<<casee<<": "<<setprecision(10)<<res<<endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("big_ki.txt", "w", stdout);

    int T;
    cin>>T;
    for(int i=1; i<=T; i++){
        process(i);
    }


}
