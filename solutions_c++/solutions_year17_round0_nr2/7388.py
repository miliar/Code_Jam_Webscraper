#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,t=1,k,f=0;
    cin>>T;
    while(T--)
    {
        char a[20];
        long long int num=0;
        scanf("%s",a);
        f=0;
        int i,n=strlen(a),m;
        if(n>=2)
        {

            if(a[0]=='1'&&a[1]=='0')
            {
                a[0]=0;
                for(int i=1;i<n;i++)
                    a[i]='9';
            }
            else
            {
                for(i=0;i<n-1;i++)
                {
                    k=i;
                    while(a[k]>a[k+1]&&k>=0)
                    {
                        a[k]=a[k]-1;
                        for(m=k+1;m<n;m++)
                        a[m]='9';
                        k--;
                    }
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(n==1)
            cout<<a[0];
        else{
        for(i=0;i<n;i++)
        {
            if(a[i]==0)
                continue;
            cout<<a[i];
        }
        }
        cout<<endl;
            t++;
    }

    return 0;
}
