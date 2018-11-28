#include<bits/stdc++.h>
using namespace std;

#define l long long
#define ld long double
#define pb push_back
#define mod 10000007
#define ii pair<int,int>
#define jj pair<ii,ii>

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;cin>>t;

    for(int ix=1;ix<=t;ix++){

        printf("Case #%d: ",ix);
        string s;cin>>s;

        int k;cin>>k;
        int n=s.length();

        int ans=0;
        for(int i=0;i<=n-k;i++){
            if(s[i]=='-'){
                ans++;
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')s[j]='+';
                    else s[j]='-';
                }
            }
        }

        bool f=true;
        for(int i=0;i<n;i++){
            if(s[i]=='-'){
                f=false;break;
            }
        }
        if(f)cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;

    }
}
