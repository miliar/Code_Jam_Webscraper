//#include<iostream>
//#include<algorithm>
//#include<cstdio>
//#include<cstring>
//#include<queue>
//#include<map>
//using namespace std;
//#define abs(x) ((x)<0?-(x):(x))
//#define min(x,y) (x<y?x:y)
//const int maxn = 1005<<1;
//const int maxm = (maxn*maxn)<<1;
//const int inf = 1e8;
//
//int edge[maxn][maxn];
//struct E
//{
//    int x1,y1,x2,y2,w;
//}s[maxn];
//
//int dis[maxn],vis[maxn];
//
//int n,x0,y0;
//
//void init()
//{
//    memset(vis,0,sizeof(vis));
//    memset(edge,-1,sizeof(edge));
//}
//
//
//int spfa()
//{
//    for(int i=1;i<=n;i++)dis[i]=inf;
//    dis[1]=0,vis[1]=1;
//    queue<int>q;
//    q.push(1);
//    while(!q.empty())
//    {
//        int u = q.front();
//        q.pop();
//        vis[u]=0;
//        for(int i=1;i<=n;i++)
//        {
//            if(edge[u][i]==-1)continue;
//            int v = i;
//            if(dis[v]>dis[u]+edge[u][i])
//            {
//                dis[v]=dis[u]+edge[u][i];
//                if(!vis[v])
//                {
//                    vis[v]=1;
//                    q.push(v);
//                }
//            }
//        }
//    }
//    return min(dis[n],dis[n-1]);
//}
//
//int main()
//{
//    int t;cin>>t;
//    while(t--)
//    {
//        int x,y,k;
//        scanf("%d%d%d",&x,&y,&k);
//        scanf("%d%d",&x0,&y0);
//        n = k*2+3;
//        init();
//        edge[1][n-1]=abs(x-x0)+abs(y-y0);
//        edge[1][n] = x0+y0-2;
//        for(int i=1;i<=k;i++)
//        {
//            scanf("%d%d%d%d%d",&s[i].x1,&s[i].y1,&s[i].x2,&s[i].y2,&s[i].w);
//            edge[1][i*2] = abs(s[i].x1-x0)+abs(s[i].y1-y0);
//            edge[1][i*2+1] = abs(s[i].x2-x0)+abs(s[i].y2-y0);
//
//            edge[i*2][n-1] =abs(s[i].x2-x)+abs(s[i].y2-y)+s[i].w ;
//            edge[i*2][n] = s[i].x2+s[i].y2-2+s[i].w;
//
//            edge[i*2+1][n-1] = abs(s[i].x1-x)+abs(s[i].y1-y)+s[i].w;
//            edge[i*2+1][n] = s[i].x1+s[i].y1-2+s[i].w;
//        }
//        for(int i=1;i<k;i++)
//        {
//            for(int j=i+1;j<=k;j++)
//            {
//                edge[i*2][j*2] = abs(s[i].x2-s[j].x1)+abs(s[i].y2-s[j].y1)+s[i].w;
//                edge[i*2][j*2+1] = abs(s[i].x2-s[j].x2)+abs(s[i].y2-s[j].y2)+s[i].w;
//
//                edge[i*2+1][j*2] = abs(s[i].x1-s[j].x1)+abs(s[i].y1-s[j].y1)+s[i].w;
//                edge[i*2+1][j*2+1] = abs(s[i].x1-s[j].x2)+abs(s[i].y1-s[j].y2)+s[i].w;
//
//                edge[j*2][i*2] = abs(s[j].x2-s[i].x1)+abs(s[j].y2-s[i].y1)+s[j].w;
//                edge[j*2][i*2+1] = abs(s[j].x2-s[i].x2)+abs(s[j].y2-s[i].y2)+s[j].w;
//
//                edge[j*2+1][i*2] = abs(s[j].x1-s[i].x1)+abs(s[j].y1-s[i].y1)+s[j].w;
//                edge[j*2+1][i*2+1] = abs(s[j].x1-s[i].x2)+abs(s[j].y1-s[i].y2)+s[j].w;
//            }
//        }
//        printf("%d\n",spfa());
//    }
//    return 0;
//}






