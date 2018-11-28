#include <bits/stdc++.h>

#define ll long long
#define de(x) cout<<#x<<": "<<x<<endl
#define INF 99999

using namespace std;

int main() {
    
    ios::sync_with_stdio(false);

    int t;
    cin>>t;
    for(int q=1;q<=t;++q){
        int d,n;
        cin>>d>>n;
        int k[n],s[n];
        double sp[n];
        double count=0;
        for(int i=0;i<n;++i){
            cin>>k[i]>>s[i];
            sp[i]=((double)(d-k[i]))/((double)s[i]);
            if(sp[i]>count){
                count=sp[i];
            }
            
        }
        cout << fixed;
        cout<<"Case #"<<q<<": "<<setprecision(6)<<((double)d/count)<<endl;
    }

}