#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		string s;
        cin>>s;
        int idx=0;
        int n=s.size();
        while (idx+1<n){
            if (s[idx]>s[idx+1]) break;
            idx++;
        }
        string ans;
        if (idx+1==n) ans=s;
        else{
            for (int i=idx+1;i<n;i++) s[i]='9';
            s[idx]=s[idx]-1;
            idx--;
            while(idx>=0 && s[idx]>s[idx+1]){
                s[idx+1]='9';
                s[idx]=s[idx]-1;
                idx--;
            }
            ans=s;
            if (ans[0]=='0') ans=ans.substr(1);
        }
        cerr<<ans<<endl;
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;

	}
}