//#include<algorithm>
//#include<iostream>
//#include<cstring>
//#include<cstdio>
//#include<vector>
//#include<queue>
//using namespace std;
//int n;
//vector<int>mp[10005];
//
//int in[10005],vis[10005];
//int ans;
//void init()
//{
//    ans = 0;
//    for(int i=1;i<=n;i++)
//    {
//        mp[i].clear();
//        in[i]=0;
//        vis[i]=0;
//    }
//}
//
//int solve()
//{
//    queue<int>q;
//    for(int i=1;i<=n;i++)
//        if(in[i]==1)q.push(i);
//    while(!q.empty())
//    {
//        int u = q.front();
//        q.pop();
//        if(vis[u])continue;
//        in[u]--;
//        vis[u] = 1;
//        int v = mp[u][0];
//        in[v]--;
//        if(!vis[v])
//        {
//            int len = mp[v].size();
//            ans++;
//            vis[v]=1;
//            for(int i=0;i<len;i++)
//            {
//                int vv = mp[v][i];
//                if(!vis[vv])
//                {
//                    if(in[vv]==2)
//                    {
//                        q.push(vv);
//                    }
//                }
//            }
//        }
//    }
//
//    if(n==1)ans = 1;
//    return ans;
//
//}
//
//int main()
//{
//    while(cin>>n)
//    {
//        init();
//        for(int i=1;i<n;i++)
//        {
//            int x,y;scanf("%d%d",&x,&y);
//            mp[x].push_back(y);
//            mp[y].push_back(x);
//            in[x]++,in[y]++;
//        }
//        cout<<solve()<<endl;
//    }
//
//    return 0;
//}




/**
  第七届省赛四川大学oj

*/

/** A  */



//#include<cstdio>
//#include<cmath>
//using namespace std;
//int main()
//{
//    double x;
//    int flag;
//    int n;
//    while(~scanf("%d",&n))
//    {
//        flag = 1;
//        for(int i=0;i<n;i++)
//        {
//            scanf("%lf",&x);
//            double y = sqrt(x);
//            int yy = y;
//            int xx = x;
//            if(y*y!=x)flag = 0;
//        }
//        if(flag) printf("Yes\n");
//        else printf("No\n");
//    }
//    return 0;
//}


/** C  */
//#include<iostream>
//#include<algorithm>
//#include<cstdio>
//#include<cstring>
//using namespace std;
//const int maxn = 5e6+10;
//int Next[maxn];
//char  s1[maxn],s2[maxn];
//int len1,len2;
//int len;
//struct st
//{
//  int id;
//  char ch;
//}ans[maxn];
//char ans1[maxn];
//void getNext()
//{
//    int i=-1,j=0;
//    Next[0]=-1;
//    while(j<len1)
//    {
//        if(i==-1||s1[i]==s1[j])
//        {
//            ++i,++j;
//            Next[j]=i;
//        }
//        else
//        {
//            i=Next[i];
//        }
//
//    }
//
//
//}
//
//void KMP()
//{
//    int i= 0,j=0;
//    while(j<len2)
//    {
//        if(i==-1||s1[i]==s2[j])
//        {
//
//            if(i==-1)
//            {
//                ans[len].ch = s2[j];
//                ans[len++].id = -1;
//            }
//            else
//            {
//                ans[len].ch = s2[j];
//                ans[len++].id = i;
//            }
//
//            i++,j++;
//
//        }else i = Next[i];
//
//        if(i==len1)
//        {
//            len-=len1;
//            if(len==0)i=0;
//            else
//            {
//                i=ans[len-1].id+1;
//            }
//        }
//    }
//}
//
//int main()
//{
//    while(~scanf("%s %s",s1,s2))
//    {
//        len1 = strlen(s1);
//        len2 = strlen(s2);
//        if(len1>len2)
//        {
//            printf("%s\n",s2);
//            continue;
//        }
//        len = 0;
//        getNext();
//        KMP();
//        for(int i=0;i<len;i++)ans1[i]=ans[i].ch;
//        ans1[len] = '\0';
//        printf("%s\n",ans1);
//    }
//
//    return 0;
//}



