#include <bits/stdc++.h>
using namespace std;
struct show
{
    char simb;
    int x,y;
};
show shows[10005];
char znak[105][105];
char word[105][105];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        int n,m;
        cin>>n>>m;
        for (int i1=1;i1<=n;i1++)
            for (int j1=1;j1<=n;j1++)
            {
                znak[i1][j1]='a';
                word[i1][j1]='a';
            }
        if (n==1)
        {
            for (int j=1;j<=m;j++)
                cin>>shows[j].simb>>shows[j].x>>shows[j].y;
            cout<<"Case #"<<i<<": 2 ";
            if (m==0 || shows[1].simb!='o')
            {
                cout<<1<<'\n';
                cout<<"o 1 1\n";
            }
            else
                cout<<0<<'\n';
        }
        else
        {
            bool fl=false;
            int st=1;
            for (int j=1;j<=m;j++)
            {
                cin>>shows[j].simb>>shows[j].x>>shows[j].y;
                znak[shows[j].x][shows[j].y]=shows[j].simb;
                word[shows[j].x][shows[j].y]=shows[j].simb;
            }
            for (int j=1;j<=n;j++)
            {
                if (znak[1][j]=='a')
                    word[1][j]='+';
                if (znak[1][j]=='x' || znak[1][j]=='o')
                {
                    word[1][j]='o';
                    fl=true;
                    st=j;
                }
            }
            if (!fl) word[1][1]='o';
            for (int j=2;j<n;j++)
                word[n][j]='+';
            int kol=0;
            for (int j=n;j>1;j--)
                if (j!=st)
                {
                    word[j][j]='x';
                    kol++;
                }
            if (kol!=n-1) word[st][1]='x';
            cout<<"Case #"<<i<<": "<<3*n-2<<' ';
            int ans=0;
            for (int i1=1;i1<=n;i1++)
                for (int j1=1;j1<=n;j1++)
                    if (word[i1][j1]!=znak[i1][j1]) ans++;
            cout<<ans<<'\n';
            for (int i1=1;i1<=n;i1++)
                for (int j1=1;j1<=n;j1++)
                    if (word[i1][j1]!=znak[i1][j1])
                        cout<<word[i1][j1]<<' '<<i1<<' '<<j1<<'\n';
        }
    }
    return 0;
}
