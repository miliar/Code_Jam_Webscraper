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
        if(s.size()>1){
            for(int i=s.size()-1;i>0;i--){
                if(s[i] < s[i-1]){
                    {
                        s[i-1]=s[i-1]-1;
                        s[i]='9';
                        int j=i;
                        while(j<s.size()-1 && s[j+1]<s[j]){
                            s[j+1]='9';
                            j++;
                        }
                    }
                }
            }
        }

        cout<<"Case #"<<n-t<<": ";
        if(s[0]!='0')
            cout<<s[0];
        for(int i=1;i<s.size();i++)
            cout<<s[i];
        cout<<"\n";
    }
    return 0;
}