//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//using namespace std;
//int main()
//{
//    int i;
//    for(i=1;i<=99;i++){
//        int j = (i%10*10+i/10);
//        if(j+i-abs(j-i)==32)break;
//    }
//    cout<<i<<endl;
//    return 0;
//}


//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//using namespace std;
//int main()
//{
//    int x,y,z;
//    int ans = 100000;
//    for(x=1;x<=300;x++)
//    {
//        for(y=1;y<=300;y++)
//        {
//            for(z=1;z<=300;z++)
//            {
//                if(x*11+13*y+17*z==2471&&x*13+y*17+z*11==2739)
//                {
//                    ans = min(ans,x+y+z);
//                }
//            }
//        }
//    }
//    cout<<ans<<endl;
//    return 0;
//}


//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//using namespace std;
//int main()
//{
//    int ans = 0;
//    int s[9]={1,2,3,4,5,6,7,8,9};
//    do{
//            int a=s[0]+s[1]+s[2],b=s[3]+s[4]+s[5],c=s[6]+s[7]+s[8];
//            int d = s[0]+s[3]+s[6],e= s[1]+s[4]+s[7],f = s[2]+s[5]+s[8];
//        if(a==b&&c==a&&d==e&&d==f)ans++;
//    }while(next_permutation(s,s+9));
//    cout<<ans<<endl;
//    return 0;
//}


//#include <stdio.h>
//#include <algorithm>
//
//long long test(int a[], int n) {
//	long long ret = 0;
//	for (int i = 0; i < n; ++i) {
//		int tp = a[i];
//		int j = 1;
//		while(tp) {
//			j *= 10;
//			tp /= 10;
//		}
//		ret = ret * j + a[i];
//	}
//	return ret;
//}
//
//long long f(int a[], int k) {
//	if (k == 6) {
//		return test(a, k);
//	}
//	long long ret = 0;
//	for(int i = k; i < 6; ++i) {
//		int t = a[k];
//		a[k] = a[i];
//		a[i] = t;
//		ret = std::max(ret,f(a,k+1));
//		t = a[k];
//		a[k] = a[i];
//		a[i] = t;
//	}
//	return ret;
//}
//
//int main() {
//	int a[6] = {517, 283, 429, 65, 6566, 32};
//	printf("%lld\n", f(a, 0));
//	return 0;
//}


//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//using namespace std;
//int main()
//{
//    int ans = 0;
//    int s[13]={1,2,3,4,5,6,7,8,9,10,11,12,13};
//    do{
//        if(s[0]*s[1]+s[2]*s[3]==s[4]*s[5]&&s[6]*s[7]-s[8]*s[9]==s[10]*s[11])ans++;
//    }while(next_permutation(s,s+13));
//    cout<<ans<<endl;
//    return 0;
//}
/** 122368  */


//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//using namespace std;
//int main()
//{
//    int s[36] = {
//       3,
//   8   ,
//   11  ,
//  13,
//1   ,
//2    ,
//6   ,
//10  ,
//  11,
//10  ,
//6   ,
//5    ,
//2   ,
//  10,
//4    ,
//7    ,
//5   ,
//5   ,
//15  ,
//3   ,
//  11,
//7   ,
//11  ,
//9   ,
// 4,
//9   ,
//4   ,
//10  ,
//12  ,
//3,
//   9,
//  16,
//11  ,
//2,
//  15,
//3
//
//    };
//
//    sort(s,s+36);
//    int i=0,ans = 0;
//    for(i;i<36;i++){
//        ans+=s[i];
//        cout<<ans<<" "<<i<<endl;
//    }
//    return 0;
//}


