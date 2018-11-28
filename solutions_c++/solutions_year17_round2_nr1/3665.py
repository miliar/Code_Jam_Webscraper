#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
typedef long long int ll;

ifstream in("A-large.in");
ofstream out("output");

int main(){
    int t;
    in>>t;
    double dest;
    int noh;
    for(int i = 1;i<=t;i++){
        out<<"Case #"<<i<<": ";
        in>>dest>>noh;
        double temp,res = 0;
        double hpos, hs;
        for(int i = 1;i<=noh;i++){
            in>>hpos>>hs;
            temp = dest-hpos;
            temp/=hs;
            res = max(res,temp);
        }
        out<<fixed<<setprecision(8)<<dest/res<<endl;
    }
    
    return 0;
}