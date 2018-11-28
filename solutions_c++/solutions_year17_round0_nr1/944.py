#include <bits/stdc++.h>
using namespace std;
int cas;
int T;
/////////////////////////////////////////////////////

const int N=1e3+5;
char s[N];

int main(){

    for(cin>>T; T--; ){
        printf("Case #%d: ", ++cas);
        /////////////////////////////////////
        int k;
        cin >> s >> k;
        int n=strlen(s);

        int cnt=0;
        for(int i=0; i+k<=n; i++)
            if(s[i]=='-'){
                for(int j=i; j<i+k; j++)
                    s[j]=s[j]=='+'?'-':'+';
                ++cnt;
            }
        bool f=true;
        for(int i=0; i<n; i++)
            if(s[i]=='-'){
                f=false;
                break;
            }

        if(f) cout << cnt << endl;
        else puts("IMPOSSIBLE");
    }
    return 0;
}