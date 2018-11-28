#include <bits/stdc++.h>

using namespace std;

char s[100005];

void solve(){
    int len,k,cnt=0;
    scanf ("%s",&s[1]);
    scanf ("%d",&k);
    len = strlen(&s[1]);
    //printf ("%d\n",len);
    for (int i=1;i+k-1<=len;i++){
        bool chk = false;
        if (s[i]=='+') continue;
        for (int j=i;j<i+k&&j<=len;j++){
            if (s[j] == '-'){
                chk = true;
            }
        }
        if (chk){
            cnt++;
            for (int j=i;j<i+k&&j<=len;j++){
                if (s[j] == '-'){
                    s[j] = '+';
                }else{
                    s[j] = '-';
                }
            }
        }
        //printf ("%s %d\n",&s[1],cnt);
    }
    bool cc = true;
    for (int i=1;i<=len;i++)
        if (s[i] == '-')
            cc = false;
    if (cc) printf ("%d\n",cnt);
    else printf ("IMPOSSIBLE\n");
}

int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("sabu-large.sol","w",stdout);
    int TC;

    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }

return 0;
}
