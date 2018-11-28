#include<bits/stdc++.h>
using namespace std;
int main() {
    freopen("b.in","r",stdin);
    freopen("b.txt","w",stdout);
    int n;
    cin>>n;
    for(int cas=1; cas<=n; cas++) {
        string a;
        cin>>a;

        for(int k=0; k<a.size(); k++) {
            int mini = 10;
            int idx=-1;
            for(int i=k; i<a.size(); i++) {
                if(a[i]-'0'<mini) {
                    mini=a[i]-'0';
                    idx=i;
                }
            }
            int maxx = -1;
            int ind = -1;
            for(int i=k; i<idx; i++) {
                if(a[i]-'0'>maxx) {
                    maxx=a[i]-'0';
                    ind = i;
                }
            }
            if(ind == -1 ) continue;

            a[ind]--;
            for(int j=ind+1; j<a.size(); j++)
                a[j]='9';
        }

        int chk=0;
        cout<<"Case #"<<cas<<": ";
        for(int i=0; i<a.size(); i++) {
            if(a[i]!='0')
                chk=1;
            if(chk)
                cout<<a[i];
        }
        cout<<endl;
    }
}
