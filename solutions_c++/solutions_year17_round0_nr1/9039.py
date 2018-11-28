#include<bits/stdc++.h>
using namespace std;
int main() {
    freopen("A-large.in","r",stdin);
    freopen("b.txt","w",stdout);

    int n;
    cin>>n;
    for(int cas=1; cas<=n; cas++) {
        string a;
        int k;
        cin>>a>>k;
        int len = a.size();
        int ans =0;
        for(int i=0; i<=len-k; i++) {
            if(a[i]=='-') {
                ans++;
                for(int j=0; j<k; j++) {
                    if(a[i+j]=='-')
                        a[i+j]='+';
                    else a[i+j]='-';
                }
            }
        }
        int chk=0;
        for(int i=len-k+1; i<len; i++) {
            if(a[i]=='-')
                chk=1;
        }
        cout<<"Case #"<<cas<<": ";
        if(chk==1)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<"\n";
    }
}
