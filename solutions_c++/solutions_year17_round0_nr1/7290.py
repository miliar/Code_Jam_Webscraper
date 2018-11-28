#include<bits/stdc++.h>

using namespace std;

int main(){
freopen("A-large.in","r",stdin);
freopen("outl_codejamA.txt","w",stdout);
int t;
cin>>t;
for(int tc=1;tc<=t;tc++){
    string s;
    cin>>s;
    int n=s.size();
    int k; cin>>k;
    int cnt=0;
    int f=0;
    for(int i=0;i<n;i++){
        if(s[i]=='-') {
            if((i+k-1)<n){
                cnt++;
                for(int j=i;j<i+k;j++){
                   if(s[j]=='-') s[j]='+';
                   else s[j]='-';
                }
            }
            else {
                f=1; break;
            }
        }
    }
    cout<<"Case #"<<tc<<": ";
    if(f) cout<<"IMPOSSIBLE\n";
    else cout<<cnt<<endl;
}


return 0;
}
