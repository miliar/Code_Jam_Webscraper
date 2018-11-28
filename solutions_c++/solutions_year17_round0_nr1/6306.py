#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

/*
formula as linear algebra

Ax = b

example
A=
1 0
1 1
1 1
0 1

x=
?

b=
1
1
1
0

operation RREF with XOR

Let
A'=
10
01
00
00

x=b'=
1
0
0
0

as same as for loop, flip pan cake if you meet any -
*/

char flip(char a)
{
    if(a=='+')
        return '-';
    return '+';
}

bool solve(char S[], int K,int *ans)
{
    int len = strlen(S);
    for(int i=0; i<len-K+1; i++)
    {
        if(S[i]=='-')
        {
            (*ans)++;
            for(int j=0; j<K; j++)
                S[i+j]=flip(S[i+j]);
        }
    }
    for(int i=0; i<len; i++)
        if(S[i]=='-')
            return false;
    return true;
}
char S[1010];
int main()
{
    int T=0;
    scanf("%d ",&T);
    for(int i=0; i<T; i++)
    {
        int K=0;
        scanf("%s %d",S,&K);
        int ans = 0;
        if(solve(S,K,&ans))
            printf("Case #%d: %d\n",i+1,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",i+1);
    }
    return 0;
}
