/**
Author:  ShivamRathore (Shivam010)
**/
#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string out = "Case #";
        double ans=99999999999999,a,b,s;
        ll d,n;
        cin>>d>>n;
        while(n--){
            cin>>a>>b;
            s=double(d*b)/(d-a);
            if(s<ans)
                ans=s;
        }
        cout<<out<<t<<": ";
        printf("%.6lf\n",ans);
        /** answer **/
    }
    return 0;
}
