#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
string st;
int k;
void solve(){
    int i,j,cnt=0;
    for(i=0;i<st.size()-k+1;i++)
        if(st[i]=='-'){
            for(j=i;j<i+k;j++){
                if(st[j]=='+') st[j]='-';
                else st[j]='+';
            }
            cnt++;
        }
    for(i=0;i<st.size();i++)
        if(st[i]=='-'){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
    cout<<cnt<<endl;
}
int main(){
    int t,i;
    freopen("A.out","w",stdout);
    freopen("A.in","r",stdin);
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        cin>>st>>k;
        printf("Case #%d: ",i);
        solve();
    }
}
