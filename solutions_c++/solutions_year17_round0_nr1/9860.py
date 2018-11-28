/*
#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int T;
    int a,b;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&a,&b);
        printf("%d\n",a+b+max(a,b));
    }
}
*/
/*
#include <stdio.h>
#include <iostream>
using namespace std;
char str[100];
int a[]={1,12,16};
int ch(char x)
{
    if(x=='H') return 0;
    else if(x=='C') return 1;
    else return 2;
}
int cnt[3];
int main()
{
    int t;

    scanf("%d",&t);
    while(t--)
    {
        for(int i=0;i<3;i++) cnt[i]=0;
        scanf("%s",str);
        for(int i=0;str[i];i++)
        {
            cnt[ch(str[i])]++;
            //cout<<cnt[ch(str[i])]<<"------"<<endl;
        }
        int ans=0;
        for(int i=0;i<3;i++)
            ans+=(cnt[i]*a[i]);
        printf("%d\n",ans);
    }
}
*/
/*
#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
typedef long long ll;
ll mod =2147493647;
struct M
{
    M()
    {
        memset(m,0,sizeof(m));
    }
    ll m[7][7];
    M operator * (const M &rhs) const
    {
        M c = M();
        for(int i=0;i<7;i++)
        {
            for(int j=0;j<7;j++)
            {
                for(int k=0;k<7;k++)
                {
                    c.m[i][j]=(c.m[i][j]+m[i][k]*rhs.m[k][j]%mod)%mod;
                }
            }
        }
        return c;
    }
};
int a[7][7]={
1,2,1,0,0,0,0,
1,0,0,0,0,0,0,
0,0,1,4,-6,4,-1,
0,0,0,1,3,3,1,
0,0,0,0,1,2,1,
0,0,0,0,0,1,1,
0,0,0,0,0,0,1
};


M mpow(M a,int n)
{
    M c = M();
    for(int i=0;i<7;i++)
        c.m[i][i]=1;
    while(n)
    {
        if(n&1) c = c*a;
        a=a*a;
        n>>=1;
    }
    return c;
}

int main()
{
    M mxt = M();
    for(int i=0;i<7;i++)
        for(int j=0;j<7;j++)
        mxt.m[i][j] = a[i][j];
    int T,n;
    M in = M();
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%I64d%I64d",&n,&in.m[1][0],&in.m[0][0]);
        in.[0][0]%=mod;in.[1][0]%=mod;
        in.m[2][0]=81;in.m[3][0]=64;in.m[4][0]=16;in.m[5][0]=4;in.m[6][0]=1;
        if(n==1) {printf("%I64d\n",in.m[1][0]);continue;}
        M p=mpow(mxt,n-2);
        in = p * in;
        printf("%I64d\n",in.m[0][0]);
    }
}
*/
/*
#include <stdio.h>
#include <vector>
#include <iostream>
#include <string.h>
#include <set>
#include <algorithm>
using namespace std;

vector<int> G[105];
bool maze[105][105];
int a[15];
int ans = 0;
int S;
int D[105];

struct P
{
    int m[10],len;
    P(){}
    P(int a[],int _len)
    {
        len = _len;
        for(int i=0;i<len;i++)
            m[i]=a[i];
        sort(m,m+len);
    }
    bool operator <(const P &rhs) const
    {
        for(int i=0;i<len;i++)
        {
            if(m[i]!=rhs.m[i])
                return m[i]<rhs.m[i];
        }
        return m[len-1]<rhs.m[len-1];
    }
};

set<P > s;

void dfs(int u,int cnt)
{
    if(cnt==S)
    {
//        P p = P(a,cnt);
//        //cout<<endl;
//        s.insert(p);


        ans++;
        return ;
    }
    for(int j=0;j<G[u].size();j++)
    {
        int v = G[u][j];
        bool flag = true;
        for(int k=0;k<cnt;k++)
        {
            if(!maze[a[k]][v])
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            a[cnt]=v;
            dfs(v,cnt+1);
        }
    }
}
int main()
{
    int T,n,m,u,v;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&m,&S);
        memset(maze,0,sizeof(maze));
        memset(D,0,sizeof(D));
        s.clear();
        for(int i=0;i<=n;i++)
        {
            G[i].clear();
        }
        ans = 0;
        for(int i=0;i<m;i++)
        {
            scanf("%d%d",&u,&v);
            if(u>v) swap(u,v);
            G[u].push_back(v);
            maze[u][v] = maze[v][u] = 1;
        }
        for(int i=1;i<=n;i++)
        {
            a[0]=i;
            dfs(i,1);
        }
        printf("%d\n",ans);
    }
}
*/


