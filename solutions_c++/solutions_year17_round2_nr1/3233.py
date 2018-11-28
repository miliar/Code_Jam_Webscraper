#include <bits/stdc++.h>
typedef long long ll;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (long long int i = a; i < b; i++)
#define lli unsigned long long int

using namespace std;

// for fast I/O
//ios_base::sync_with_stdio(0);
//cin.tie(0);

int main() {
    freopen ("myoutput.txt","w",stdout);

    lli t;cin>>t;
    lli testcase=1;

    while(t--){
        lli d,n;
        cin>>d>>n;
        lli k[n],s[n];
        double t[n];
        REP(i,0,n){
            cin>>k[i]>>s[i];
        }
        double maxtime=0;
        REP(i,0,n){
            t[i]=double(d-k[i])/double(s[i]);
            if(t[i]>maxtime)maxtime=t[i];
        }

        float ans=double(d)/maxtime;
        cout<<"Case #"<<testcase++<<": "<<fixed<<setprecision(6)<<ans<<endl;




    }
    return 0;
}
