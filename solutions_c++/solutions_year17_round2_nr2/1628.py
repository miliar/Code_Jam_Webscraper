#include <bits/stdc++.h>

#define MOD 1000000009

using namespace std;

int main()
{
    freopen("D:/codes/in.txt","r",stdin);
    freopen("D:/codes/out.txt","w",stdout);

    int t,n,i,j,k,m,cnt,ans,r,o,y,g,v,b;
    char a[1001];

     scanf("%d",&t);
     int tc=t;
     while(t--)
     {
        scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
        printf("Case #%d: ",tc-t);
        fill(a,a+1001,0);

        cnt=r+y+b;
        if(r>cnt/2 || y>cnt/2 || b>cnt/2)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        else
        {
            if(y>r && y>b)
            {
                for(i=0;i<n;i+=2)
                {
                    if(y>0)
                    {
                        a[i]='Y';
                        --y;
                    }
                    else if(r>0)
                    {
                        a[i]='R';
                        --r;
                    }
                    else if(b>0)
                    {
                        a[i]='B';
                        --b;
                    }
                }

                for(i=1;i<n;i+=2)
                {
                    if(y>0)
                    {
                        a[i]='Y';
                        --y;
                    }
                    else if(r>0)
                    {
                        a[i]='R';
                        --r;
                    }
                    else if(b>0)
                    {
                        a[i]='B';
                        --b;
                    }
                }

            }
            else
            {

                for(i=0;i<n;i+=2)
                {
                    if(r>0)
                    {
                        a[i]='R';
                        --r;
                    }
                    else if(y>0)
                    {
                        a[i]='Y';
                        --y;
                    }
                    else if(b>0)
                    {
                        a[i]='B';
                        --b;
                    }
                }

                for(i=1;i<n;i+=2)
                {
                    if(r>0)
                    {
                        a[i]='R';
                        --r;
                    }
                    else if(y>0)
                    {
                        a[i]='Y';
                        --y;
                    }
                    else if(b>0)
                    {
                        a[i]='B';
                        --b;
                    }
                }
            }
        }

        printf("%s\n",&a);
        for(i=0;i<n;++i)
        {
            if(a[i]==a[(i+1)%n])
                cout<<"Z\n";
        }


     }

	return 0;

}
