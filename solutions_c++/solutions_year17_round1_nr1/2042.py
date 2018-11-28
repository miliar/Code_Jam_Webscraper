#include<iostream>
#include<bits/stdc++.h>
using namespace std;
char a[26][26];
int main()
{
    int t,r,c,i=1,f,p,ind;
    cin>>t;
    while(t--)
    {
        cin>>r>>c;
        f=0;p=0;ind=-1;
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
                {
                    cin>>a[j][k];
                }
        }
      /*   for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
                {
                    cout<<a[j][k];
                }
                cout<<endl;
        }
        cout<<endl;*/
        for(int j=0;j<r;j++)
        {
            f=0;
            for(int k=0;k<c;k++)
                {
                    if(a[j][k]=='?')
                    {
                        if(f==1)
                        {
                            if(j-1>=0)
                            a[j][k]=a[j-1][k];
                            else if(j==0)
                            p=1;
                        }

                        if(a[j][k-1]!='?'&&k-1>=0)
                        {
                            if(f!=1)
                            a[j][k]=a[j][k-1];
                        }
                        else
                        {
                        int o=k+1;
                        while(o<c)
                        {
                            if(a[j][o]!='?')
                                break;
                            o++;
                        }
                            if(o==c)
                            {
                                f=1;
                                if(j-1>=0&&ind!=j-1)
                                    a[j][k]=a[j-1][k];
                                else if(p==1&&ind<j)
                                    ind=j;
                                else if(j==0)
                                   {
                                        p=1;
                                        ind=j;
                                   }
                            }
                            else
                            a[j][k]=a[j][o];
                        }


                    }
                }
        }
        if(p==1)
            for(int j=ind;j>=0;j--)
            {
               for(int k=0;k<c;k++)
                {
                    a[j][k]=a[j+1][k];
                }
            }

        cout<<"Case #"<<i<<":"<<endl;
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
                {
                    cout<<a[j][k];
                }
                cout<<endl;
        }
        i++;
    }
    return 0;
}
