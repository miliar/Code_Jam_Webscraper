#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, cs=0;
    cin>>t;
    while(t--){
        string n;
        cin>>n;
        int x=n.size(), y=0; char z='0';
        string rslt;
        for(int i=0; i<x; i++) rslt+='0';
        bool f=false, ff=false;
        for(int i=0; i<x; i++){
            if(ff) rslt[i]='9';
            else if(f) rslt[i]=n[i]-1, ff=true;
            else if(n[i]>z){
                y=i; rslt[i]=n[i]; z=n[i];
            }
            else if(n[i]==z) rslt[i]=n[i], z=n[i];
            else i=y-1, f=true;
        }
        if(rslt[0]=='0') rslt=rslt.substr(1, x-1);
        printf("Case #%d: %s\n",++cs, rslt.c_str());
    }
}
