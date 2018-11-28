#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long int lld;
int main()
{
    freopen("input2.in","r",stdin);
    freopen("out2.txt","w",stdout);
    lld t,tno=1;
    cin>>t;
    while(t--)
    {
        char a[10001];
        lld k,i,j,cnt=0;
        cin>>a>>k;
        //cout<<a<<endl;
        for(i=0;i<strlen(a)-k+1;i++)
        {
            if(a[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    if(a[j]=='-')
                        a[j]='+';
                    else
                        a[j]='-';
                }
                cnt++;
                //cout<<a<<endl;
            }
        }
        for(j=0;j<strlen(a) && a[j]=='+';j++);
        cout<<"Case #"<<tno<<": ";
        if(j==strlen(a))
            cout<<cnt<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
        tno++;
    }
    return 0;
}