/*
#include <stdio.h>
#include <string.h>
int bi[200000*20][2];
int num[200000*20];
int cnt;
void add(int n)
{
    int now = 0;
    for(int i=31;i>=0;i--)
    {
        int x = (n>>i)&1;
        if(bi[now][x]==-1)
        {
            bi[now][x]=++cnt;
        }
        now = bi[now][x];
        num[now]++;
    }
}

void rm(int n)
{
    int now = 0;
    for(int i=31;i>=0;i--)
    {
        int x = (n>>i)&1;
        now = bi[now][x];
        num[now]--;
    }
}

int query(int n)
{
    int ret=0;
    int now = 0;
    for(int i=31;i>=0;i--)
    {
        int x = (n>>i)&1;
        if(bi[now][(x&1)^1]!=-1&&num[bi[now][(x&1)^1]])
        {
            ret+=(1<<i)*((x&1)^1);
            now = bi[now][(x&1)^1];
        }
        else if(bi[now][(x&1)]!=-1&&num[bi[now][(x&1)]])
        {
            ret+=(1<<i)*((x&1));
            now = bi[now][(x&1)];
        }
        else break;

    }
    return (ret^n)>n?(ret^n):n;
}

int main()
{
    int n,x;
    char str[10];
    while(~scanf("%d",&n))
    {
        cnt=0;
        memset(bi,-1,sizeof(bi));
        memset(num,0,sizeof(num));
        for(int i=0;i<n;i++)
        {
            scanf("%s%d",str,&x);
            if(str[0]=='+')
            {
                add(x);
            }
            else if(str[0]=='-')
            {
                rm(x);
            }
            else
            {
                printf("%d\n",query(x));
            }
        }
    }
    return 0;
}
*/
/*
#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;
int p[40005];
map<int,int> mp[40005];
int main()
{
    int T,n,m;
    int u,v,val;
    scanf("%d",&T);
    while(T--)
    {
        memset(p,0,sizeof(p));
        scanf("%d%d",&n,&m);
        for(int i=0;i<=n;i++) mp[i].clear();
        for(int i=0;i<n-1;i++)
        {
            scanf("%d%d%d",&u,&v,&val);
            if(val)
            {
                mp[u][v]=1;
                mp[v][u]=1;
                p[u]++;
                p[v]++;
            }
        }
        for(int i=0;i<m;i++)
        {
            scanf("%d",&val);
            if(val)
            {
                scanf("%d%d%d",&u,&v,&val);
                ////////////////
                if(mp[u][v]!=val){
                    mp[u][v]=val;
                    mp[v][u]=val;
                if(val) p[u]++,p[v]++;
                else p[u]--,p[v]--;
                }
            }
            else
            {
                scanf("%d",&val);
                if(p[val]&1)
                {
                    printf("Girls win!\n");
                }
                else printf("Boys win!\n");
            }
        }
    }
}
*/
/*
#include <stdio.h>
#include <vector>
#include <iostream>
#include <string.h>
using namespace std;
vector<int> G[1005];
int p[1005];
int c[1005];
int s[1005];
int dfs(int pre,int u,int cnt,int stu)
{
    c[u]=-1;
    for(int i=0;i<G[u].size();i++)
    {
        int v=G[u][i];
        if(stu&&s[v]==stu) return -1;
        if(v==pre) continue;
        if(c[v]<0)
        {
            if(cnt&1)
            return cnt;
        }
        else if(!c[v])
        {
            if(stu) stu = (stu%2)+1;
            int ret = dfs(u,v,cnt+1,stu);
            if(ret&1) return ret;
        }
    }
    c[u]=1;
    return 0;
}
int main()
{
    int n,m,x,y;
    int u,v;
    while(~scanf("%d%d%d%d",&n,&m,&x,&y))
    {
        for(int i=1;i<=n;i++)
            G[i].clear();
        memset(p,0,sizeof(p));
        memset(c,0,sizeof(c));
        memset(s,0,sizeof(s));
        for(int i=0;i<m;i++)
        {
            scanf("%d%d",&u,&v);
            G[v].push_back(u);
            G[u].push_back(v);
        }
        for(int i=0;i<x;i++)
        {
            scanf("%d",&u);
            s[u]=1;
        }
        for(int i=0;i<y;i++)
        {
            scanf("%d",&u);
            s[u]=2;
        }
        bool flag=true;
        for(int i=1;i<=n;i++)
        {
            if(G[i].size()==0&&s[i]==0)
            {
                flag = false;
                break;
            }
            int t = dfs(0,i,1,s[i]);
            //cout<<t;
            if(t==-1||t&1)
            {
                flag = false;
                break;
            }
        }
        if(flag) printf("YES\n");
        else printf("NO\n");
    }
}
*/




