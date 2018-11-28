#include <bits/stdc++.h>

using namespace std;

int main()
{   freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1; j<=t; j++){
        string s;
        cin>>s;
        int n=s.size();
        string ans;
        if (n==1){ans=s;}
        else {ans=s;
        int flag=1;
        while(1){
            int pos=-1;
            for(int i=0; i<n-1; i++) if(ans[i]>ans[i+1]) {pos=i; break;}
            if(pos==-1) break;
            ans[pos]=(ans[pos]=='0'? '9': ans[pos]-1);
            for(int i=pos+1; i<n; i++) ans[i]='9';

        }}
        int k=0;
        while(ans[k]=='0') k++;
        cout<<"Case #"<<j<<": ";
        for(int i=k; i<n; i++) cout<<ans[i];
        cout<< endl;
    }

    return 0;
}
