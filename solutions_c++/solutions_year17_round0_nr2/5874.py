#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    char c[20];
    long long ans1;
    int t;
    cin>>t;
    for(int t1=1;t1<=t;t1++)
    {
        //long long a;
        memset(c,'\0',sizeof(c));
        cin>>c;
        int len=strlen(c);
        int flag=len-1;
        for(int i=len-1;i>=1;i--)
        {
            if(c[i]<c[i-1]){
                c[i-1]--;
                flag=i-1;
            }
        }
        if(c[flag]=='0')
        {
            while(c[flag]==0)
                flag--;
        }
        //c[flag]--;
        //int len=0;
        printf("Case #%d: ",t1);
        if(c[flag]=='0'&&flag==0)
        {
            for(int i=1;i<len;i++)
                cout<<'9';
            cout<<endl;
        }
        else
        {
            for(int i=0;i<=flag;i++)
                cout<<c[i];
            for(int i=flag+1;i<len;i++)
                cout<<'9';
            cout<<endl;
        }
        //printf("Case #%d: %d\n",t1,ans1);
    }
    //cout << "Hello world!" << endl;
    return 0;
}
