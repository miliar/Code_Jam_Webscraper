#include <iostream>
#include <cstdio>

using namespace std;

int T;
char S[25];

int main()
{
    scanf("%d",&T);
    for (int Case=1; Case<=T; Case++)
    {
        scanf("\n%s",S);
        int i=1;
        while (S[i]!='\0' && S[i-1]<=S[i])
        {
            i++;
        }

        if (S[i]=='\0'); //tidy num
        else
        {
            int j=i;
            while (S[j]!='\0')
            {
                S[j]='9';
                j++;
            }
            S[j=i-1]-=1;
            while (j>0 && S[j]<S[j-1])
            {
                S[j]='9';
                S[--j]-=1;
            }

        }

        i=0;
        while (S[i]!='\0' && S[i]=='0')
        {
            i++;
        }

        printf("Case #%d: %s\n",Case,S+i);




    }

    return 0;
}