//
//#include <stdio.h>
//#include <iostream>
//#define KEY_NUM ch[ch[root][1]][0]
//using namespace std;
//
//const int N = 100010;
//long long val[N],maxx[N],size[N],add[N],fa[N],vale[N];
//int root,tot1,ch[N][2];
//
//
/////////////////////////////////////////
//
//
//void NewNode(int &r,int father,int k)//一个是调用的时候注意变量顺序，还有r必须引用&
//{
//    r=++tot1;
//    fa[r]=father;
//    size[r]=1;//这个不能忘记 ,一定是1，否则可能出错
//    val[r]=k;
//    add[r]=0;
//    maxx[r]=0;
//    ch[r][0]=ch[r][1]=0;
//}
//void pushup(int x);
//void pushdown(int x);
//void Build(int &x,int l,int r,int father)
//{
//    if(l>r)return;
//    int mid=(l+r)/2;
//    NewNode(x,father,vale[mid]);
//    Build(ch[x][0],l,mid-1,x);
//    Build(ch[x][1],mid+1,r,x);
//    pushup(x);
//}
//初始化，前后各加一个king结点
//void Init(int n)
//{
//    for(int i=1;i<=n;i++)scanf("%I64d",&vale[i]);
//    root=tot1=0;
//    ch[root][0]=ch[root][1]=fa[root]=size[root]=add[root]=maxx[root]=0;
//    val[root]=0;
//    NewNode(root,0,-1);
//    NewNode(ch[root][1],root,-1);//头尾各加入一个空位
//    Build(KEY_NUM,1,n,ch[root][1]);
//    pushup(ch[root][1]);
//    pushup(root);
//}
//
//int select(int r,int k)
//{
//    pushdown(r);
//    int t=size[ch[r][0]]+1;
//    if(t==k)return r;
//    if(t>k)return select(ch[r][0],k);
//    else return select(ch[r][1],k-t);
//}
//
//////////////////////////////////////////
//
//
//
//void pushdown(int x)
//{
//    if(add[x])
//    {
//        if(ch[x][0])
//        {
//            add[ch[x][0]]+=add[x];
//            val[ch[x][0]]+=add[x];
//            maxx[ch[x][0]]+=add[x]*size[ch[x][0]];
//        }
//        if(ch[x][1])
//        {
//            add[ch[x][1]]+=add[x];
//            val[ch[x][1]]+=add[x];
//            maxx[ch[x][1]]+=add[x]*size[ch[x][1]];
//        }
//        add[x]=0;
//    }
//}
//
//void pushup(int x)
//{
//    size[x]=1;
//    maxx[x]=val[x];
//    if(ch[x][0])
//    {
//        size[x]+=size[ch[x][0]];
//        maxx[x]+=maxx[ch[x][0]];
//    }
//    if(ch[x][1])
//    {
//        size[x]+=size[ch[x][1]];
//        maxx[x]+=maxx[ch[x][1]];
//    }
//}
//
//int select2(int x)
//{
//    int u = root;
//    pushdown(u);
//    while(size[ch[u][0]]+1!=x)
//    {
//        if(x<size[ch[u][0]]+1)
//        {
//            u = ch[u][0];
//        }
//        else
//        {
//            x -= size[ch[u][0]]+1;
//            u = ch[u][1];
//        }
//        pushdown(u);
//    }
//    return u;
//}
//
//void srotate(int x)
//{
//    int y = fa[x];
//    int z = fa[y];
//    pushdown(y);
//    pushdown(x);
//    int kind = (ch[y][1]==x);
//    fa[x]=z;
//    ch[z][(ch[z][1]==y)]=x;
//    ch[y][kind] = ch[x][!kind];
//    fa[ch[y][kind]]=y;
//    ch[x][!kind]=y;
//    fa[y]=x;
//    pushup(y);
//    pushup(x);
//}
//
//void splay(int x,int goal)
//{
//    while(fa[x]!=goal)
//    {
//        int y = fa[x];
//        int z = fa[y];
//        if(z==goal)
//        {
//            srotate(x);
//        }
//        else
//        {
//            srotate(x);
//            srotate(x);
//        }
//    }
//    if(!goal) root = x;
//}
//
//long long query(int l,int r)
//{
//    int x = select(root,l);
//    int y = select(root,r+2);
//    splay(x,0);
//    splay(y,root);
//    return maxx[KEY_NUM];
//}
//
//void update(int l,int r,int c)
//{
//    int x = select(root,l);
//    int y = select(root,r+2);
//    splay(x,0);
//    splay(y,root);
//    add[KEY_NUM]+=c;
//    val[KEY_NUM]+=c;
//    maxx[KEY_NUM]+=c*size[KEY_NUM];
//}
//
//int build(int l,int r)
//{
//    if(l==r)
//    {
//        size[l]=1;
//        ch[l][0] = ch[l][1] = 0;
//        maxx[l]=val[l];
//        return l;
//    }
//    else if(l>r)
//    {
//        return 0;
//    }
//    int mid = (l+r)>>1;
//    int ls = build(l,mid-1),rs = build(mid+1,r);
//    fa[ls] = fa[rs] = mid;
//    ch[mid][0]=ls;ch[mid][1]=rs;
//    pushup(mid);
//    return mid;
//}
//
//void init(int n)
//{
//    n+=2;
//    root = build(1,n);
//    fa[root]=0;
//    ch[0][1]=root;
//}
//
//int main()
//{
//    int n,m;
//    while(~scanf("%d%d",&n,&m))
//    {
//        Init(n);
//        for(int i=2;i<=n+1;i++)
//        {
//            scanf("%I64d",val+i);
//            maxx[i]=val[i];
//        }
//        char op[10];
//        for(int l,r,c,i=0;i<m;i++)
//        {
//            scanf("%s",op);
//            if(op[0]=='Q')
//            {
//                scanf("%d%d",&l,&r);
//                printf("%I64d\n",query(l,r));
//            }
//            else
//            {
//                scanf("%d%d%d",&l,&r,&c);
//                update(l,r,c);
//            }
//        }
//    }
//    return 0;
//}
//

