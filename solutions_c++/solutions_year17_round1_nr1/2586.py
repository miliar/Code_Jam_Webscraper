#include <iostream>
using namespace std;

int main() 
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        
        int r,c,j,k,y;
        cin>>r>>c;
        char a[r][c],f[1000];
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                cin>>a[j][k];
            }
        }
        for(j=0;j<c;j++)
        {
            f[j]='?';
        }
        
         for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                if(a[j][k]!='?')
                {
                    f[k]=a[j][k];   
                }
                else
                {
                    if(j==0&&r>1)
                    {
                        y=1;
                        while(a[j+y][k]=='?'&&y<r)
                        {
                            y++;
                        }
                        if(y==r)
                        y--;
                        a[j][k]=a[j+y][k];
                        f[k]=a[j][k];
                    }
                    else
                    {
                        a[j][k]=f[k];
                    }
                }
                //cout<<f[k];
            }
            //cout<<endl;
        }
        for(j=0;j<r;j++)
        {
            f[j]='?';
        }
        for(k=0;k<c;k++)
        {
            for(j=0;j<r;j++)
            {
                if(a[j][k]!='?')
                {
                    f[j]=a[j][k];   
                }
                else
                {
                    if(k==0&&c>1)
                    {
                        y=1;
                        while(a[j][k+y]=='?'&&y<c)
                        {
                            y++;
                        }
                        if(y==c)
                        y--;
                        a[j][k]=a[j][k+y];
                        f[j]=a[j][k];
                    }
                    else
                    {
                        a[j][k]=f[j];
                    }
                }
                //cout<<f[k];
            }
            //cout<<endl;
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
