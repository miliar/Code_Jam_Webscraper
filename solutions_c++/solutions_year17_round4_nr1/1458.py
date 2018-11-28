#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("A-large.in","r",stdin)
#define FRO freopen("A-large.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define DB(x) #x"=>",x
#define RAD(x) ((x*PI)/180)
#define NEX(x) ((x)==n-1?0:(x)+1)
#define PRE(x) ((x)==0?n-1:(x)-1)
#define DEG(x) ((x*180)/PI)

#define EPS 1e-6
#define INF 1000000007
#define MOD 1000000007
#define MAXN 1005
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

int cnt[4];
vector < vector <int> >dp2;
vector < vector < vector <int> > >dp3;
vector < vector < vector < vector <int> > > >dp4;

void solve4(int n,int cas) {
    int i,j,k,l,leftOver,temp,g;
    for(i=0;i<4;i++) cnt[i]=0;
    for(i=0;i<n;i++) {
        cin>>g;
        cnt[g%4]++;
    }
    dp4.clear();
    dp4.resize(cnt[0]+1);
    for(i=0;i<=cnt[0];i++) {
        dp4[i].resize(cnt[1]+1);
        for(j=0;j<=cnt[1];j++) {
            dp4[i][j].resize(cnt[2]+1);
            for(k=0;k<=cnt[2];k++)
                dp4[i][j][k].resize(cnt[3]+1);
        }

    }
    for(i=0;i<=cnt[0];i++)
        for(j=0;j<=cnt[1];j++)
            for(k=0;k<=cnt[2];k++)
                for(l=0;l<=cnt[3];l++) {
                    dp4[i][j][k][l]=0;
                    if(i>0) {
                        leftOver=((i-1)*0+j*1+k*2+l*3)%4;
                        temp=dp4[i-1][j][k][l];
                        if(leftOver==0) temp++;
                        dp4[i][j][k][l]=max(temp,dp4[i][j][k][l]);
                    }
                    if(j>0) {
                        leftOver=(i*0+(j-1)*1+k*2+l*3)%4;
                        temp=dp4[i][j-1][k][l];
                        if(leftOver==0) temp++;
                        dp4[i][j][k][l]=max(temp,dp4[i][j][k][l]);
                    }
                    if(k>0) {
                        leftOver=(i*0+j*1+(k-1)*2+l*3)%4;
                        temp=dp4[i][j][k-1][l];
                        if(leftOver==0) temp++;
                        dp4[i][j][k][l]=max(temp,dp4[i][j][k][l]);
                    }
                    if(l>0) {
                        leftOver=(i*0+j*1+k*2+(l-1)*3)%4;
                        temp=dp4[i][j][k][l-1];
                        if(leftOver==0) temp++;
                        dp4[i][j][k][l]=max(temp,dp4[i][j][k][l]);
                    }
                }
    cout<<"Case #"<<cas<<": "<<dp4[cnt[0]][cnt[1]][cnt[2]][cnt[3]]<<endl;
}

void solve3(int n,int cas) {
    int i,j,k,leftOver,temp,g;
    for(i=0;i<3;i++) cnt[i]=0;
    for(i=0;i<n;i++) {
        cin>>g;
        cnt[g%3]++;
    }
    dp3.clear();
    dp3.resize(cnt[0]+1);
    for(i=0;i<=cnt[0];i++) {
        dp3[i].resize(cnt[1]+1);
        for(j=0;j<=cnt[1];j++)
            dp3[i][j].resize(cnt[2]+1);
    }
    for(i=0;i<=cnt[0];i++)
        for(j=0;j<=cnt[1];j++)
            for(k=0;k<=cnt[2];k++) {
                dp3[i][j][k]=0;
                if(i>0) {
                    leftOver=((i-1)*0+j*1+k*2)%3;
                    temp=dp3[i-1][j][k];
                    if(leftOver==0) temp++;
                    dp3[i][j][k]=max(temp,dp3[i][j][k]);
                }
                if(j>0) {
                    leftOver=(i*0+(j-1)*1+k*2)%3;
                    temp=dp3[i][j-1][k];
                    if(leftOver==0) temp++;
                    dp3[i][j][k]=max(temp,dp3[i][j][k]);
                }
                if(k>0) {
                    leftOver=(i*0+j*1+(k-1)*2)%3;
                    temp=dp3[i][j][k-1];
                    if(leftOver==0) temp++;
                    dp3[i][j][k]=max(temp,dp3[i][j][k]);
                }
            }
    cout<<"Case #"<<cas<<": "<<dp3[cnt[0]][cnt[1]][cnt[2]]<<endl;
}

void solve2(int n,int cas) {
    int i,j,leftOver,temp,g;
    for(i=0;i<2;i++) cnt[i]=0;
    for(i=0;i<n;i++) {
        cin>>g;
        cnt[g%2]++;
    }
    dp2.clear();
    dp2.resize(cnt[0]+1);
    for(i=0;i<=cnt[0];i++)
        dp2[i].resize(cnt[1]+1);
    for(i=0;i<=cnt[0];i++)
        for(j=0;j<=cnt[1];j++) {
            dp2[i][j]=0;
            if(i>0) {
                leftOver=((i-1)*0+j*1)%2;
                temp=dp2[i-1][j];
                if(leftOver==0) temp++;
                dp2[i][j]=max(temp,dp2[i][j]);
            }
            if(j>0) {
                leftOver=(i*0+(j-1)*1)%2;
                temp=dp2[i][j-1];
                if(leftOver==0) temp++;
                dp2[i][j]=max(temp,dp2[i][j]);
            }
        }
    cout<<"Case #"<<cas<<": "<<dp2[cnt[0]][cnt[1]]<<endl;
}

void solve(int cas) {
    int n,p;
    cin>>n>>p;
    switch(p) {
        case 2: solve2(n,cas); break;
        case 3: solve3(n,cas); break;
        case 4: solve4(n,cas); break;
        default: assert(false);
    }
}

int main() {
    FRI;
    FRO;
    int T,t=0;
    scanf("%d",&T);
    while(t++<T) solve(t);
    return 0;
}
