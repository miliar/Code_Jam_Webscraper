#include <bits/stdc++.h>
using namespace std;

#define read() freopen("A-large.in","r",stdin)
#define INF ((1<<29)-1)
#define EPS (1e-9)
#define PI (2*acos(0.0))
#define ll long long
#define ull unsigned ll
#define SIZE ((ll)1e6)+10
#define testcase ll T;cin>>T;for(int t=1;t<=T;t++)
#define printcase() cout<<"Case "<<t<<":\n"
#define pb push_back
#define PAR_SIZE 1000000+10
#define BFS_GRID 1010
#define NL() cout << endl
#define FOR(itt,n) for(int itt=0;itt<n;++itt)
#define FOR1(itt,n) for(int itt=1;itt<=n;++itt)
#define MAX_PRIME 1000010



int main()
{
    #ifdef pinanzo
        //read();
        //freopen("output.txt","w",stdout);
    #endif // pinanzo
    //ios_base::sync_with_stdio(0);
    //cin.tie(NULL);
    //cout.tie(NULL);
    int T, k;
    string s;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        cin>>s>>k;
        int len = s.size();
        int c = 0;
        bool flag = true;
        for(int i=0; i<len; ++i){
            if(s[i]=='-'){
                int j=i;
                ++c;
                cout << c << endl;
                while(j-i<k){
                    if(j==len)flag = false;
                    if(s[j]=='+')s[j]='-';
                    else s[j]='+';
                    ++j;
                }
            }
        }
        if(flag)printf("Case #%d: %d\n", t, c);
        else printf("Case #%d: IMPOSSIBLE\n", t);
    }

    return 0;
}

/// 13259
