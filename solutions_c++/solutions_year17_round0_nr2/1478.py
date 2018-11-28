#include<bits/stdc++.h>
using namespace std;
int main(){
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    cin>>t;
    for(int k=1;k<=t;k++){
        string s;
        cin>>s;
        int i=0;
        for(;i<s.size()-1;i++){
            if(s[i]>s[i+1]) {
                s[i]--;
                for(int j=i+1;j<s.size();j++) s[j]='9';
                i=-1;
            }
        }
        int j;
        for(j=0;j<s.size()-1;j++) if(s[j]!='0') break;
        cout<<"Case #"<<k<<": ";
        for(;j<s.size();j++) cout<<s[j];
        cout<<endl;

    }
}
