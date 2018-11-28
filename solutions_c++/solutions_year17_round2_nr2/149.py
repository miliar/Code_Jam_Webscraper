#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
//#pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
using namespace __gnu_pbds;
typedef pair<int,int> par;
char ans[1005];
int r,o,y,g,b,v,n;
int rr,oo,yy,gg,bb,vv,nn;
bool calc(){
    for(int i=0;i<n;i++)
        ans[i]='_';
    ans[n]=0;
    char A='R',B='Y',C='B';
    int X=r,Y=y,Z=b;
    if(X<Y)swap(X,Y),swap(A,B);
    if(Y<Z)swap(Y,Z),swap(B,C);
    if(X<Y)swap(X,Y),swap(A,B);
    if(X*2>n)return 0;
    for(int i=0;i<X;i++)
        ans[i*2]=A;
    for(int i=n-1;i>=0;i--){
        if(ans[i]!='_')continue;
        if(Y==0)swap(Y,Z),swap(B,C);
        ans[i]=B;Y--;
        swap(Y,Z),swap(B,C);
        }
    if(ans[0]==ans[n-1]){
        return 0;
        }
    for(int i=1;i<n;i++)
        if(ans[i]==ans[i-1])return 0;
    return 1;
    }
bool cal(){
    if(n==3)
        if(o||g||v)return 0;
    r-=g;
    y-=v;
    b-=o;
    n-=(g+v+o)*2;
    if(r<0||y<0||b<0)return 0;
    if(g&&!r)return 0;
    if(v&&!y)return 0;
    if(o&&!b)return 0;
    return 1;
    }
int main(){
    int t,T=0;
    scanf("%d",&t);
    while(t--){T++;
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        n=r+o+y+g+b+v;
        rr=r;oo=o;yy=y;gg=g;bb=b;vv=v;
        nn=n;
        if(!o&&!y&&!b&&!v){
            printf("Case #%d: ",T);
            if(r!=g)
                printf("IMPOSSIBLE\n");
            else{
                for(int i=0;i<r;i++)
                    printf("RG");
                puts("");
                }
            continue;
            }
        if(!o&&!r&&!b&&!g){
            printf("Case #%d: ",T);
            if(y!=v)
                printf("IMPOSSIBLE\n");
            else{
                for(int i=0;i<y;i++)
                    printf("YV");
                puts("");
                }
            continue;
            }
        if(!y&&!r&&!v&&!g){
            printf("Case #%d: ",T);
            if(o!=b)
                printf("IMPOSSIBLE\n");
            else{
                for(int i=0;i<b;i++)
                    printf("BO");
                puts("");
                }
            continue;
            }
        if(!cal()){
            printf("Case #%d: IMPOSSIBLE\n",T);
            }
        else{
            if(!calc()){
                printf("Case #%d: IMPOSSIBLE\n",T);
                }
            else{
                string s;
                int A=0,B=0,C=0;
                for(int i=0;i<n;i++){
                    s+=ans[i];
                    if(ans[i]=='R'){
                        for(int j=0;j<g;j++)
                            s+="GR";
                        g=0;A++;
                        }
                    if(ans[i]=='Y'){
                        for(int j=0;j<v;j++)
                            s+="VY";
                        v=0;B++;
                        }
                    if(ans[i]=='B'){
                        for(int j=0;j<o;j++)
                            s+="OB";
                        o=0;C++;
                        }
                    }
                if(A!=rr||B!=yy||C!=bb){
                    //printf("QQ %d %d %d %d %d %d\n",A,rr,B,yy,C,bb);
                    }
                if(s.length()!=nn)puts("QQQQQQQQQQQQQQQQQQQQQQQQ");
                if(g||v||o)puts("~~~~~~~~~~~~~~~~~~~~~~OAOAOAO~~~~~~~~~~~~~");
                printf("Case #%d: %s\n",T,s.c_str());
                }
            }
        }
    return 0;
    }
