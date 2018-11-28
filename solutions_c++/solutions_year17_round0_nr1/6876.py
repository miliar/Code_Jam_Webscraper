#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in11.txt","r",stdin);
    freopen("out11.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int t1=1;
    while(t--){

        printf("Case #%d: ",t1++);
        string s;
        int K;
        cin>>s;
        scanf("%d",&K);
        int i=0;
        int ans=0;
        bool pos=1;
        while(1){

            if(i==s.size())
            break;
            if(s.at(i)=='+')
            {
                ++i;continue;
            }
            else{
                if(i+K-1>=s.size())
                {
                    pos=0;
                    break;
                }
                for(int j=i;j<=i+K-1;++j)
                    s[j]=s[j]=='-'?'+':'-';
                ++ans;
                ++i;
            }
            if(i==s.size()-1 && s.at(i)=='-')
                pos=0;

        }
        if(pos)
            printf("%d\n",ans);
        else
            printf("IMPOSSIBLE\n");
    }

    return 0;
}
