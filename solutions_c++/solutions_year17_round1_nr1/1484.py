#include<bits/stdc++.h>

using namespace std;

#define li long int
#define ii pair<li,li>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define vi vector<li>
#define vii vector<ii>
#define INF 99999
#define MAXN 100005
#define sz size()
#define ins insert

template <class T>
void read(T &a)
{
    static char c;
    static int fh;
    while (((c = getchar()) < '0' || c > '9') && c != '-');
    if (c == '-') fh = -1, a = 0;
    else fh = 1, a = c - '0';
    while ((c = getchar()) <= '9' && c >= '0') a = (a << 3) + (a << 1) + c - '0';
    a = a * fh;
}
template <class T>
void write(T a)
{
    if (a == 0) putchar('0');
    else
    {
        if (a < 0) putchar('-'), a = -a;
        static char c[30];
        static int c0;
        c0 = 0;
        while (a) c[++c0] = a % 10 + '0', a /= 10;
        while (c0) putchar(c[c0--]);
    }
}



int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    li testcases; read(testcases);
    for(li testcase=1;testcase<=testcases;testcase++)
    {
        string s[26];
        int i,j,k,r,c;
        cin>>r>>c;

        for(i=0;i<r;i++) cin>>s[i];

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(s[i][j]!='?')
                {
                    k=j;
                    while(k+1<c && s[i][k+1]=='?') { s[i][k+1]=s[i][k]; k++; }

                    k=j;
                    while(k-1>=0 && s[i][k-1]=='?') { s[i][k-1]=s[i][k]; k--; }
                }
            }
        }

        for(i=0;i<r;i++)
        {
            if(s[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) s[i][j]=s[i-1][j];
                }
                else if (i+1<r)
                {
                    for(j=0;j<c;j++) s[i][j]=s[i+1][j];
                }
            }
        }

        for(i=r-1;i>=0;i--)
        {
            if(s[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) s[i][j]=s[i-1][j];
                }
                if (i+1<r)
                {
                    for(j=0;j<c;j++) s[i][j]=s[i+1][j];
                }
            }
        }

        cout<<"Case #"<<testcase<<":"<<endl;

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++) cout<<s[i][j];
            cout<<endl;
        }
    }
    return 0;
}
