#include <bits/stdc++.h>
using namespace std;

vector<char> a[1005];

void solve(int tc){
    printf("Case #%d: ",tc);
    int n,r,o,y,g,b,v;
    scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
    if(n==1){
        if(r) printf("R\n");
        if(o) printf("O\n");
        if(y) printf("Y\n");
        if(g) printf("G\n");
        if(b) printf("B\n");
        if(v) printf("V\n");
        return;
    }
    if(n==b+o && b==o){
        for(int i=0;i<b;i++) printf("BO"); printf("\n");
        return;
    }
    if(n==y+v && y==v){
        for(int i=0;i<y;i++) printf("YV"); printf("\n");
        return;
    }
    if(n==r+g && r==g){
        for(int i=0;i<r;i++) printf("RG"); printf("\n");
        return;
    }
    if(b<=o && o>0){
        printf("IMPOSSIBLE\n"); return;
    }
    if(y<=v && v>0){
        printf("IMPOSSIBLE\n"); return;
    }
    if(r<=g &&g>0){
        printf("IMPOSSIBLE\n"); return;
    }
    b-=o; y-=v; r-=g;
    if(r==max({r,y,b})){
        if(b+y<r) printf("IMPOSSIBLE");
        else{
            for(int i=0;i<r;i++) a[i].push_back('R');
            int t=0;
            if(y>b){
                for(int i=0;i<y;i++){
                    a[t++].push_back('Y');
                    t%=r;
                }
                for(int i=0;i<b;i++){
                    a[t++].push_back('B');
                    t%=r;
                }
            }
            else{
                for(int i=0;i<b;i++){
                    a[t++].push_back('B');
                    t%=r;
                }
                for(int i=0;i<y;i++){
                    a[t++].push_back('Y');
                    t%=r;
                }
            }
        }
    }
    else if(y==max({r,y,b})){
        if(b+r<y) printf("IMPOSSIBLE");
        else{
            for(int i=0;i<y;i++) a[i].push_back('Y');
            int t=0;
            if(r>b){
                for(int i=0;i<r;i++){
                    a[t++].push_back('R');
                    t%=y;
                }
                for(int i=0;i<b;i++){
                    a[t++].push_back('B');
                    t%=y;
                }
            }
            else{
                for(int i=0;i<b;i++){
                    a[t++].push_back('B');
                    t%=y;
                }
                for(int i=0;i<r;i++){
                    a[t++].push_back('R');
                    t%=y;
                }
            }
        }
    }
    else if(b==max({r,y,b})){
        if(r+y<b) printf("IMPOSSIBLE");
        else{
            for(int i=0;i<b;i++) a[i].push_back('B');
            int t=0;
            if(y>r){
                for(int i=0;i<y;i++){
                    a[t++].push_back('Y');
                    t%=b;
                }
                for(int i=0;i<r;i++){
                    a[t++].push_back('R');
                    t%=b;
                }
            }
            else{
                for(int i=0;i<r;i++){
                    a[t++].push_back('R');
                    t%=b;
                }
                for(int i=0;i<y;i++){
                    a[t++].push_back('Y');
                    t%=b;
                }
            }
        }
    }
    for(int i=0;i<max({r,y,b});i++){
        for(char c: a[i]){
            printf("%c",c);
            if(c=='B' && o>0) while(o--) printf("OB");
            if(c=='R' && g>0) while(g--) printf("GR");
            if(c=='Y' && v>0) while(v--) printf("VY");
        }
        a[i].clear();
    }printf("\n");
}

int main()
{
    freopen("B-large.in","r",stdin); //freopen("out.txt","w",stdout);
    int tc; scanf("%d",&tc);
    for(int i=1;i<=tc;i++){
        solve(i);
    }
    return 0;
}
