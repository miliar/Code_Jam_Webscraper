#include<bits/stdc++.h>
using namespace std;
void fileMode(){
    freopen("input1.in","r",stdin);
    freopen("output.out","w",stdout);
}
int main(){
    fileMode();
    int t,ans,n;
    string s;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>s>>n;
        ans=0;
        for(int j=0;j<s.length()-n+1;j++){
            if(s[j]=='-'){
                for(int k=0;k<n;k++){
                    s[j+k]=s[j+k]=='-'?'+':'-';
                }
                ans++;
            }
        }
        for(int j=0;j<s.length();j++)
			if(s[j]=='-') ans=-1;
        cout<<"Case #"<<i<<": ";
		if(ans==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
    }
}
