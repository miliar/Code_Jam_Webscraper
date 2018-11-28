#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int>>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define MOD 1000000007LL
#define ld long double
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(; c<'0'||c>'9'; c=getchar())if(c=='-')sign=-1;
    for(num=0; c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

char S[1003];
int A[56];
char col[23]="AROYGBV";

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        int n=getnum();
        S[n+1]=0;


        for(int i=1;i<=6;i++)A[i]=getnum();

        int r=A[1]+A[2]+A[6];
        int y=A[2]+A[3]+A[4];
        int b=A[4]+A[5]+A[6];

        printf("Case #%d: ",cases);

        if(A[2]+A[4]+A[6]==0)
        {
            if(A[1]*2>n||A[3]*2>n||A[5]*2>n)puts("IMPOSSIBLE");
            else
            {
                int a=1,b=3,c=5;
                if(A[1]>=max(A[3],A[5]))
                {
                    a=1;
                    if(A[3]>=A[5])b=3,c=5;
                    else b=5,c=3;
                }
                else if(A[3]>=max(A[1],A[5]))
                {
                    a=3;
                    if(A[1]>=A[5])b=1,c=5;
                    else b=5,c=1;
                }
                else if(A[5]>=max(A[1],A[3]))
                {
                    a=5;
                    if(A[1]>=A[3])b=1,c=3;
                    else b=3,c=1;
                }

                for(int i=1;i<=n;i++)
                {
                    if(A[a]>=max(A[b],A[c]))
                    {
                        if(S[i-1]!=col[a])S[i]=col[a],A[a]--;
                        else if(A[b]>=A[c])S[i]=col[b],A[b]--;
                        else S[i]=col[c],A[c]--;
                    }
                    else if(A[b]>=max(A[a],A[c]))
                    {
                        if(S[i-1]!=col[b])S[i]=col[b],A[b]--;
                        else if(A[a]>=A[c])S[i]=col[a],A[a]--;
                        else S[i]=col[c],A[c]--;
                    }
                    else if(A[c]>=max(A[a],A[b]))
                    {
                        if(S[i-1]!=col[c])S[i]=col[c],A[c]--;
                        else if(A[a]>=A[b])S[i]=col[a],A[a]--;
                        else S[i]=col[b],A[b]--;
                    }
                }
                puts(S+1);
            }
        }
        else if(A[1]+A[4]==n)
        {
            if(A[1]!=A[4])puts("IMPOSSIBLE");
            else
            {
                for(int i=1;i<=n;i++)
                {
                    if(i%2)S[i]='R';
                    else S[i]='G';
                }
                puts(S+1);
            }
        }
        else if(A[5]+A[2]==n)
        {
            if(A[5]!=A[2])puts("IMPOSSIBLE");
            else
            {
                for(int i=1;i<=n;i++)
                {
                    if(i%2)S[i]='B';
                    else S[i]='O';
                }
                puts(S+1);
            }
        }
        else if(A[3]+A[6]==n)
        {
            if(A[3]!=A[6])puts("IMPOSSIBLE");
            else
            {
                for(int i=1;i<=n;i++)
                {
                    if(i%2)S[i]='Y';
                    else S[i]='V';
                }
                puts(S+1);
            }
        }
        else if(r*2>n||b*2>n||y*2>n)puts("IMPOSSIBLE");
        else
        {
            if(A[1]<=A[4]&&A[4]>0)puts("IMPOSSIBLE");
            else if(A[5]<=A[2]&&A[2]>0)puts("IMPOSSIBLE");
            else if(A[3]<=A[6]&&A[6]>0)puts("IMPOSSIBLE");
            else
            {
                A[1]-=A[4];
                A[3]-=A[6];
                A[5]-=A[2];

                int m=A[1]+A[3]+A[5];

                int a=1,b=3,c=5;
                if(A[1]>=max(A[3],A[5]))
                {
                    a=1;
                    if(A[3]>=A[5])b=3,c=5;
                    else b=5,c=3;
                }
                else if(A[3]>=max(A[1],A[5]))
                {
                    a=3;
                    if(A[1]>=A[5])b=1,c=5;
                    else b=5,c=1;
                }
                else if(A[5]>=max(A[1],A[3]))
                {
                    a=5;
                    if(A[1]>=A[3])b=1,c=3;
                    else b=3,c=1;
                }

                for(int i=1;i<=n;i++)
                {
                    if(A[a]>=max(A[b],A[c]))
                    {
                        if(S[i-1]!=col[a])S[i]=col[a],A[a]--;
                        else if(A[b]>=A[c])S[i]=col[b],A[b]--;
                        else S[i]=col[c],A[c]--;
                    }
                    else if(A[b]>=max(A[a],A[c]))
                    {
                        if(S[i-1]!=col[b])S[i]=col[b],A[b]--;
                        else if(A[a]>=A[c])S[i]=col[a],A[a]--;
                        else S[i]=col[c],A[c]--;
                    }
                    else if(A[c]>=max(A[a],A[b]))
                    {
                        if(S[i-1]!=col[c])S[i]=col[c],A[c]--;
                        else if(A[a]>=A[b])S[i]=col[a],A[a]--;
                        else S[i]=col[b],A[b]--;
                    }
                }
                int fr=0,fy=0,fb=0;
                for(int i=1;i<=m;i++)
                {
                    if(A[2]&&S[i]=='B'&&fb==0)
                    {
                        fb=1;
                        for(int j=1;j<=A[2];j++)putchar('B'),putchar('O');
                    }
                    if(A[4]&&S[i]=='R'&&fr==0)
                    {
                        fr=1;
                        for(int j=1;j<=A[4];j++)putchar('R'),putchar('G');
                    }
                    if(A[6]&&S[i]=='Y'&&fy==0)
                    {
                        fy=1;
                        for(int j=1;j<=A[6];j++)putchar('Y'),putchar('V');
                    }
                    putchar(S[i]);
                }
                puts("");
            }
        }
    }
}
