#include <bits/stdc++.h>

using namespace std;


typedef long long ll;

int main(){

    freopen("out.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){

        ll n;
        vector<int>v;

        scanf("%lld",&n);
        while(n>0){
            v.push_back(n%10);
            n/=10;
        }

        reverse(v.begin(),v.end());

        for (int i=0;i<v.size()-1;i++){
            if (v[i]>v[i+1]){
                int j=i;
                while(j>=1&&v[j-1]==v[j]) j--;
                v[j]--;
                for (j=j+1;j<v.size();j++) v[j]=9;
                break;
            }
        }

        ll ans=0;
        for (int i=0;i<v.size();i++){
            ans*=10;
            ans+=v[i];
        }

        printf("Case #%d: ",cas);
        printf("%lld\n",ans);
    }
    return 0;
}
