#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void pjam(int tt){
    printf("Case #%d: ",tt);
}
string s;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,it;
    cin>>t;
    for(it=1;it<=t;it++){
        cin>>s;
        for(int j=1;j<=18;j++){
            for(int i=0;i<s.size()-1;i++){
                if(s[i]>s[i+1]){
                    for(int k=i+1;k<s.size();k++)
                        s[k]='9';
                    s[i]--;
                    break;
                }
            }
        }
        pjam(it);
        bool flag=false;
        for(auto it :s){
            if(it!='0')
                flag=true;
            if(flag)
                cout<<it;
        }
        cout<<endl;
    }
}
