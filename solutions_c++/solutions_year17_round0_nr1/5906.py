#include <iostream>
#include <bits/stdc++.h>

using namespace std;

char c[2000];


int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    //cin>>v0>>v1>>d>>t;
    int k,t;
    cin>>t;
    for(int t1=1;t1<=t;t1++)
    {
        //double cos=-2*(v1*v1)/(2*(v0*v0+v1*v1))
        memset(c,'\0',sizeof(c));
        cin>>c;
        char c1[2000];
        int flag1=1,flag2=1;
        strcpy(c1,c);
        cin>>k;
        int ans1=0,ans2=0;
        int len=strlen(c);
        for(int i=0;i<=len-k;i++)
        {
            if(c1[i]=='-')
            {
                //cout<<i<<' ';
                for(int j=i;j<i+k;j++){
                    if(c1[j]=='-')
                        c1[j]='+';
                    else
                        c1[j]='-';
                }
                ans1++;
            }
        }
        //cout<<c<<endl;
        //cout<<c1<<endl;
        for(int i=0;i<len;i++){
            if(c1[i]=='-')
                flag1=0;
        }
        strcpy(c1,c);
        for(int i=len-1;i>=k-1;i--)
        {
            if(c1[i]=='-')
            {
                //cout<<i<<' ';
                for(int j=i;j>i-k;j--){
                    if(c1[j]=='-')
                        c1[j]='+';
                    else
                        c1[j]='-';
                }
                ans2++;
            }
        }
        //cout<<c<<endl;
        //cout<<c1<<endl;
        for(int i=0;i<len;i++){
            if(c1[i]=='-')
                flag2=0;
        }
        if(flag1&flag2)
        printf("Case #%d: %d\n",t1,min(ans1,ans2));
        else if(flag1)
        printf("Case #%d: %d\n",t1,ans1);
        else if(flag2)
        printf("Case #%d: %d\n",t1,ans2);
        else
        printf("Case #%d: IMPOSSIBLE\n",t1);

        //cout << "Hello world!" << endl;
    }
    return 0;
}
