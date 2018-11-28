#include<stdio.h>

char inp[100];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti,mark,i;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf("%s",inp);
        mark=0;
        if (!inp[1])printf ("Case #%d: %s\n",ti+1,inp);
        else
        {
            for (i=0;inp[i+1];++i)
            {
                if (inp[i]<inp[i+1]) mark=i+1;
                else if (inp[i]>inp[i+1]) break;
            }
            if (!inp[i+1])printf ("Case #%d: %s\n",ti+1,inp);
            else
            {
                inp[mark]--;
                for(i=mark+1;inp[i];++i)inp[i]='9';
                if (inp[0]=='0')
                {
                    printf ("Case #%d: ",ti+1);
                    for (i=1;inp[i];++i)
                        printf ("%c",inp[i]);
                    printf ("\n");
                }
                else
                {
                    printf ("Case #%d: %s\n",ti+1,inp);
                }
            }
        }
    }
    return 0;
}
