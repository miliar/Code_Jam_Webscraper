#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>

#define lo long long
#define fi first
#define se second
#define mp make_pair
#define pb push_back

using namespace std;

lo t,r,c;
char tab[50][50];
int main()
{
    freopen("input1.in","r",stdin);
    freopen("output1.out","w",stdout);

    scanf("%lld",&t);
    for (lo i=1;i<=t;i++)
    {
        scanf("%lld %lld\n",&r,&c);
        for (lo j=0;j<r;j++)
        {
            scanf("\n%s",tab[j]);
        }

        for (lo j=0;j<r;j++)
        {
            for (lo k=0;k<c;k++)
            {
                if (tab[j][k]!='?')
                {
                    //sebar kanan
                    lo st=k-1;
                    while (st>-1 && tab[j][st]=='?')
                    {
                        tab[j][st]=tab[j][k];
                        st--;
                    }
                    //sebar kiri
                    st=k+1;
                    while (st<c && tab[j][st]=='?')
                    {
                        tab[j][st]=tab[j][k];
                        st++;
                    }
                }
            }
        }

        //tutup row kosong
        for (lo j=0;j<r;j++)
        {
            if (tab[j][0]!='?')
            {
                //sebar atas
                lo st=j-1;
                while(st>-1 && tab[st][0]=='?')
                {
                    strcpy(tab[st],tab[j]);
                    st--;
                }
                //sebar bawah
                st=j+1;
                while (st<r && tab[st][0]=='?')
                {
                    strcpy(tab[st],tab[j]);
                    st++;
                }
            }
        }

        printf("Case #%lld:\n",i);
        for (lo j=0;j<r;j++)
        {
            printf("%s\n",tab[j]);
        }
    }

    return 0;
}
