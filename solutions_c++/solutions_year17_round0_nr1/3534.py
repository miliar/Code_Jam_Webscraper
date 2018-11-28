#include<bits/stdc++.h>
using namespace std;

string s;
int k;
int t = 0;
void solve(){
    printf("Case #%d: ",++t);
    cin>>s>>k;
    int ans = 0;
    for(int i=0;i<s.size()-k+1;i++){
        if(s[i]=='-'){
            ans++;
            for(int j=0;j<k;j++){
                if(s[i+j]=='-')
                    s[i+j]='+';
                else
                    s[i+j]='-';
            }
        }
    }
    int flag = 0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='-')flag = 1;
    }
    if(flag==1){
        cout<<"IMPOSSIBLE"<<endl;
    }else{
        cout<<ans<<endl;
    }
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)solve();
}
