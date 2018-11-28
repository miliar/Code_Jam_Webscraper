#include <bits/stdc++.h>
#define maxn 1010
#define REP(i,x,y) for(int i=x;i<=y;i++)
using namespace std;
int n,r,o,y,g,b,v;
char ans[maxn],ans2[maxn],ans3[maxn];
int main()
{
    freopen("data4.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        memset(ans,0,sizeof(ans));memset(ans2,0,sizeof(ans2));
        memset(ans3,0,sizeof(ans3));
        scanf("%d",&n);
        scanf("%d %d %d %d %d %d",&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",cas++);
        int maxx=0;char c;
        if(r>=y&&r>=b) maxx=r,c='R',r=0;
        else if(y>=r&&y>=b) maxx=y,c='Y',y=0;
        else if(b>=y&&b>=r) maxx=b,c='B',b=0;
        if(maxx>n/2) printf("IMPOSSIBLE\n");
        else {
            REP(i,1,maxx) ans[i]=c;
            int maxx2=0,maxx3=0;char c1,c2;
            if(r==0){
                if(b>y) {
                    maxx2=b;maxx3=y;
                    c1='B';c2='Y';
                }
                else {
                    maxx2=y;maxx3=b;
                    c1='Y';c2='B';
                }
            }
            else if(b==0){
                if(r>y) {
                    maxx2=r;maxx3=y;
                    c1='R';c2='Y';
                }
                else {
                    maxx2=y;maxx3=r;
                    c1='Y';c2='R';
                }
            }
            else if(y==0){
                if(b>r) {
                    maxx2=b;maxx3=r;
                    c1='B';c2='R';
                }
                else {
                    maxx2=r;maxx3=b;
                    c1='R';c2='B';
                }
            }
            ans2[1]=c1;maxx2--;ans2[2]=c;
            int cnt=2;
            REP(i,1,maxx){
                if(ans[i]==ans[i+1]){
                    if(maxx2) ans2[++cnt]=c1,maxx2--;
                    else if(maxx3) ans2[++cnt]=c2,maxx3--;
                }
                ans2[++cnt]=ans[i+1];
            }
            int len2=cnt;
            int cnt2=0;
            REP(i,1,len2){
                if(maxx3) {ans3[++cnt2]=c2;maxx3--;}
                ans3[++cnt2]=ans2[i];
            }
            //cout<<cnt2<<endl;
            REP(i,1,cnt2+1) if(ans3[i]!='\0')putchar(ans3[i]);
            puts("");
        }
    }
}
