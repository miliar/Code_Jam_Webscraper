//__ hr1212 __//

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mi;

#define si(a) scanf("%d",&a)
#define sii(a,b) scanf("%d %d",&a,&b)
#define siii(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define pi(a) printf("%d\n",a)
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define f(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b) for(i=a;i>=b;i--)
#define clr(x,a) memset(x,a,sizeof(x))
#define MAX 1000100
#define MOD 1000000007

int n,m,a[MAX][2];
vector<pii > v;

int cmp(pii p,pii q){
        return p.first<q.first;
}

int main(){
    int tt,idx,r,k,i,c=0,x=0,y=0,j,t,l,z,x1=0,y1=0,prevs,prevp;
    ll ans=0;string p;
    double mint,tx,temp;
    si(t);
   f(tt,1,t+1){
        double time=0.0,maxtx=0;
        v.clear();
        sii(m,n);
        f(i,0,n){
            sii(x,y);
            v.pb(mp(x,y));
        }
        sort(all(v),cmp);
        y=0;tx=0;
        f(i,0,n){
            f(j,i+1,n){
                if((v[i].second-v[j].second)!=0){
                tx=(double)(v[j].first-v[i].first)/(v[i].second-v[j].second);
                if(tx>maxtx){
                    maxtx=tx;
                    x=i;y=j;
                }
                }
            }
        }

        if(maxtx!=0){
            if((v[y].first+maxtx*v[y].second)<m)
                time=maxtx+(double)(m-(v[y].first+maxtx*v[y].second))/v[y].second;
            else
                time=(double)(m-v[x].first)/v[x].second;
        }
        else
            time=(double)(m-v[0].first)/v[0].second;
        printf("Case #%d: %lf\n",tt,((double)m/time));
    }

    return 0;
}
