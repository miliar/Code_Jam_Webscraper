#include<bits/stdc++.h>

using namespace std;

void solve(int test)
{
    char num[30];
    scanf("%s",num);
    int n = strlen(num);
    for ( int c=n ; c>0 ; c-- )
    {
        bool okay = true;
        for ( int d=0 ; d<c-1 ; d++ )
        {
            //printf("%d %d\n",num[d],num[d+1]);
            if ( num[d] > num[d+1] )    okay = false;
        }
        if ( okay ) break;
        num[c-1] = '9';
        for ( int d= c-2 ; d>=0 ; d-- )
        {
            if ( num[d] == '0' )    num[d] = '9';
            else
            {
                num[d]--;
                break;
            }
        }
    }
    int start;
    if ( num[0] == '0' )   start = 1;
    else    start = 0;
    printf("Case #%d: ",test);
    for ( int c = start ; c<n ; c++ )   printf("%c",num[c]);
    printf("\n");
}

int main()  {
    freopen("B-large.in","r",stdin);
    freopen("B-large-out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for ( int c=1 ; c<=T ; c++ )
    {
        solve(c);
    }
}
