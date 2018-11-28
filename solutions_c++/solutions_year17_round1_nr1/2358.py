// 2017/04/15 GCJ 2017 Round1 A
// A- alphabet cake
#include <iostream>
#include <cstdio>
using namespace std;

int cases, R, C;
bool head[30];
char ch[30][30];


void init()
{
    cin>>R>>C;
    for(int i=1;i<=R;++i){
        head[i]=0;
        for(int j=1;j<=C;++j){
            cin>>ch[i][j];
            if(ch[i][j]!='?' && head[i]==0){
                ch[i][0]=ch[i][j];
                head[i]=1;
            }
        }
    }
}

void solve()
{
    for(int i=1;i<=R;++i){
        if(!head[i])
            continue;
        for(int j=1;j<=C;++j){
            if(ch[i][j]=='?')
                ch[i][j]=ch[i][j-1];
        }
    }

    int flag;
    for(int i=1;i<=R;++i)
        if(head[i]){
            flag=i; break;
        }

    for(int j=1;j<=C;++j)
        ch[0][j]=ch[flag][j];

    for(int i=1;i<=R;++i){
        if(!head[i]){
            for(int j=1;j<=C;++j)
                ch[i][j]=ch[i-1][j];
        }
    }
}

void output()
{
    for(int i=1;i<=R;++i){
        for(int j=1;j<=C;++j)
            cout<<ch[i][j];
        cout<<endl;
    }
}

int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    cin>>cases;
    for(int kase=1;kase<=cases;++kase){
        cout<<"Case #"<<kase<<":\n";
        init();
        solve();
        output();
    }
}
