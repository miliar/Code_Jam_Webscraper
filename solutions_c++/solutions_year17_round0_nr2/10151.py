#include<iostream>
#include<algorithm>
#include<string.h>
#include<stdio.h>
using namespace std;

int t,i,j,k,l,n,m,flag=0;
char a[100][1000];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("TidySout1.txt","w",stdout);

    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>a[i];
    }

    for(i=0;i<t;i++)
    {
        l=strlen(a[i]);
        if(l==1)
        {
            cout<<"Case #"<<i+1<<": "<<a[i]<<"\n";
        }
        else
        {
            for(j=1;j<l;j++)
            {
                if(a[i][j]<a[i][j-1])
                {
                    while(a[i][j]<=a[i][j-1])
                    {
                        if(a[i][j]!='0')
                        {
                            a[i][j]--;
                        }
                        else
                        {
                            if(a[i][j-1]!='0')
                            {
                                n=j;
                                flag=0;
                                while(a[i][j]=='0' && a[i][j]!='\0')
                                {
                                    a[i][j]='9';
                                    if(a[i][j+1]!='\0' && a[i][j+1]!='0')
                                        a[i][j+1]='9';
                                    flag=1;
                                    j++;
                                }
                                if(flag==1)
                                    a[i][n-1]--;
                                j=n;
                            }
                        }
                    }
                    j=0;
                }
            }
            cout<<"Case #"<<i+1<<": ";
            for(j=0;j<l;j++)
                if(a[i][j]!='0')
                    cout<<a[i][j];

            cout<<"\n";
        }
    }
return 0;
}
