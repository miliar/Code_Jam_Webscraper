#include<bits/stdc++.h>
using namespace std;
int main(){
string n;
int t,k;
ios_base::sync_with_stdio(false);
cin.tie(NULL);
freopen("sample.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>t;
int j=1;
while(j<=t){
    cin>>n>>k;
    int count=0;
    for(int i=0;i<=n.size()-k;i++){
        if(n[i]=='-'){
            count++;
            for(int j=0;j<k;j++){
                if(n[i+j]=='+') n[i+j]='-';
                else n[i+j]='+';
            }
        }
    }
    bool res=true;
    for(int i=n.size()-k+1;i<n.size();i++){
        if(n[i]=='-'){
            res=false;
            break;
        }
    }
    if(res)
    cout<<"Case #"<<j<<": "<<count<<"\n";
    else  cout<<"Case #"<<j<<": IMPOSSIBLE\n";
    j++;
}
return 0;
}
