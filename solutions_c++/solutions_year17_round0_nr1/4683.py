#include <bits/stdc++.h>

using namespace std;

int t,i,ttl,j,k;
string s;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>s>>k;
        cout<<"Case #"<<t1<<": ";
        ttl=0;
        for (i=0;i<s.size();i++)
          if (s[i] == '-')
          {
           if (i+k-1 >= s.size()) {
            ttl=-1;
            break;
           }
           ttl++;
           for (j=i;j<i+k;j++)
            s[j]='+'+'-'-s[j];
          }
        if (ttl == -1) cout<<"IMPOSSIBLE"<<endl; else
            cout<<ttl<<endl;
    }
}
