#include<bits/stdc++.h>
using namespace std;
int main(){
string n;
int t;
ios_base::sync_with_stdio(false);
cin.tie(NULL);
freopen("sample.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>t;
int j=1;
while(j<=t){
    cin>>n;
    int l=n.size();
    int last=-1;
    int max=-1;
    for(int i=1;i<l;i++){
        if(n[i]<n[i-1]) {
                max=i-1; break;
        }
    }
    while(max>=0&&n[max]==n[max-1])
        max--;
    if(l==1){;}
    else if(max==-1){;}
    else if(n[max]=='1'){
        n="";
        for(int i=0;i<l-1;i++)
            n+='9';
            }
    else{
        n[max]--;
        for(int i=max+1;i<l;i++)
            n[i]='9';
            }
    cout<<"Case #"<<j<<": "<<n<<"\n";
    j++;
}
return 0;
}
