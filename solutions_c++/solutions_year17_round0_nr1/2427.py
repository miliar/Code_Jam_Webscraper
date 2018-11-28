#include<stdio.h>

char inp[1011];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti,i,n,len,cnt,j;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%s",inp);
        scanf ("%d",&n);
        for(i=0;inp[i];++i);
        len = i;
        cnt=0;
        for (i=0;i<len-n+1;++i)
        {
            if (inp[i]=='-')
            {
                for (j=0;j<n;++j)
                {
                    if (inp[i+j]=='-')inp[i+j]='+';
                    else inp[i+j]='-';
                }
                cnt++;
            }
        }
        for (i=len-n;i<len;++i)
            if (inp[i]=='-')break;
        if (i == len)printf ("Case #%d: %d\n",ti+1,cnt);
        else printf ("Case #%d: IMPOSSIBLE\n",ti+1);
        //printf ("***%s\n",inp);
    }
    return 0;
}
