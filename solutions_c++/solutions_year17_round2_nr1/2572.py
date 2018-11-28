#include <bits/stdc++.h>
#define gcd _gcd

using namespace std;

int main(){
    int tt;
    cin>>tt;
    for(int t=1;t<tt+1;t++){
        long long d;
        int n;
        cin>>d>>n;
        float maxTime=0;
        for(int i=0;i<n;i++){
            float time;
            long long k;
            int s;
            cin>>k>>s;
            time=(d-k)/(s*1.0);
            if(time>maxTime){
                maxTime=time;
            }
        }
        cout<<"Case #"<<t<<": ";
        printf("%0.6f\n",d/maxTime);
    }
}