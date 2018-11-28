#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("test1.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    long long int t,n,k,i,l,j,y=1;
    cin>>t;
    int a[100],b[100];
    for(y=1;y<=t;y++)
    {
        cin>>n;
        cout<<"Case #"<<y<<": ";
        k=n;
        l=0;
        while(k)
        {
            a[l++]=k%10;
            k=k/10;
        }
        j=0;
        for(i=l-1;i>=0;i--)
        {
            b[j++]=a[i];
        }
        for(i=1;i<l;i++)
        {
            if(b[i]<b[i-1])
                break;
        }
        if(i==l)
        {
            for(i=0;i<l;i++)
                cout<<b[i];
            cout<<endl;

        }
        else
        {

            for(j=i-1;j>0;j--)
            {
                if(b[j-1]<b[j])
                    break;
            }
            if(j==0)
            {
                b[0]=b[0]-1;
                if(b[0]==0)
                {
                    for(i=1;i<l;i++)
                        cout<<"9";
                }
                else
                {
                    cout<<b[0];
                    for(i=1;i<l;i++)
                    {
                        cout<<"9";
                    }
                }

                cout<<endl;
            }
            else
            {
                b[j]=b[j]-1;
                for(i=0;i<j;i++)
                    cout<<b[i];
                cout<<b[j];
                for(i=j+1;i<l;i++)
                {
                    cout<<"9";
                }
                cout<<endl;

            }
    }



    }
}
