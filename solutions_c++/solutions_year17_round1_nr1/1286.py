#include<bits/stdc++.h>
using namespace std;
char a[30][30];
int main(){
    ios_base::sync_with_stdio(0);
    int tc,cc,r,c,i,j;
    char ch;
    cin>>tc;
    for(cc=1;cc<=tc;++cc){
        cin>>r>>c;
        for(i=0;i<r;++i)cin>>a[i];
        for(i=0;i<r;++i){
            ch=-1;
            for(j=0;j<c;++j){
                if(a[i][j]=='?'){
                    if(ch!=-1){
                        a[i][j]=ch;
                    }
                }
                else ch=a[i][j];
            }
        }
        for(i=0;i<r;++i){
            ch=-1;
            for(j=c-1;j>-1;--j){
                if(a[i][j]=='?'){
                    if(ch!=-1){
                        a[i][j]=ch;
                    }
                }
                else ch=a[i][j];
            }
        }
        for(i=0;i<c;++i){
            ch=-1;
            for(j=0;j<r;++j){
                if(a[j][i]=='?'){
                    if(ch!=-1){
                        a[j][i]=ch;
                    }
                }
                else ch=a[j][i];
            }
        }
        for(i=0;i<c;++i){
            ch=-1;
            for(j=r;j>-1;--j){
                if(a[j][i]=='?'){
                    if(ch!=-1){
                        a[j][i]=ch;
                    }
                }
                else ch=a[j][i];
            }
        }
        cout<<"Case #"<<cc<<":\n";
        for(i=0;i<r;++i)cout<<a[i]<<'\n';
    }
    return 0;
}
