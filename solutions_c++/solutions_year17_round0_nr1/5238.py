//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define MAXN 1000005

int main(){
    freopen ("A-large.in","r",stdin); 
    freopen ("A-large.out","w",stdout);
    int i,j,n,l,t,ans;
    bool flag;
    string s;
    scanf("%d",&t);
    for (int tester = 1; tester <= t; ++tester){
        cin>>s;
        scanf("%d",&n);
        flag = true;
        ans = 0;

        l = s.size();
        for(i=0;i<l;i++){
            if(s[i]=='+') continue;
            ans++;
            if(i+n-1>=l){
                flag = false;
                break;
            }
            for(j=i;j<i+n;j++)
                (s[j]=='+') ? s[j]='-' : s[j]='+';
        }
        (flag) ? printf("Case #%d: %d\n",tester,ans) : printf("Case #%d: IMPOSSIBLE\n",tester);;

    } 

    return 0;
}