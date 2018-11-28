#include<bits/stdc++.h>
using namespace std;


int save[33][3][3][11];
string str;

int rec(int pos,int sm,int srt,int pre)
{
    if(pos==str.size()) return 1;
    int &ret=save[pos][sm][srt][pre];
    if(ret!=-1) return ret;

    int i;
    ret=0;
    if(srt)
    {
        if(sm)
        {
            for(i=1; i<=9; i++) ret|=rec(pos+1,sm,0,i);
        }
        else
        {
            for(i=1; i<str[pos]-48; i++) ret|=rec(pos+1,1,0,i);
            ret|=rec(pos+1,0,0,str[pos]-48);
        }
        ret|=rec(pos+1,1,1,0);
    }
    else
    {
        if(sm)
        {
            for(i=pre; i<=9; i++) ret|=rec(pos+1,sm,0,i);
        }
        else
        {
            for(i=pre; i<str[pos]-48; i++) ret|=rec(pos+1,1,0,i);
            if(str[pos]-48>=pre) ret|=rec(pos+1,0,0,str[pos]-48);
        }
    }
    return ret;
}

void path(int pos,int sm,int srt,int pre)
{
    if(pos==str.size()) return ;
    int i;
    if(srt)
    {
        if(sm)
        {
            for(i=9; i>=1; i--)
            {
                if(rec(pos+1,sm,0,i))
                {
                    printf("%d",i);
                    path(pos+1,sm,0,i);
                    return;
                }
            }
        }
        else
        {
            if(rec(pos+1,0,0,str[pos]-48))
            {
                printf("%d",str[pos]-48);
                path(pos+1,0,0,str[pos]-48);
                return;
            }
            for(i=str[pos]-48-1; i>=1; i--)
            {
                if(rec(pos+1,1,0,i))
                {
                    printf("%d",i);
                    path(pos+1,1,0,i);
                    return;
                }
            }
        }
        if(rec(pos+1,1,1,0))
        {
            path(pos+1,1,1,0);
            return;
        }
    }
    else
    {
        if(sm)
        {
            for(i=9; i>=pre; i--)
            {
                if(rec(pos+1,sm,0,i))
                {
                    printf("%d",i);
                    path(pos+1,sm,0,i);
                    return;
                }
            }
        }
        else
        {
            if(str[pos]-48>=pre)
            {
                if(rec(pos+1,0,0,str[pos]-48))
                {
                    printf("%d",str[pos]-48);
                    path(pos+1,0,0,str[pos]-48);
                    return;
                }
            }
            for(i=str[pos]-48-1; i>=pre; i--)
            {
                if(rec(pos+1,1,0,i))
                {
                    printf("%d",i);
                    path(pos+1,1,0,i);
                    return;
                }
            }
        }
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.in", "w", stdout);

    int t;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        cin >> str;
        memset(save,-1,sizeof save);
        rec(0,0,1,0);
        printf("Case #%d: ",ca);
        path(0,0,1,0);
        printf("\n");

    }

}
