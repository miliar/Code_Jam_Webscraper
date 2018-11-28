#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    int n,p;
    for(int t=1;t<=tc;t++){
        scanf("%d%d",&n,&p);
        int x;
        int ans=0;
        if(p==2){
            int a=0,b=0;
            for(int i=0;i<n;i++){
                scanf("%d",&x);
                if(x%2==1)b++;
                else a++;
            }
            ans+=a;
            ans+=(b+1)/2;
        }
        else if(p==3){
            int a=0,b=0,c=0;
            for(int i=0;i<n;i++){
                scanf("%d",&x);
                if(x%3==0)a++;
                else if(x%3==1)b++;
                else c++;
            }
            ans+=a;
            if(b<c)swap(b,c);
            ans+=c;
            ans+=(b-c+2)/3;
        }
        else{
            int a=0,b=0,c=0,d=0;
            for(int i=0;i<n;i++){
                scanf("%d",&x);
                if(x%4==0)a++;
                else if(x%4==1)b++;
                else if(x%4==2)c++;
                else d++;
            }
            ans+=a;
            ans+=c/2;
            c-=(c/2)*2;
            if(b<d)swap(b,d);
            ans+=d;
            b-=d;
            ans+=(b/4);
            b-=(b/4)*4;
            if(c>0 || b>0)ans++;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