//
//#include <stdio.h>
//#include <map>
//#include <string>
//#include <iostream>
//using namespace std;
//int main()
//{
//    int t,n;
//    cin>>t;
//    while(t--)
//    {
//        map<string,int> m1,m2;
//        string s;
//        int v;
//        cin>>n;
//        for(int i=0;i<n;i++)
//        {
//            cin>>s>>v;
//            if(m2[s]<v)
//            {
//                m1[s]=m2[s];
//                m2[s]=v;
//            }
//            else if(v>m1[s])
//            {
//                m1[s]=v;
//            }
//        }
//        int ans = 0;
//        for(map<string,int>::iterator i = m1.begin();i!=m1.end();i++)
//        {
//            ans += i->second;
//        }
//        for(map<string,int>::iterator i = m2.begin();i!=m2.end();i++)
//        {
//            ans += i->second;
//        }
//        cout<<ans<<"\n";
//    }
//}
//
//
//#include <stdio.h>
//#include <map>
//#include <string>
//#include <iostream>
//#include <set>
//#include <string.h>
//using namespace std;
//int s1[100005],s2[100005],s3[100005],s4[100005];
//struct E
//{
//    int u,v;
//}e[100005];
//int main()
//{
//    int t,n,m,u,v,k;
//    scanf("%d",&t);
//    while(t--)
//    {
//        scanf("%d%d%d",&n,&m,&k);
//        memset(s1,0,sizeof(s1));
//        memset(s2,0,sizeof(s2));
//        int cnt1=0,cnt2=0;
//        for(int i=0;i<k;i++)
//        {
//            scanf("%d%d",&u,&v);
//                s1[u]++;
//                s2[v]++;
//                e[i].u = u;
//                e[i].v = v;
//        }
//        long long ans = 0;
//        for(int i=0;i<k;i++)
//        {
//            ans+=(long long)(s1[e[i].u]-1)*(s2[e[i].v]-1);
//        }
//        printf("%lld\n",ans);
//    }
//}





