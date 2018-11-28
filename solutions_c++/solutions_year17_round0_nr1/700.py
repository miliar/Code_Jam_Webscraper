#include<bits/stdc++.h>
using namespace std;
int main()
{

      freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cases,caseno=0;
    cin>>cases;
    while(cases--)
    {
        char ch[10002];
        int k,i;
        cin>>ch>>k;
        int ans =0;
        int len = strlen(ch);
        for( i=0;i<=len-k;i++)
        {
            if(ch[i]=='-')
            {
                for(int j=0;j<k;j++)
                {
                    if(ch[i+j]=='-')
                    ch[i+j]='+';
                    else
                    ch[i+j] = '-';
                }
                ans++;
            }
        }
        int flag =1;
        for(int x=len-k+1;x<=len-1;x++)
        {
            if(ch[x]=='-')
            flag=0;
        }
        if(flag==1)
         cout<<"Case #"<<++caseno<<": "<<ans<<endl;
        else
        cout<<"Case #"<<++caseno<<": IMPOSSIBLE"<<endl;

    }
    return 0;
}
