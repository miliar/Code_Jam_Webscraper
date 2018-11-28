#include<iostream>
using namespace std;
int main()
{
    int t,r,c,i,j,k,l;
    char a[26][26],ch;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>r>>c;
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                cin>>a[j][k];
            }
        }
        bool flag=0;
        // L->R
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                if(a[j][k]!='?')
                {
                    ch=a[j][k];
                    for(l=k+1;l<c;l++)
                    {
                        if(a[j][l]!='?') break;
                        else a[j][l]=ch;
                    }
                    k=l-1;
                }

            }
        }
        //R->L
        for(j=0;j<r;j++)
        {
            for(k=c-1;k>=0;k--)
            {
                if(a[j][k]!='?')
                {
                    ch=a[j][k];
                    for(l=k-1;l>=0;l--)
                    {
                        if(a[j][l]!='?') break;
                        a[j][l]=ch;
                    }
                    k=l+1;
                }

            }
        }
        //T->B
        for(j=1;j<r;j++)
        {
            if(a[j][0]=='?'&&a[j-1][0]!='?')
            {
                for(k=0;k<c;k++)
                a[j][k]=a[j-1][k];
            }
        }
        //B->T
        for(j=r-2;j>=0;j--)
        {
            if(a[j][0]=='?'&&a[j+1][0]!='?')
            {
                for(k=0;k<c;k++)
                a[j][k]=a[j+1][k];
            }
        }
        cout<<"Case #"<<i<<":"<<endl;
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                cout<<a[j][k];
            }
            cout<<endl;
        }
    }
    return 0;
}
