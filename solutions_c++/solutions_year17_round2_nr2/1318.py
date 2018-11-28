#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int R,O,Y,G,B,V,n;
bool ok1(){
    int ma=R;
    if(ma<O)ma=O;
    if(ma<Y)ma=Y;
    if(ma<G)ma=G;
    if(ma<B)ma=B;
    if(ma<V)ma=V;
    //printf("%d %d\n",ma,n);
    return ma+ma>n;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
//    freopen("A-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d%d%d%d%d%d",&n,&R,&O,&Y,&G,&B,&V);
        printf("Case #%d: ",ca);
        if(ok1()){
            puts("IMPOSSIBLE");
        }
        else if(O+Y+B+V==0){
            if(R==G){
                for(int i=0;i<G;++i)printf("RG");
                puts("");
            }
            else puts("IMPOSSIBLE");
        }
        else if(R+O+G+B==0){
            if(Y==V){
                for(int i=0;i<V;++i)printf("YV");
                puts("");
            }
            else puts("IMPOSSIBLE");
        }
        else if(R+Y+G+V==0){//cout<<1111<<endl;
            if(O==B){
                for(int i=0;i<O;++i)printf("BO");
                puts("");
            }
            else puts("IMPOSSIBLE");
        }
        else if((O&&O>=B)||(G&&G>=R)||(V&&V>=Y))puts("IMPOSSIBLE");
        else{
            R-=G;
            Y-=V;
            B-=O;
            n=R+Y+B;
            int f=0,ma=R;
            if(Y>ma)f=1,ma=Y;
            if(B>ma)f=2,ma=B;
            if(ma+ma>n)puts("IMPOSSIBLE");
            else{
                string ans="";
                if(f==0){
                    if(R==1)for(int i=0;i<G;++i)ans+="RG";
                    --R;
                    ans+="R";
                }
                else if(f==1){
                    if(Y==1)for(int i=0;i<V;++i)ans+="YV";
                    --Y;
                    ans+="Y";
                }
                else{
                    if(B==1)for(int i=0;i<O;++i)ans+="BO";
                    --B;
                    ans+="B";
                }
                while(R+Y+B){
                    if(f==0){
                        if(Y>B){
                            if(Y==1)for(int i=0;i<V;++i)ans+="YV";
                            --Y;
                            f=1;
                            ans+="Y";
                        }
                        else{
                            if(B==1)for(int i=0;i<O;++i)ans+="BO";
                            --B;
                            f=2;
                            ans+="B";
                        }
                    }
                    else if(f==1){
                        if(R>B){
                            if(R==1)for(int i=0;i<G;++i)ans+="RG";
                            --R;
                            f=0;
                            ans+="R";
                        }
                        else{
                            if(B==1)for(int i=0;i<O;++i)ans+="BO";
                            --B;
                            f=2;
                            ans+="B";
                        }
                    }
                    else{
                        if(R>Y){
                            if(R==1)for(int i=0;i<G;++i)ans+="RG";
                            --R;
                            f=0;
                            ans+="R";
                        }
                        else{
                            if(Y==1)for(int i=0;i<V;++i)ans+="YV";
                            --Y;
                            f=1;
                            ans+="Y";
                        }
                    }
                }
                n=ans.length();
                if(n>1&&ans[0]==ans[n-1]){
                    --n;
                    do{
                        --n;
                        swap(ans[n],ans[n+1]);
                    }while(ans[n-1]==ans[n]||ans[n]==ans[n+1]);
                }
                cout<<ans;
                puts("");
            }
        }
    }
    return 0;
}
