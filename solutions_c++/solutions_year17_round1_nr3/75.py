#include<bits/stdc++.h>
using namespace std;

set<tuple<int,int,int,int>> turn;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        turn.clear();
        printf("Case #%d: ",t);
        int HD, AD, HK, AK, b, d, ans = -1;
        scanf("%d%d%d%d%d%d",&HD,&AD,&HK,&AK,&b,&d);
        queue<tuple<int,int,int,int,int>> q;
        q.emplace(0,HD,AD,HK,AK);
        turn.emplace(HD,AD,HK,AK);
        while(!q.empty())
        {
            int n,hd,ad,hk,ak;
            tie(n,hd,ad,hk,ak) = q.front();
            q.pop();
            if(ad >= hk)
            {
                ans = n+1;
                break;
            }
            int x = hd-ak, y = ad, z = hk-ad, w = ak;
            if(x>0)
            {
                tuple<int,int,int,int> tp = {x,y,z,w};
                if(turn.find(tp) == turn.end())
                {
                    turn.insert(tp);
                    q.emplace(n+1,x,y,z,w);
                }
            }

            if(b)
            {
                x = hd-ak, y = ad+b, z = hk, w = ak;
                if(x>0)
                {
                    tuple<int,int,int,int> tp = {x,y,z,w};
                    if(turn.find(tp) == turn.end())
                    {
                        turn.insert(tp);
                        q.emplace(n+1,x,y,z,w);
                    }
                }
            }
            if(hd<HD && ak)
            {
                x = HD-ak, y = ad, z = hk, w = ak;
                if(x>0)
                {
                    tuple<int,int,int,int> tp = {x,y,z,w};
                    if(turn.find(tp) == turn.end())
                    {
                        turn.insert(tp);
                        q.emplace(n+1,x,y,z,w);
                    }
                }
            }
            if(d && ak)
            {
                y = ad, z = hk, w = max(ak-d,0), x = hd - w;
                if(x>0)
                {
                    tuple<int,int,int,int> tp = {x,y,z,w};
                    if(turn.find(tp) == turn.end())
                    {
                        turn.insert(tp);
                        q.emplace(n+1,x,y,z,w);
                    }
                }
            }
        }
        if(ans >=0) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
}
