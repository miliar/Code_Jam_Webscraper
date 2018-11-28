#include<bits/stdc++.h>
using namespace std;
const int N=30;
int t,r,c,T,i,j,k,idx;
char a[N][N];
bool define_row;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&r,&c);
        for(i=0;i<r;i++) scanf(" %s",a[i]);

        printf("Case #%d:\n",++T);

        for(i=0;i<r;i++)
        {
            define_row=false;
            if(count(a[i],a[i]+c,'?')==c) continue;
            if(count(a[i],a[i]+c,'?')) define_row=true;
            if(define_row)
            {
                for(j=0;j<c;j++)
                {
                    if(a[i][j]=='?') continue;
                    for(k=j-1;k>=0;k--)
                        if(a[i][k]=='?') a[i][k]=a[i][j];
                }
                for(j=c-1;j>=0 and a[i][j]=='?';j--) ;
                for(k=j+1;k<c;k++) a[i][k]=a[i][j];
            }

            for(j=i-1;j>=0;j--)
            {
                if(count(a[j],a[j]+c,'?'))
                    for(k=0;k<c;k++) a[j][k]=a[i][k];
                else break;
            }
            for(j=i+1;j<r;j++)
            {
                if(count(a[j],a[j]+c,'?')==c)
                    for(k=0;k<c;k++) a[j][k]=a[i][k];
                else break;
            }
        }

        for(i=0;i<r;i++) printf("%s\n",a[i]);
    }
}
