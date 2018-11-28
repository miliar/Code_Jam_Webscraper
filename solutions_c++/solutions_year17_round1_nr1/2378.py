#include<bits/stdc++.h>

using namespace std;

///***********SEXY & I KNOW IT******************///
#define li long long int
///***input******// for +ve int
inline li in() {
    li p=0; register char ch=0;
    while(ch<'0' or ch>'9') {ch=getchar();}
    while(ch>='0' and ch<='9') {p=(p<<1)+(p<<3)+ch-'0'; ch=getchar();}
    return p;
}
///***output*****// for +ve int
#define pc(x) putchar(x)
inline void dukya(li n){
        li N = n, rev, count_ = 0;
        rev = N;
        if (N == 0) { pc('0'); pc('\n'); return ;}
        while ((rev % 10) == 0) { count_++; rev /= 10;}
        rev = 0;
        while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}
        while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
        while (count_--) pc('0');
        pc('\n');
    }
///
#define ld long double
#define lega(n) scanf("%lld", &n)
#define dley(n, m) scanf("%lld %lld", &n, &m)
#define dega(n) printf("%lld\n", n)
#define chal(n) for(li i=0;i<n; ++i)
#define FOR(i, n, c) for(i=c; i<n; i++)
#define fpos(n) for(auto pos=n.begin(); pos!=n.end(); ++pos)
#define frng(n) for(auto val : n)
#define ot(n) cout<<n<<"\n"
#define wl(n) while(n--)
#define vs vector<string>
#define vi vector<li>
#define ii pair<li, li>
#define mii map<ii, li>
#define mli map<li, li>
#define met multiset<li>
#define p_b(n) push_back(n)
#define ict int test_case=in(); wl(test_case)
#define INF 1000000009
#define mod 1000000007
#define EPS 0;.000000001
#define lipos(s) s&-s
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL)
///****************************************///

       char grid[30][30], vis[30][30];
       li r, c;
       bool check(li x, li y)
       {
           if(x<0||y<0||x>=r||y>=c)
            return false;
           return true;
       }
       char up(li x, li y)
       {
           if(grid[x][y]!='?')
            return grid[x][y];
           li x1=x-1;
           if(check(x1, y))
            grid[x][y]=up(x1, y);
            return grid[x][y];
       }
       char down(li x, li y)
       {
           if(grid[x][y]!='?')
            return grid[x][y];
           li x1=x+1;
           if(check(x1, y))
            grid[x][y]=down(x1, y);
            return grid[x][y];
       }
       char lef(li x, li y)
       {
           if(grid[x][y]!='?')
            return grid[x][y];
           li y1=y-1;
           if(check(x, y1))
            grid[x][y]=lef(x, y1);
            return grid[x][y];
       }
       char rig(li x, li y)
       {
           if(grid[x][y]!='?')
            return grid[x][y];
           li y1=y+1;
           if(check(x, y1))
            grid[x][y]=rig(x, y1);
            return grid[x][y];
       }
int main()
{
    li test=in();
   for(li tt=1; tt<=test; ++tt)
   {
       cout<<"Case #"<<tt<<": "<<endl;

        r=in(), c=in();
       chal(r)
       {
           for(li j=0; j<c; ++j)
            cin>>grid[i][j];
       }
       chal(r)
       {
           for(li j=0; j<c; ++j)
            {
                if(grid[i][j]=='?')
                {
                    grid[i][j]=up(i, j);
                }
            }
       }
       chal(r)
       {
           for(li j=0; j<c; ++j)
            {
                if(grid[i][j]=='?')
                {
                    grid[i][j]=down(i, j);
                }
            }
       }
       chal(r)
       {
           for(li j=0; j<c; ++j)
            {
                if(grid[i][j]=='?')
                {
                    grid[i][j]=lef(i, j);
                }
            }
       }
       chal(r)
       {
           for(li j=0; j<c; ++j)
            {
                if(grid[i][j]=='?')
                {
                    grid[i][j]=rig(i, j);
                }
            }
       }
       chal(r)
       {
           for(li j=0; j<c; ++j)
            cout<<grid[i][j];
            cout<<endl;
       }

   }
    return 0;
}
