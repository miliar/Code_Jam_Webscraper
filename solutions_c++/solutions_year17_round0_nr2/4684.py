#include<bits/stdc++.h>
using namespace std;


main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t ;
    scanf("%d",&t);
    string s;
    char n[20];
    int number[20];
    for(int i=1;i<=t;i++)
    {  cin>>s;
       strcpy(n,s.c_str());
       int len=s.length();
       for(int y=0;y<len;y++) number[y]=n[y]-'0';
       cout<<"Case #"<<i<<": ";
//       for(int i=0;i<len;i++)cout<<number[i];cout<<endl;
       int shift=0;
       if (len==1) cout<<number[0];
       else
       {
       for (int j = 0;j<len-1 ; j++)
       {
           if(number[j]<=number[j+1])
            {
                if(number[j]==number[j+1])  shift++;
                else shift=0;
                if(j+1>=len-1) for(int h=0;h<len;h++) cout<<number[h];
            }
           else
           {
//               printf("j:%d  shift:%d  number[j]:%d\n",j,shift,number[j]);
               if (j-shift==0 &&number[0]==1)       for(int k=0;k<len-1;k++)cout<<'9';
                else
               {
                   for(int k=0;k<j-shift;k++) cout<<n[k];
                    number[j-shift]--;
                    cout<<number[j-shift];
                   for(int k=j-shift+1;k<len;k++) cout<<9;
               }
              break;
           }
       }
       }
       cout<<endl;
    }








}
