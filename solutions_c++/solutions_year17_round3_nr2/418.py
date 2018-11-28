#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define CLR(x,y) memset(x,y,sizeof(x))
using namespace std;
#define fr(i,x,y) for(int i=x;i<=y;i++)
typedef long long ll;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
int  n,m;
struct node{
    int x,y;
    bool operator<(const node&oth )const{
        return x<oth.x;
    }
}a[105],b[105];
int d1[1005],d2[1005],c[1005];
vector<int > aa,bb;
void doit(){
    aa.clear();
    bb.clear();
    int t1=0,t2=0;
    scanf("%d%d",&n,&m);
    fr(i,1,n){
        scanf("%d%d",&a[i].x,&a[i].y);
        t1+=a[i].y-a[i].x;
    }
    fr(i,1,m){
        scanf("%d%d",&b[i].x,&b[i].y);
        t2+=b[i].y-b[i].x;
    }

    t1=720-t1;
    t2=720-t2;


    sort(a+1,a+1+n);
    sort(b+1,b+1+m);
    int i=1,j=1,o=1;
    while (i<=n&&j<=m){
        if (a[i].x<b[j].x)
        {
              c[o]=1;d1[o]=a[i].x;d2[o]=a[i].y;o++;
               i++;
        }
        else {c[o]=2;d1[o]=b[j].x;d2[o]=b[j].y;o++;
                j++;
        }

    }

    while(i<=n){
        c[o]=1;d1[o]=a[i].x;d2[o]=a[i].y;o++;i++;
    }
    while(j<=m){
        c[o]=2;d1[o]=b[j].x;d2[o]=b[j].y;o++;j++;
    }
    c[o]=c[1];d1[o]=d1[1]+1440;

    int an=0;
    //fr(i,1,o)printf("~~~~~~~~%d %d %d\n",c[i],d1[i],d2[i]);
    fr(i,1,o-1)
    if (c[i]!=c[i+1]) an+=1;else {
        an += 2;
        if (c[i]==1) aa.pb(d1[i+1]-d2[i]);
        else bb.pb(d1[i+1]-d2[i]);
    }

    //printf("%d %d %d\n",an,aa.size(),bb.size());
    sort(aa.begin(),aa.end());
    int sz=aa.size();
    //fr(i,0,sz-1)printf("!!!!!!!!! %d %d\n",i,aa[i]);
    fr(i,0,sz-1)
    if (t1>=aa[i]){t1-=aa[i];an-=2;}


    sort(bb.begin(),bb.end());
    sz=bb.size();
    //fr(i,0,sz-1)printf("@@@@@@@@@ %d %d\n",i,bb[i]);
    fr(i,0,sz-1)
        if (t2>=bb[i]){t2-=bb[i];an-=2;}

    printf("%d\n",an);
}
int main() {
   freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);



    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {
        printf("Case #%d: ",++i);
        doit();

    }
}