//#include<algorithm>
//#include<iostream>
//#include<cstdio>
//#include<cstring>
//#include<string>
//#include<map>
//using namespace std;
//int main()
//{
//    map<string,int>mp;
//    string x,y;
//    while(cin>>x&&x[0]!='e')
//    {
//        int d;
//        cin>>y;
//        if(x[0]=='i')
//        {
//            cin>>d;
//            if(mp[y]==0)mp[y]=d+1;
//            else mp[y]=max(mp[y],d+1);
//        }
//        else
//        {
//            cout<<mp[y]-1<<endl;;
//        }
//    }
//
//    return 0;
//}


//#include<bits/stdc++.h>
//using namespace std;
//
//char mp[1005][1005];
//int cnt[1005][1005],vis[1005][1005];
//int n,m;
//struct st
//{
//    int x,y;
//    int cnt[4];
//    st(){
//        cnt[0]=cnt[1]=cnt[2]=cnt[3]=-1;
//    }
//
//}s[1005*1005];
//
//void dfs(int x,int y)
//{
//    vis[x][y]=1;
//    int num = cnt[x][y];
//    for(int i=0;i<4;i++)
//    {
//        int num1 = s[num].cnt[i];
//        if(num1!=-1&&!vis[s[num1].x][s[num1].y])
//        {
//             dfs(s[num1].x,s[num1].y);
//        }
//    }
//
//}
//
//int main()
//{
//    memset(cnt,-1,sizeof(cnt));
//    memset(vis,0,sizeof(vis));
//    scanf("%d%d",&n,&m);
//    int num = 0;
//    for(int i=0;i<n;i++)
//    {
//        int x=-1,y=-1;
//        scanf("%s",mp[i]);
//        for(int j=0;j<m;j++)
//        {
//            if(mp[i][j]=='1')
//            {
//                cnt[i][j]=++num;
//                s[num].x=i,s[num].y=j;
//                if(x!=-1)
//                {
//                    s[num].cnt[0]=cnt[x][y];
//                    s[cnt[x][y]].cnt[1]=cnt[i][j];
//                }
//                x = i,y = j;
//            }
//
//        }
//    }
//    for(int j=0;j<m;j++)
//    {
//        int x=-1,y=-1;
//        for(int i=0;i<n;i++)
//        {
//            if(mp[i][j]=='1')
//            {
//                num = cnt[i][j];
//                if(x!=-1)
//                {
//                    s[num].cnt[2]=cnt[x][y];
//                    s[cnt[x][y]].cnt[3]=cnt[i][j];
//                }
//                x = i,y = j;
//
//            }
//
//        }
//    }
//    int ans = 0;
//
//    for(int i=0;i<n;i++)
//    {
//        for(int j=0;j<m;j++)
//        {
//            if(mp[i][j]=='1'&&!vis[i][j])
//            {
//                dfs(i,j);
//                ans++;
//            }
//        }
//    }
//    cout<<ans<<endl;
//    return 0;
//}




//#include<bits/stdc++.h>
//#include<string>
//#include<string.h>
//using namespace std;
//int s[10] = {0,1,2,3,4,5,6,7,8,9};
//map<long long,int>mp;
//map<string,int>mp1;
//int flag;
//int ans;
//long long aa[100000][10];
//void dfs(int x,long long ss[10],int cnt)
//{
//    if(x==10)
//    {
//        long long ss1[10]= {0};
//        for(int i=0; i<cnt; i++)ss1[i]=ss[i];
//        sort(ss1,ss1+cnt);
//        string s1 = "";
//        for(int i=0; i<cnt; i++)
//        {
//            long long xx = ss1[i];
//            string s2="";
//            while(xx)
//            {
//                s2+=(xx%10+'0');
//
//                xx/=10;
//            }
//            if(ss1[i]==0)s2+='0';
//            reverse(s2.begin(),s2.end());
//            s1+=s2;
//            s1+='#';
//        }
//        if(!mp1[s1])
//        {
//            ans++;
//            mp1[s1]=1;
//        }
//        return ;
//    }
//    long long sum = 0;
//    for(int i=x; i<10; i++)
//    {
//        if(sum==0&&s[i]!=0&&i!=x)return;
//        sum=sum*10ll+s[i];
//        if(mp[sum])
//        {
//            ss[cnt]=sum;
//            dfs(i+1,ss,cnt+1);
//        }
//    }
//
//}
//
//int main()
//{
//    string dd;
//    dd+=to_string(100);
//    for(long long i=0; i<=100000; i++)
//    {
//        long long j = i*i;
//        mp[j]=1;
//    }
//    ans = 0;
//    do
//    {
//        long long ss[10];
//        dfs(0,ss,0);
//    }
//    while(next_permutation(s,s+10));
//    cout<<ans<<endl;
//    return 0;
//}

