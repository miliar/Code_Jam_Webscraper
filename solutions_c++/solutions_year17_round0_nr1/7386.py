/*-------------------------------------------------------------------
                            tenacious
-------------------------------------------------------------------*/
#include<bits/stdc++.h>
using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    //ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

    int t;
    cin>>t;
    int n=t;
    while(t--){
        string s;
        cin>>s;
        int k;
        cin>>k;

        bool poss=true;
        int turns=0;

        for(int i=0;i<s.size();i++){
            if(s[i]=='-'){
                turns++;
                if( (s.size()-i) < k){
                    poss=false;
                    break;
                }
                for(int j=i;j<i+k;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        if(poss){
            cout<<"Case #"<<n-t<<": "<<turns<<"\n";
        }
        else{
            cout<<"Case #"<<n-t<<": "<<"IMPOSSIBLE"<<"\n";
        }
    }
    return 0;
}
