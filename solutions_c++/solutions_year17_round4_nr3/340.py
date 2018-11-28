//#define WYTE 133
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define eb(...) emplace_back(__VA_ARGS__)
#define SZ(x) int((x).size())
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define arrayin(a,n) for(int _i=0;_i<n++_i){cin>>a[_i];}
#define arrayin1(a,n) for(int _i=1;_i<=n;++_i){cin>>a[_i];}
#define arrayout(a,n) for(int _i=0;_i<n;++_i){cout<<a[_i]<<" \n"[_i+1==n];}
#define arrayout1(a,n) for(int _i=1;_i<=n;++_i){cout<<a[_i]<<" \n"[_i+1>n];}
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define LLNF 1e18
#define EPS 1e-7
#define MOD 1000000007
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)
#define mod(x) if(x>=MOD)x%=MOD
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int dx[]={-1,1,0,0},dy[]={0,0,-1,1},m1[]={3,2,1,0},m2[]={2,3,0,1};
int r,c,bad,sat,val[2505];
string tb[55];
vector<pair<pii,pii>> sat_eq;

void process_gun_helper(int i,int j,int dir)
{
    int x=i,y=j,init_dir=dir;
    while(1)
    {
        x+=dx[dir];
        y+=dy[dir];
        if(tb[i][j]=='/')
        {
            dir=m1[dir];
        }
        else if(tb[i][j]=='\\')
        {
            dir=m2[dir];
        }
        if(x<0||x>=r||y<0||y>=c||tb[x][y]=='#')break;
        if(tb[x][y]=='-'||tb[x][y]=='|')
        {
            pii p=mp(i*c+j,!(dir>>1));
            sat_eq.eb(p,p);
            break;
        }
    }
}

void process_gun(int i,int j)
{
    process_gun_helper(i,j,0);
    process_gun_helper(i,j,1);
    process_gun_helper(i,j,2);
    process_gun_helper(i,j,3);
}

void process_space_helper(int i,int j,int dir,vii &cons)
{
    int x=i,y=j;
    while(1)
    {
        x+=dx[dir];
        y+=dy[dir];
        if(tb[i][j]=='/')
        {
            dir=m1[dir];
        }
        else if(tb[i][j]=='\\')
        {
            dir=m2[dir];
        }
        if(x<0||x>=r||y<0||y>=c||tb[x][y]=='#')break;
        if(x==i&&y==j)break;
        if(tb[x][y]=='-'||tb[x][y]=='|')
        {
            cons.eb(x*c+y,dir>>1);
            break;
        }
    }
}

void process_space(int i,int j)
{
    vii cons;
    process_space_helper(i,j,0,cons);
    process_space_helper(i,j,1,cons);
    process_space_helper(i,j,2,cons);
    process_space_helper(i,j,3,cons);
    if(cons.size()==0)
    {
        bad=1;
    }
    else if(cons.size()==1)
    {
        sat_eq.eb(cons[0],cons[0]);
    }
    else if(cons.size()==2)
    {
        sat_eq.eb(cons[0],cons[1]);
    }
    else
    {
        cerr<<"cons > 2\n";
    }
}

void run_2sat()
{
    srand(133);
    int i,j;
    for(i=0;i<10000000;i++)
    {
        for(j=0;j<sat_eq.size();j++)
        {
            if(val[sat_eq[j].X.X]!=sat_eq[j].X.Y&&val[sat_eq[j].Y.X]!=sat_eq[j].Y.Y)
            {
                if(rand()%2)
                {
                    val[sat_eq[j].X.X]^=1;
                }
                else
                {
                    val[sat_eq[j].Y.X]^=1;
                }
                break;
            }
        }
        if(j==sat_eq.size())
        {
            sat=1;
            break;
        }
    }
}

int main()
{
    freopen("C-small-attempt2.in","rb",stdin);
    freopen("output2.txt","wb",stdout);
    int t,ii,i,j;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>r>>c;
        for(i=0;i<r;i++)
        {
            cin>>tb[i];
        }
        sat_eq.clear();
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(tb[i][j]=='-'||tb[i][j]=='|')
                {
                    process_gun(i,j);
                }
            }
        }
        bad=0;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(tb[i][j]=='.')
                {
                    process_space(i,j);
                }
            }
        }
        sat=0;
        if(!bad)run_2sat();
        printf("Case #%d: %s\n",ii,sat?"POSSIBLE":"IMPOSSIBLE");
        if(sat)
        {
            for(i=0;i<r;i++)
            {
                for(j=0;j<c;j++)
                {
                    if(tb[i][j]=='-'||tb[i][j]=='|')
                    {
                        printf("%c",val[i*c+j]?'-':'|');
                    }
                    else
                    {
                        printf("%c",tb[i][j]);
                    }
                }
                printf("\n");
            }
        }
    }
}
