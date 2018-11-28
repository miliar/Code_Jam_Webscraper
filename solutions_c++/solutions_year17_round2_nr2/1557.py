#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,n,r,o,y,g,b,v,p;
    int k=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        if(r>n/2||y>n/2||b>n/2)
        {
            printf("Case #%d: IMPOSSIBLE\n",k);
            k++;
        }
        else
        {
            if(r+y<b||y+b<r||b+r<y)
            {
                printf("Case #%d: IMPOSSIBLE\n",k);
                k++;
            }
            else
            {
                char a[n];
                set<char> s;
                s.insert('R');
                s.insert('B');
                s.insert('Y');
                char c;
                int p1;
                for(i=0;i<n;i++)
                    a[i]='K';
                if(r>=b&&r>=y)
                {
                    c='R';
                    p=r;
                }
                else if(b>=r&&b>=y)
                {
                    p=b;
                    c='B';
                }
                else
                {
                    p=y;
                    c='Y';
                }
                s.erase(c);
                for(i=0;i<n&&p--;i+=2)
                {
                    a[i]=c;
                }
                i--;
                if(i>n-1)
                    i=1;
                if(c=='R')
                {
                    if(b>y)
                    {
                        p=b;
                        c='B';
                    }
                    else
                    {
                        p=y;
                        c='Y';
                    }
                }
                else if(c=='B')
                {
                    if(r>y)
                    {
                        p=r;
                        c='R';
                    }
                    else
                    {
                        p=y;
                        c='Y';
                    }
                }
                else
                {
                    if(b>r)
                    {
                        p=b;
                        c='B';
                    }
                    else
                    {
                        p=r;
                        c='R';
                    }
                }
                s.erase(c);
                for(i;p--;i+=2)
                {
                    if(i>n-1)
                        i=1;
                    a[i]=c;
                }
                c=*(s.begin());
                for(i=0;i<n;i++)
                {
                    if(a[i]=='K')
                    {
                        a[i]=c;
                    }
                }
                printf("Case #%d: ",k);
                k++;
                for(i=0;i<n;i++)
                {
                    printf("%c",a[i]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}

