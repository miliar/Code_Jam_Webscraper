#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, cs=0;
    cin>>t;
    while(t--){
        string str; int k, rslt=0;
        cin>>str>>k;
        int x=str.size();
        for(int i=0; i<x-k+1; i++){
            if(str[i]=='+') continue;
            rslt++;
            for(int j=i; j<i+k; j++){
                str[j]=(str[j]=='+')?'-':'+';
            }
        }
        bool f=true;
        for(int i=0; i<x; i++){
            if(str[i]=='-'){
                f=false; break;
            }
        }
        if(f) printf("Case #%d: %d\n", ++cs, rslt);
        else printf("Case #%d: IMPOSSIBLE\n", ++cs);
    }
}
