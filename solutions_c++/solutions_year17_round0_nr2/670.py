#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
string s,ans;
int len;
bool pan(int i,int j){
    for(;i<len;i++){
        ans[i]='0'+j;
    }
    return ans<=s;
}
int main(){
    ll a,b,c,d,e,f,g,h,k,t;
    ios::sync_with_stdio(0);
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        cin>>s;
        cout<<"Case #"<<ii<<": ";
        len=s.size();
        ans="";
        for(int i=0;i<len;i++){
            ans.push_back('0');
        }
        for(int i=0;i<len;i++){
            h=9;
            int j;
            if(i==0){
                j=0;
            }
            else{
                j=ans[i-1]-'0';
            }
            for(;j<10;j++){
                if(!pan(i,j)){
                    h=j-1;break;
                }
            }
            ans[i]='0'+h;
        }
        g=0;
        for(int i=0;i<len;i++){
            g*=10ll;
            g+=ans[i]-'0';
        }
        cout<<g<<endl;
    }
    return 0;
}
