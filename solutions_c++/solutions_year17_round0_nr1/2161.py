#include <iostream>
#include <cstdio>

using namespace std;

int T, K;
char S[1010];
int vege[2010];

int main()
{
    scanf("%d",&T);
    for (int Case=1; Case<=T; Case++)
    {
        scanf("\n%s %d",S,&K);
        int i=0;
        int db=0;
        int akt=0;
        while (S[i]!='\0')
        {
            if (S[i]=='-' && akt%2==0 || S[i]=='+' && akt%2==1)
            {
                db++; akt++;
                vege[i+K-1]+=1;
            }
            akt-=vege[i];
            vege[i]=0;
            i++;
        }

            //printf("db: %d akt: %d\n",db,akt);
            if (akt==0) printf("Case #%d: %d\n",Case,db);
            else
            {
                printf("Case #%d: IMPOSSIBLE\n",Case);
                while (akt>0)
                {akt-=vege[i];
                vege[i++]=0;
                }

            }
    }

    return 0;
}
