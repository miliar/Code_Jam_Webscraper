#include<bits/stdc++.h>
#define X first
#define Y second
using namespace std;

typedef pair<int,int> pii;
const int maxn=3000;
char c[60][60];
bool mark[60][60],des,pos,mark2[maxn];
int n,m,col[maxn],cmp,cnt,N,a[60][60];
vector<int>G[maxn],G1[maxn],topo,f[maxn];
vector<pii>tmpvec,vec;
pii place[maxn];

int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};

int rev(int x) {return 2*N-x-1;}

bool fin(int x,int y)
{
    return (x<0 || x>=n || y<0 ||y>=m || c[x][y]=='#');
}

bool lazer(int x,int y)
{
    return (c[x][y]=='|' || c[x][y]=='-');
}

void dfs(int x,int y,int dir)
{
    x+=dx[dir],y+=dy[dir];
   // cout<<x<<" "<<y<<" "<<dir<<endl;
    if(fin(x,y)) return;
    if(lazer(x,y)) {des=true;return;}
    if(c[x][y]=='.' && !mark[x][y]) tmpvec.push_back(pii(x,y));
    mark[x][y]=true;
    if(c[x][y]=='\\') dir^=3;
    if(c[x][y]=='/') dir^=1;
    dfs(x,y,dir);
}

void add_edge(int v,int u)
{
    G[v].push_back(u);
    G1[u].push_back(v);
}

void dfsrev(int v)
{
    col[v]=cmp;
    mark2[v]=true;
    for(int i=0;i<G1[v].size();i++)
    {
        int u=G1[v][i];
        if(!mark2[u])
            dfsrev(u);
    }
}

void dfs1(int v)
{
    mark2[v]=true;
    for(int i=0;i<G[v].size();i++)
    {
        int u=G[v][i];
        if(!mark2[u])
            dfs1(u);
    }
    topo.push_back(v);
}

void twoSAT()
{
    memset(mark2,false,sizeof mark2);
    topo.clear();
    for(int i=0;i<2*N;i++)
        if(!mark2[i])
            dfs1(i);
    memset(mark2,false,sizeof mark2);
    cmp=0;
    for(int i=topo.size()-1;i>-1;i--)
    {
        int v=topo[i];
        if(!mark2[v])
        {
            cmp++;
            dfsrev(v);
        }
    }
    for(int i=0;i<N;i++) {
        if(col[i]==col[rev(i)]) pos=false;
        else if(col[i]<col[rev(i)]) c[place[i].X][place[i].Y]='-';
        else c[place[i].X][place[i].Y]='|';
    }
}

int main()
{
    ifstream cin("in");
    ofstream cout("out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>m;
        cnt=0;
        vec.clear();
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                cin>>c[i][j];
                if(lazer(i,j))
                    place[vec.size()]=pii(i,j),vec.push_back(pii(i,j));
                if(c[i][j]=='.')
                    f[cnt].clear(),a[i][j]=cnt++;
            }
        N=vec.size();
        for(int i=0;i<2*N;i++)
            G[i].clear(),G1[i].clear();
        for(int i=0;i<vec.size();i++)
        {
            for(int jahat=0;jahat<2;jahat++){
                des=false;
                tmpvec.clear();
                memset(mark,false,sizeof mark);
                dfs(vec[i].X,vec[i].Y,jahat);
                dfs(vec[i].X,vec[i].Y,2+jahat);
                if(!des)
                {
                    for(int j=0;j<tmpvec.size();j++)
                        f[a[tmpvec[j].X][tmpvec[j].Y]].push_back((jahat==0?i:rev(i)));
                }
                else add_edge((jahat==0?i:rev(i)),(jahat==1?i:rev(i)));
            }
        }

        pos=true;
        for(int i=0;i<cnt;i++)
        {
            if(f[i].size()==0) {pos=false;break;}
            if(f[i].size()==1) f[i].push_back(f[i][0]);
            add_edge(rev(f[i][0]),f[i][1]);
            add_edge(rev(f[i][1]),f[i][0]);
        }
        twoSAT();
        cout<<"Case #"<<q<<": ";
        if(!pos) {cout<<"IMPOSSIBLE\n";continue;}
        cout<<"POSSIBLE\n";
        for(int i=0;i<n;i++,cout<<endl)
            for(int j=0;j<m;j++)
                cout<<c[i][j];
    }
}
