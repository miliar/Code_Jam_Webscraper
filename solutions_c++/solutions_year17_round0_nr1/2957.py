#include <bits/stdc++.h>
using namespace std;

int main(){
    int t,k,ncase = 1, val, ans, acum, store[1000];
    string seq;
    bool possible;
    cin>>t;
    while(t>0){
        possible = true;
        cin>>seq>>k;
        acum = ans = 0;
        for (int i=0;i<seq.length();i++)store[i]=0;
        for (int i=0;i<seq.length();i++){
            val = seq[i]=='+'?0:1;
            val = (val+acum)%2;
            if (val==1){
                if (i+k-1>=seq.length()){
                    possible=false;
                    break;
                }
                store[i+k-1]=1;
                acum++,ans++;
            }if (store[i])acum--;
        }
        if (possible)printf("Case #%d: %d\n",ncase++,ans);
        else printf("Case #%d: IMPOSSIBLE\n",ncase++);
        t--;
    }
}
