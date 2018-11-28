#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int n;
char s[1010];
int add[1010];

int main()
{
#ifndef ONLINE_JUDGE
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
#endif // ONLINE_JUDGE
    int t, cas=0;
    cin>>t;
    while(cas++ < t)
    {
        printf("Case #%d: ",cas);
        scanf("%s%d", s+1, &n);
        int len = strlen(s+1);
        memset(add,0,sizeof add);
        bool ok = true;
        int ans = 0;

        //cout<<s+1<<" "<<n<<endl;
        for(int i=1; i<=len; i++){
            add[i] += add[i-1];
            //cout<<s[i]<<" "<<add[i]<<endl;
            if(s[i] == '-' && add[i]%2 == 0 || s[i] == '+' && add[i]%2==1){
                //cout<<"fsdf"<<endl;
                add[i] ++;
                add[i+n] --;
                ans ++;
                if(i + n > len + 1) {
                    ok = false;
                    break;
                }
            }
        }
        if(ok) cout<<ans<<endl;
        else puts("IMPOSSIBLE");
    }
    return 0;
}
