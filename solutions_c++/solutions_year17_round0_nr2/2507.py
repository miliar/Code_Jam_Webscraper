#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
string st;
void solve(){
    int i,j;
    for(i=st.size()-1;i>0;i--){
        if(st[i]<st[i-1]){
            j=i-1;
            while(st[j]=='0'){
                st[j]='9';
                j--;
            }
            st[j]--;
            for(j=i;j<st.size();j++) st[j]='9';
        }
    }
    if(st[0]=='0') st=st.substr(1);
    cout<<st<<endl;
}
int main(){
    int t,i;
    freopen("Bl.in","r",stdin);
    freopen("Bl.out","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>st;
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
