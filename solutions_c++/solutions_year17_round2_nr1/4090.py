#include <bits/stdc++.h>
using namespace std;

int main() {
    int t,d=1;
    long double diff=0;
    cin>>t;
    while(t--){
        diff=0;
        long double a,b;
        cin>>a>>b;
        for(int i=0;i<b;i++){
            long double x,y;
            cin>>x>>y;
            diff = max(diff,(a-x)/y);
        }
        long double ans = a/diff;
        std::cout<<std::fixed;
        cout<<"Case #"<<d++<<": "<<setprecision(6)<<ans<<endl;
    }
	return 0;
}