///*******

///*******
//#include<cstdio>
//#include<queue>
//#include<vector>
//#include <string.h>
//#include <iostream>
//#include <algorithm>
//#include<map>
//#define  ull string
//using namespace std;
//int a[2000000];
//char buf[7000000];
//int dis[2000000];
//
//vector<int> g[2000000];
//
//int e,mind;
//void dfs(int now,int fa,int dep)
//{
//    dis[now] = max(dis[now],dep);
//    if(dis[now]>=mind)
//    {
//        e = now;
//        mind = dis[now];
//    }
//    for(int i=0; i<g[now].size(); i++)
//    {
//        int v = g[now][i];
//        if(v!=fa)
//            dfs(v,now,dep+1);
//    }
//}
//int p = 1000007;
//
//string gethash(int x,int fa)
//{
//    if(g[x].size()==1) return "x";
//    string ret = "";
//    vector<string> ans;
//    for(int i=0; i<g[x].size(); i++)
//    {
//        int v = g[x][i];
//        if(v!=fa)
//        {
//            string tmp ="";
//            int t = a[x]-a[v];
//            if(t)
//            {
//                while(t)
//                {
//                    tmp+=t%10+'0';
//                    t/=10;
//                }
//            }
//            else tmp = "0";
//            ans.push_back(tmp+","+gethash(v,x));
//        }
//    }
//    sort(ans.begin(),ans.end());
//    for(int i=0;i<ans.size();i++)
//        ret += ans[i]+"#";
//    return ret;
//}
//
//int xgethash(int x,int fa)
//{
//    if(g[x].size()==1) return 1;
//    int ret = 0;
//    vector<int> ans;
//    for(int i=0; i<g[x].size(); i++)
//    {
//        int v = g[x][i];
//        if(v!=fa)
//        {
//            ans.push_back(a[x]-a[v]+xgethash(v,x));
//        }
//    }
//    sort(ans.begin(),ans.end());
//    int base = p;
//    for(int i=0; i<ans.size(); i++)
//    {
//        ret+=base*ans[i];
//        base*=p;
//    }
//    return ret;
//}
//
//int main()
//{
//    freopen("test_case.in","r",stdin);
//    freopen("out.txt","w",stdout);
//    int n;
//    scanf("%d\n",&n);
//    map<pair<ull,ull> , int> mp;
//    int cnt=1;
//    for(int i=1; i<=n; i++)
//    {
//        //cout<<i<<endl;
//        for(int j=1; j<=cnt; j++)
//            g[j].clear();
//        cnt=1;
//        gets(buf);
//        int tmp = 0,u,v;
//        bool flag = 1;
//        for(int j=0;; j++)
//        {
//            if(buf[j])
//            {
//                if(buf[j]>='0'&&buf[j]<='9')
//                {
//                    tmp*=10;
//                    tmp+=buf[j]-'0';
//                }
//                else
//                {
//                    if(flag)
//                    {
//                        u = tmp;
//                        flag = 0;
//                        tmp=0;
//                    }
//                    else
//                    {
//                        v = tmp;
//                        flag = 1;
//                        g[u].push_back(v);
//                        g[v].push_back(u);
//                        cnt++;
//                        tmp=0;
//                    }
//                }
//            }
//            else
//            {
//                v = tmp;
//                g[u].push_back(v);
//                g[v].push_back(u);
//                cnt++;
//                break;
//            }
//        }
//        for(int j=1; j<cnt; j++)
//        {
//            scanf("%d",&a[j]);
//            dis[j]=0;
//        }
//        scanf("%d\n",&a[cnt]);
//        dis[cnt]=0;
//        e = 1;
//        mind = 0;
//        dfs(e,0,0);
//        dfs(e,0,0);
//        dfs(e,0,0);
//        int x = -1,y = -1;
//        for(int j=1; j<=cnt; j++)
//        {
//            if(dis[j]<=mind)
//            {
//                y = x;
//                x = j;
//                mind = dis[j];
//            }
//        }
//        if(y==-1||dis[x]!=dis[y])
//        {
//            cout<<x<<"-------"<<endl;
//            ull hs = gethash(x,0);
//            pair<ull,ull> pir;
//            pir.first = hs;
//            pir.second = "";
//            mp[pir]+=1;
//        }
//        else
//        {
//            cout<<x<<"-------"<<y<<" "<<dis[x]<<" "<<dis[y]<<endl;
//            ull hs1 = gethash(x,0);
//            ull hs2 = gethash(y,0);
//            if(hs1>hs2) swap(hs1,hs2);
//            pair<ull,ull> pir;
//            pir.first = hs1;
//            pir.second = hs2;
//            mp[pir]+=1;
//        }
//    }
//    vector<int> ans;
//    for(map<pair<ull,ull>,int>::iterator it = mp.begin(); it!=mp.end(); it++)
//    {
//        ans.push_back(it->second);
//    }
//    sort(ans.begin(),ans.end());
//    printf("%d",ans[0]);
//    for(int j=1; j<ans.size(); j++)
//        printf(" %d",ans[j]);
//    printf("\n");
//    return 0;
//}
//
//#include<map>
//#include <set>
//#include <stdio.h>
//#include <string>
//#include <iostream>
//#include <queue>
//#include <algorithm>
//#include <vector>
//#include <cmath>
//#define ll long long
//using namespace std;
//
//int a[100005],t[100005],hs[100005],invhs[100005];
//vector<int> vec[20005];
//int main()
//{
//    int n;
//    char buf[10];
//    scanf("%d",&n);
//    int addcnt=0;
//    for(int tt=0; tt<n; tt++)
//    {
//        scanf("%s",buf);
//        if(buf[0]=='a')
//        {
//            scanf("%d",&a[tt]);
//            hs[tt]=a[tt];
//            t[tt]=0;
//            addcnt++;
//        }
//        else if(buf[0]=='d')
//        {
//            scanf("%d",&a[tt]);
//            t[tt]=1;
//            hs[tt]=a[tt];
//        }
//        else
//        {
//            t[tt]=2;
//        }
//    }
//    sort(hs,hs+n);
//    int cnt = unique(hs,hs+n) - hs;
//    for(int i=0;i<n;i++)
//    {
//        if(t[i]==0)
//        {
//            int tmp  = lower_bound(hs,hs+cnt,a[i]) - hs;
//            invhs[tmp] = a[i];
//            a[i] = tmp;
//            int index = a[i]/5;
//            vector<int>::iterator it = lower_bound(vec[index].begin(),vec[index].end(),a[i]);
//            vec[index].insert(it,a[i]);
//        }
//        else if(t[i]==1)
//        {
//            int tmp  = lower_bound(hs,hs+cnt,a[i]) - hs;
//            invhs[tmp] = a[i];
//            a[i] = tmp;
//            int index = a[i]/5;
//            vector<int>::iterator it = lower_bound(vec[index].begin(),vec[index].end(),a[i]);
//            vec[index].erase(it);
//        }
//        else
//        {
//            long long ans = 0;
//            for(int k=2,c=0,j=0;k<addcnt;k+=5)
//            {
//                while(k-c>(int)vec[j].size()-1&&j<cnt/5+1)
//                {
//                    c+=vec[j].size();
//                    ++j;
//                }
//                if((int)vec[j].size()>k-c) ans+=invhs[vec[j][k-c]];
//            }
//            printf("%I64d\n",ans);
//        }
//    }
//    return 0;
//}


#include <stdio.h>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <map>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;



int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ios::sync_with_stdio(false);
    int T;
    cin>>T;
    for(int cas = 1;cas<=T;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        string str="";
        cin>>str;
        int num;
        cin>>num;
        set<string> s;
        queue<string> q;
        queue<int> ansq;
        q.push(str);
        ansq.push(0);
        int ans = 0;
        int len = str.length();
        while(!q.empty())
        {
            str = q.front();
            s.insert(str);
            ans = ansq.front();
            q.pop();
            ansq.pop();
            if(-1==str.find("-"))
                break;
            for(int i=0;i<=len-num;i++)
            {
                string tmp = str;
                for(int j=0;j<num;j++)
                {
                    if(str[i+j]=='+')
                        tmp[i+j] = '-';
                    else tmp[i+j] = '+';
                }
                if(!s.count(tmp))
                   {q.push(tmp);
                ansq.push(ans+1);
                   }
            }
        }
        if(-1==str.find("-"))
        {
            cout<<ans<<"\n";
        }
        else cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
