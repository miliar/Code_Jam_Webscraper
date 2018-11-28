#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int cases=0;
    while(T--){
        cases++;
        int D,N;
        cin>>D>>N;
        long double MaxTime=0;
        for(int i=0;i<N;i++){
            long double Ki,Si;
            cin>>Ki>>Si;
            MaxTime=max(MaxTime,(D-Ki)/Si);
        }
        cout<<"Case #"<<cases<<": "<<fixed<<setprecision(6)<<D/MaxTime<<endl;
    }
    return 0;
}
