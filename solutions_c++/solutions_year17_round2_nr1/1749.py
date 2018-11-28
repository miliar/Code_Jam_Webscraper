#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<n;++i)
#define rforn(i,n) for(int i=n-1;i>=0;--i)
#define y1 gteethegrrwmjtrrtgghnrhthth
#define y2 fgntrhtrhththreggjntghnrtfg


#define ld long double

int main(){

    ifstream cin("input.txt");
    ofstream cout("output.txt");
/*
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
*/
    int t;
    cin>>t;

    ld d;
    int n;

    ld k,s;
    ld maxTime;
    ld cTime;

    cout<<fixed<<setprecision(8);

    for(int i=1;i<=t;++i){
        cin>>d>>n;

        maxTime =  0;
        for(int j=0;j<n;++j){
            cin>>k>>s;
            cTime = (d-k)/s;
            if(cTime>maxTime)
                maxTime = cTime;
        }
        cout<<"Case #"<<i<<": "<<d/maxTime<<'\n';
    }
}
