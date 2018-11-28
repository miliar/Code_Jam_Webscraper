#include <bits/stdc++.h>
#define MAXR 30
using namespace std;

inline void in(int &n){scanf("%d",&n);}

int T;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    in(T);
    for(int t=1;t<=T;++t){
        printf("Case #%d: ",t);
        int R,C;
        char m[MAXR][MAXR];
        in(R);in(C);
        for(int i=0;i<R;++i)
            for(int j=0;j<C;++j){
                cin>>m[i][j];
                if(m[i][j]!='?'){
                    int k=i-1;
                    while(k>=0 && m[k][j]=='?'){
                        m[k][j]=m[i][j];
                        --k;
                    }
                }
            }
        for(int i=1;i<R;++i)
            for(int j=0;j<C;++j)
                if(m[i][j]=='?')
                    m[i][j]=m[i-1][j];
        for(int i=0;i<R;++i)
            for(int j=1;j<C;++j)
                if(m[i][j]=='?')
                    m[i][j]=m[i][j-1];
        for(int i=0;i<R;++i)
            for(int j=C-2;j>=0;--j)
                if(m[i][j]=='?')
                    m[i][j]=m[i][j+1];
        printf("\n");
        for(int i=0;i<R;++i){
            for(int j=0;j<C;++j)
                cout<<m[i][j];
            cout<<endl;
        }
    }
}
