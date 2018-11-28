#include <bits/stdc++.h>
#define  ren(i,j,n) for(li i=(j);i<(n);i++)
#define  rep(i,n) ren(i,0,(n))
#define  all(a) begin(a),end(a)
using namespace std;
typedef long int li;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<li> vli;
typedef vector<string> vs;
 
int main()
{
    int n;
    cin>>n;
    rep(i,n){
        string s;
        cin>>s;
        int len=s.size(),z=len-1;
        if(z)for(;z>=1;z--){
            if(s[z-1]>s[z]){
                for(int x=z;x<len;x++)s[x]='9';
                if(s[z-1]=='0') s[z-1]='9';
                else s[z-1]-=1;
            }
        }
        while(s[0]=='0') s=s.substr(1);
        cout<<"Case #"<<i+1<<": "<<s<<"\n";
    }
     
    return 0;
}