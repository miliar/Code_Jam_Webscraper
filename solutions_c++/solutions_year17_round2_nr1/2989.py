#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp("BAL.in");
    ofstream op;
    op.open("BA.txt",ios_base::app);
    int tc,caseno=1;
    inp>> tc;
    while(tc--){
        double n,d;
        inp>> d >> n;
        double k[1005],s[1005],t[1005],mx=0.0;
        for(int a=0;a<n;a++){
            inp>> k[a] >> s[a];
            t[a]=(d-k[a])/s[a];
            mx=max(mx,t[a]);
        }
        op<< setprecision(8) << "Case #" << caseno++ << ": " << d/mx <<endl;
    }
    op.close();
    return 0;
}
