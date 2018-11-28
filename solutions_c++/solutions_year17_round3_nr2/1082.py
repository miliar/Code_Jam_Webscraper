#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

struct Span
{
    int c,d;
    int f;
    bool operator<(const Span&obj) const {return c<obj.c;}
}sp[400];
struct Node
{
    int l,f;
    bool operator<(const Node&obj){return l<obj.l;}
};
vector<Node> node;
int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    cin >> T;
    while(T--)
    {
        node.clear();
        printf("Case #%d: ",++cas);
        int n[2],N;
        cin >> n[0] >> n[1];
        N=n[0]+n[1];
        int t[2];
        t[0]=t[1]=0;
        for(int i=1;i<=n[0];i++)
            cin >> sp[i].c >> sp[i].d, sp[i].f=0,t[1]+=sp[i].d-sp[i].c;
        for(int i=n[0]+1;i<=n[0]+n[1];i++)
            cin >> sp[i].c >> sp[i].d, sp[i].f=1,t[0]+=sp[i].d-sp[i].c;
        sort(sp+1,sp+1+n[0]+n[1]);
        t[0]=720-t[0];
        t[1]=720-t[1];
        int ans=0;
//        cout << N << endl;
        if(N)
        {
            for(int i=1;i<=N;++i)
            {
                int j=i%N+1;
                if(sp[i].f==sp[j].f)
                {
                    ans+=2;
                    node.push_back(Node{(sp[j].c-sp[i].d+1440)%1440,1-sp[i].f});
                }
                else ans++;
            }
//            cout << node.size() <<ans << endl;
            for(int i=0;i<node.size();++i)
                if(node[i].l<=t[node[i].f])
                    t[node[i].f]-=node[i].l,ans-=2;

//            int f=1-sp[1].f;
//            int ff=-1;
//            for(int j=2;j<=N+1;++j)
//            {
//                cout << j << " " << f << " " << ff << endl;
//                int i=(j-1)%N+1;
//                int tmp=t[f]+sp[i-1].d;
//                cout << sp[i].c <<" " << sp[i].d << " " << tmp << " " << t[f] << endl;
//                if(ff!=f)
//                {
//
//                if(tmp>=sp[i].c) t[f]-=sp[i].c-sp[i-1].d;
//                else {
//                        t[f]=0,ff=f;
//                        t[1-f]-=sp[i].c-tmp;
//                    ans++;
//                    f=1-f;
//                }
//                }
//                else
//                {
////                    if (f==ff)
////                    {
//                        f=1-f;
//                        ans++;
////                    }
//                }
//                if(f!=1-sp[i].f)
//                {
//                    f=1-sp[i].f;
//                    ans++;
//                }
//            }
        }
//        cout << ans << endl;
        printf("%d\n",max(2,ans));
    }
    return 0;
}

