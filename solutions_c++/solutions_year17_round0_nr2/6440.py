#include<bits/stdc++.h>

using namespace std;
string ss;
int len;

void call(int pos)
{
    if(pos==len-2)
        return;
    if(ss[pos]<=ss[pos+1])
        call(pos+1);
    else
    {
        int y1;
        y1 = ss[pos]-'0'-1;
        ss[pos]=y1+'0';

        for(int i=pos+1;i<len;i++)
        {
            ss[i]='9';
        }

        call(pos-1);
    }


}


int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,t,k;
    scanf("%d",&t);
    int cnt=0;



     for(int kk1=1;kk1<=t;kk1++)
    {
       cin>>ss;
       ss='0'+ss+'9';
    //   cout<<ss<<endl;

       len = ss.size();

      // bool flag=false;

      // for(i=0;i<len;i++)
      // {

    //   }

       call(1);
       printf("Case #%d: ",kk1);

       for(i=1;i<len-1;i++)
       {
           if(ss[i]!='0')
           cout<<ss[i];
       }
      cout<<endl;














       }




}


