#include <bits/stdc++.h>

using namespace std;

string s,ans;

void solve(){
    int len,i;
    bool chk = false;
    ans = "";
    //scanf ("%s",&s[1]);
    //len = strlen(&s[1]);
    cin >> s;
    len = s.size();
    for (i=0;i<len;i++){
        if (s[i] > s[i+1] && i+1<len){
            int j=i;
            for (;s[j-1]==s[i]&&j>0;j--){}
            s[j]--;
            j = j+1;
            for (;j<len;j++){
                s[j] = '9';
            }
            break;
        }
    }
    //cout << s << endl;

    for (i=0;i<len;i++){
        if (s[i]!='0')
            break;
    }
    for (;i<len;i++)
        ans += s[i];
    cout << ans << endl;
}

int main(){
    freopen ("B-large.in","r",stdin);
    freopen ("sabu-large.sol","w",stdout);
    int TC;

    scanf ("%d",&TC);
    for (int tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        solve();
    }

return 0;
}
