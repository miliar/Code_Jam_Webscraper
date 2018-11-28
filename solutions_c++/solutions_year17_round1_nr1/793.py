#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 100005

string s[30];
int r, c;

pii top_left(char ch)
{
    for(int i = 0; i < r; i++)
    {
        for(int j = 0; j < c; j++)
        {
            if(s[i][j] == ch)
                return mp(i,j);
        }
    }
    return mp(0,0);
}

pii bottom_right(char ch)
{
    for(int i = r-1; i >= 0; i--)
    {
        for(int j = c-1; j >= 0; j--)
        {
            if(s[i][j] == ch)
                return mp(i,j);
        }
    }
    return mp(0,0);
}

void fleft(char ch)
{
    pii tl = top_left(ch);
    pii br = bottom_right(ch);

    for(int i = tl.yy; i >= 0; i--)
    {
        for(int j = tl.xx; j <= br.xx; j++)
        {
            if(s[j][i] != ch && s[j][i] != '?')
                return ;
        }
        for(int j = tl.xx; j <= br.xx; j++)
            s[j][i] = ch;
    }
}

void fright(char ch)
{
    pii tl = top_left(ch);
    pii br = bottom_right(ch);

    for(int i = br.yy; i < c; i++)
    {
        for(int j = tl.xx; j <= br.xx; j++)
        {
            if(s[j][i] != ch && s[j][i] != '?')
                return ;
        }
        for(int j = tl.xx; j <= br.xx; j++)
            s[j][i] = ch;
    }
}

void fup(char ch)
{
    pii tl = top_left(ch);
    pii br = bottom_right(ch);

    for(int i = tl.xx; i >= 0; i--)
    {
        for(int j = tl.yy; j <= br.yy; j++)
        {
            if(s[i][j] != ch && s[i][j] != '?')
                return ;
        }
        for(int j = tl.yy; j <= br.yy; j++)
            s[i][j] = ch;
    }
}

void fdown(char ch)
{
    pii tl = top_left(ch);
    pii br = bottom_right(ch);

    for(int i = br.xx; i < r; i++)
    {
        for(int j = tl.yy; j <= br.yy; j++)
        {
            if(s[i][j] != ch && s[i][j] != '?')
                return ;
        }
        for(int j = tl.yy; j <= br.yy; j++)
            s[i][j] = ch;
    }
}

int main()
{
    //READ("A-large.in");
    //WRITE("A-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, i, j;
    set <char> st;
    set <char>::iterator it;

    cin >> cases;

    while(cases--)
    {
        cin >> r >> c;

        st.clear();

        FOR(i,0,r-1)
        {
            cin >> s[i];
            FOR(j,0,c-1) st.insert(s[i][j]);
        }

        for(it = st.begin(); it != st.end(); it++)
            fleft(*it);
        for(it = st.begin(); it != st.end(); it++)
            fup(*it);
        for(it = st.begin(); it != st.end(); it++)
            fright(*it);
        for(it = st.begin(); it != st.end(); it++)
            fdown(*it);

        cout << "Case #" << ++caseno << ":" << NL;

        FOR(i,0,r-1) cout << s[i] << NL;
    }

    return 0;
}


