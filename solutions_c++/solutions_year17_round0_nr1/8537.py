#include<string>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<unordered_map>
#include<string.h>
#include<queue>
#include<map>
using namespace std;
#define N 400005
#define INF 1100000000
map<string,int> mp;
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    int ca=0;
    scanf("%d",&t);
    while(t--)
    {
        mp.clear();
        string s;int k;
        cin>>s>>k;
        int len=s.length();
        mp[s]=1;
        queue<string> que;
        que.push(s);
        int ans=-1;
        while(que.size())
        {
            string p=que.front();que.pop();
            //cout<<p<<endl;
            int z=0;
            for(int i=0;i<len;i++)if(p[i]=='+')z++;else z--;
            if(z==len){ans=mp[p]-1;break;}
            for(int i=0;i+k<=len;i++)
            {
                string q=p;
               // cout<<q<<endl;
                for(int j=i;j<i+k;j++)
                    if(q[j]=='-')q[j]='+';
                        else q[j]='-';
               //         cout<<q<<endl;
                if(!mp[q])mp[q]=mp[p]+1,que.push(q);
            }
        }
        printf("Case #%d: ",++ca);
        if(ans==-1)
            puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }

    return 0;
}


