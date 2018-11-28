#include <iostream>
#include<algorithm>
#include<fstream>
#include<cmath>
using namespace std;
long long int call(long long int n);
int main()
{    ifstream input;
     input.open("B-small-attempt0.in");
     ofstream output;
     output.open("code2.txt");

    long long int t,i;
    input>>t;
    for(i=0;i<t;i++)
    {    long long int w=0,q;
          int flag=0,r;
        long long int num,temp,temp1,n=0,u,j,count,res,x,y,ans;
        input>>num;

        for(j=0;j<num;j++)
        {
            res=num-n;
            count=call(res);
            if(count==1)
            {
                ans=res;
                break;
            }
            temp1=num;
            for(r=0;r<count&&(flag==0);r++)
            {
                q=temp1%10;
                temp1=temp1/10;
                if(q==0||q==1)
                    continue;
                else{
                    break;
                    }
            }
            if(r==count)
             {  flag=1;
               for(int t=0;t<count-1;t++)
             w=(w*10)+9;
                 break;}
            temp=res;
            u=count-1;
            while(u)
            {
                x=temp%10;
                temp=temp/10;
                y=temp%10;
                if(y<=x)
                   {
                     u=u-1;
                     continue;
                   }
                else
                    break;
            }
            if(u==0)
            {
                ans=res;
                break;
            }
            n++;
        }
        if(!flag)
        output<<"Case #"<<i+1<<": "<<ans<<endl;
        else
       output<<"Case #"<<i+1<<": "<<w<<endl;
    }
    return 0;
}
     long long int call(long long int n)
{  int a=0;
    while(n>0)
    {
        n=n/10;
        a++;
    }
    return (a);
}
