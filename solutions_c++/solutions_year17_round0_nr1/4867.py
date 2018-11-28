#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
ll arr[100100],t,k,n,ans,temp;
string s;
int main()
{
    freopen("input1codejam.in","r",stdin);
    freopen("output1codejam.out","w",stdout);
    cin>>t;
    for(int j=1;j<=t;j++){
        ans=0;
        bool ok=true;
        cin>>s;
        n=s.length();
        cin>>k;
        for(int i=0;i<n;i++){
            if(s[i]=='-'){
                if((i+k)<=n){
                    ans++;
                    for(int q=i;q<(i+k);q++){
                        if(s[q]=='-')   s[q]='+';
                        else    s[q]='-';
                    }
                }
                else{
                    ok=false;
                    break;
                }
            }
        }
        if(!ok)
            cout<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<j<<": "<<ans<<endl;
    }
return 0;
}
