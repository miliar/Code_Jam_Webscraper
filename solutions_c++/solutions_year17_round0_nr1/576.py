#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;

int a[1100];

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        printf("Case #%d: ",test);
        string s;
        int k;
        cin >> s >> k;
        memset(a,0,sizeof(a));
        int ans=0;
        int d=0;
        bool bad=false;
        for(int i=0;i<s.length();++i)
        {
            d+=a[i];
            int p = (s[i]=='+'?1:0);
            if(d%2) p=1-p;
            if(!p)
            {
                ans++;
                d++;
                if(i+k<=s.length())
                    a[i+k]--;
                else
                    bad=true;
            }
        }
        if(bad)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }

}