//#include<cstdio>
//#include<iostream>
//#include<algorithm>
//#include<queue>
//using namespace std;
//int n,k;
//int ini[5005],d[5005];
//
//struct st{
//    int v;
//    int id;
//    st(int v,int id):v(v),id(id){}
//    st(){}
//    bool operator <(const st &a )const{
//        if(v==a.v)return d[a.id]<d[id];
//        return a.v<v;
//    }
//};
//
//int main ()
//{
//
//    while(~scanf("%d%d",&n,&k))
//    {
//        priority_queue<st>q;
//        for(int i=0;i<n;i++)
//        {
//            scanf("%d",&ini[i]);
//            q.push(st(ini[i],i));
//        }
//        for(int i=0;i<n;i++)
//        {
//            scanf("%d",&d[i]);
//        }
//        int ans  = 0;
//        while(k)
//        {
//            st a = q.top();
//            q.pop();
//            ans += a.v;
//            k--;
//            q.push(st(a.v+d[a.id],a.id));
//        }
//        cout<<ans<<endl;
//    }
//
//
//    return 0;
//}

//#include<iostream>
//#include<algorithm>
//#include<cstdio>
//using namespace std;
//
//int main()
//{
//    freopen("4.in","r",stdin);
//    freopen("4.out","w",stdout);
//    int t;
//    cin>>t;
//    int T = 1;
//    while(t--)
//    {
//        long long int n;
//        scanf("%lld",&n);
//        int s[20];
//        int len = 0;
//        while(n)
//        {
//            s[len++]=n%10;
//            n/=10;
//        }
//        for(int i=1;i<len;i++)
//        {
//            if(s[i]<=s[i-1])continue;
//            s[i]--;
//            for(int j=i-1;j>=0;j--)s[j]=9;
//        }
//        printf("Case #%d: ",T++);
//        if(s[len-1]==0)len--;
//        for(int i=len-1;i>=0;i--)printf("%d",s[i]);
//        cout<<endl;
//    }
//
//    return 0;
//}


#include<iostream>
#include<algorithm>
#include<cstdio>
#include<map>
#include<string>
#include<queue>
#include<cstring>
using namespace std;
struct nod{
    string s;
    int cnt;
    nod(string s,int cnt):s(s),cnt(cnt){}
    nod(){}
};
map<string,int>mp;
int k,ans,flag,len;
string s;
bool bfs()
{
    queue<nod>q;
    q.push(nod(s,0));
    len = s.size();
    while(!q.empty())
    {
        nod a = q.front();
        q.pop();
        s = a.s;
        if(mp[s])continue;
        mp[s]=1;
        int num = 0;
        for(int j=0;j<len;j++)
            if(s[j]=='+')num++;
        if(num==len)
            {
                ans = a.cnt;
                return true;
            }
        for(int i=0;i<=len-k;i++)
        {
            string ss = s;

            for(int j=i;j<k+i;j++)
            {
                if(ss[j]=='-')ss[j]='+';
                else ss[j]='-';
            }


            if(!mp[ss])
            {
                q.push(nod(ss,a.cnt+1));
            }
        }
    }
    return false;
}


int main()
{
    freopen("5.in","r",stdin);
    freopen("5.out","w",stdout);
    int t;
    cin>>t;
    int T = 1;
    while(t--)
    {
        mp.clear();
        cin>>s;
        cin>>k;
        ans = 0;
        printf("Case #%d: ",T++);
        if(bfs())
        {
            cout<<ans<<endl;
        }
        else cout<<"IMPOSSIBLE"<<endl;
    }

    return 0;
}
