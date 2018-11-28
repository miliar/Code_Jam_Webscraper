#include<bits/stdc++.h>
#include<fstream>
using namespace std;

typedef long long int ll;

int main(){
    ll t;
    ifstream f ;
    f.open("A-large (1).in");
    ofstream out ;
    out.open("out.txt");
    f >> t;
    ll a=1;
    while(a<=t){
        double dist;
        ll n;
        f >> dist >> n;
        double pos, vel,mn=0,curr,ans;
        while(n--){
            f >> pos >> vel;
            curr = (dist-pos)/vel;
            if(curr>mn){
                mn = curr;
            }
        }
        ans = dist/mn;
        out << "Case #" << a << ": ";
        out << setprecision(18) << ans << endl;
        a++;
    }
    f.close();
    out.close();
}


