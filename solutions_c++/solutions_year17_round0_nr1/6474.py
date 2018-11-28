#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int i,j,t,k;
    scanf("%d",&t);
    int cnt=0;

    string ss;

    for(int kk1=1;kk1<=t;kk1++)
    {
        cin>>ss;
        scanf("%d",&k);
        int len=ss.size();
        cnt=0;
        for(i=0;i<=len-k;i++)
        {
            if(ss[i]=='-')
            {
                cnt++;
                for(j=i;j<i+k;j++)
                {
                    if(ss[j]=='-')
                    {
                        ss[j]='+';
                    }
                    else
                    {
                        ss[j]='-';
                    }
                }
            }
         //   cout<<ss<<endl;
        }

     //   cout<<cnt<<endl;

     bool flag=true;

     for(i=0;i<len;i++)
     {
         if(ss[i]=='-')
         {
             flag=false;
             break;
         }
     }

   //  Case #1: 3

     printf("Case #%d: ",kk1);

     if(flag)
     {
         cout<<cnt<<endl;

     }
     else
     {
         cout<<"IMPOSSIBLE"<<endl;
     }

    }


}
