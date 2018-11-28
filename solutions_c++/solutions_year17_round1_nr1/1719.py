#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int c1=0;
    while(t--)
    {
        string str1[40];
        int i,j,var,r,c;
        scanf("%d %d",&r,&c);
        c1++;
       for(i=0;i<r;i++) cin>>str1[i];

       for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(str1[i][j]!='?')
                {
                    var=j;
                    while(var+1<c && str1[i][var+1]=='?') { str1[i][var+1]=str1[i][var]; var++; }

                   var=j;
                    while(var-1>=0 && str1[i][var-1]=='?') { str1[i][var-1]=str1[i][var]; var--; }
                }
            }
        }

       for(i=0;i<r;i++)
        {
            if(str1[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) str1[i][j]=str1[i-1][j];
                }
                else if (i+1<r)
                {
                    for(j=0;j<c;j++) str1[i][j]=str1[i+1][j];
                }
            }
        }

       for(i=r-1;i>=0;i--)
        {
            if(str1[i][0]=='?')
            {
                if(i-1>=0)
                {
                    for(j=0;j<c;j++) str1[i][j]=str1[i-1][j];
                }
                if (i+1<r)
                {
                    for(j=0;j<c;j++) str1[i][j]=str1[i+1][j];
                }
            }
        }
        printf("Case #%d:\n",c1);
       //cout<<"Case #"<<t<<":"<<endl;

       for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            cout<<str1[i][j];
            printf("\n");
        }
    }
    return 0;
}
