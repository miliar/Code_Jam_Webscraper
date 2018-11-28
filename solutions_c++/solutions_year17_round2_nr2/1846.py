#include <bits/stdc++.h>

using namespace std;


int main()
{

    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2out.in","w",stdout);

    int t;
    cin>>t;

    int cs=0;

    while(cs<t)    {
        int n,r,o,y,g,b,v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        int mx=0;
        if(r>mx)    mx=r;
        if(y>mx)    mx=y;
        if(b>mx)    mx=b;

        if(2*mx>r+y+b)    {
            printf("Case #%d: IMPOSSIBLE\n",++cs);
            continue;
        }
        printf("Case #%d: ",++cs);
        char xx,yy,zz;
        int X,Y,Z;

        if(mx==r)    {
            xx='R';
            yy='Y';
            zz='B';
            X=r;
            Y=y;
            Z=b;
        }
        else if(mx==y)    {
            xx='Y';
            yy='B';
            zz='R';
            X=y;
            Y=b;
            Z=r;
        }
        else if(mx==b)    {
            xx='B';
            yy='Y';
            zz='R';
            X=b;
            Y=y;
            Z=r;
        }

        while(1)    {
            if(X==Y+Z)    break;
            printf("%c%c%c",xx,yy,zz);
            X--;
            Y--;
            Z--;

        }

        for(int i=0;i<Y;i++)    {
            printf("%c%c",xx,yy);
        }
        for(int i=0;i<Z;i++)    {
            printf("%c%c",xx,zz);
        }
        printf("\n");
    }

    return 0;

}
