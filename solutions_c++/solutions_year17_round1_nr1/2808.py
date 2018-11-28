#include<bits/stdc++.h>
using namespace std;

int main()
{
    char a[30][30],c;
    int i,j,k,n,m,test=0,testcase;

    cin>>testcase;

    while(testcase>test++)
    {
        cin>>n>>m;
        //cout<<n<<m<<endl;

        for(i=1;i<=n;i++)for(j=1;j<=m;j++)
        {
            scanf(" %c",&a[i][j]);//cout<<i<<" "<<j<<" "<<a[i][j]<<endl;
            //a[i][j]=c;
        }

        bool tr=false;
        int lastrow;
        for(i=1;i<=n;i++)
        {
            bool row=false;

            for(j=1;j<=m;j++)
            {
                if(a[i][j]!='?')
                {
                    c=a[i][j];
                    row=true;
                    break;
                }
            }
            if(row==false && tr==false)continue;

            if(row==false && tr== true)
            {
                for(j=1;j<=m;j++)a[i][j]=a[lastrow][j];
            }

            if(row==false)continue;

            if(row==true)lastrow=i;

            for(j=1;j<=m;j++)
            {
                if(a[i][j]!='?')c=a[i][j];
                else a[i][j]=c;
            }
            if(tr==false)
            {
                tr=true;
                for(int ii=1;ii<i;ii++)
                {
                    for(j=1;j<=m;j++)a[ii][j]=a[i][j];
                }
            }
        }
        printf("Case #%d:\n",test);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)printf("%c",a[i][j]);
            printf("\n");
        }
    }
    return 0;
}
