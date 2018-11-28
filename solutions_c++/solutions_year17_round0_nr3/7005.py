#include<bits/stdc++.h>
using namespace std;
void insert_o(int ti,int t,int o[])
{
    //cout<<"entry"<<endl;
    //cout<<"o[2]="<<o[2]<<endl;
    int len=0;
    for(int i=0;o[i]!=(-1);i++)
    {
       len++;
    }
    //cout<<"len:"<<len<<endl;
    for(int i=len;i>=ti;i--)
    {
        o[i+1]=o[i];

    }
    o[ti]=t;
 //   cout<<"o[ti+2]="<<o[ti+2]<<endl;
   // cout<<"exit"<<endl;
}
int main()
{
int t;
cin>>t;
for(int tc=1;tc<=t;tc++)
{
    int n,k;
    cin>>n>>k;
    n+=2;
    int o[10000];
   // memset(o,-1,n);
    o[0]=1;
    o[1]=n;
    o[2]=-1;
    //int oi=0;
    int t,ti;
    for(int i=0;i<k;i++)
    {
        int j=1,diff=0;
        while(o[j]!=-1)
        {
           // cout<<"hello"<<endl;
            if(o[j]-o[j-1]>diff)
            {
            diff=o[j]-o[j-1];
            t=(o[j]+o[j-1])/2;
            ti=j;
            }
        j++;
        }
        //cout<<"ti="<<ti<<" t="<<t<<endl;
        insert_o(ti,t,o);

    }
  //      cout<<"ti="<<ti<<" t="<<t<<endl;

/*
    for(int i=0;o[i]!=-1;i++)
    {
        cout<<"i="<<i<<"    "<<o[i]<<endl;

    }
*/
        int ls=t-o[ti-1]-1,lr=o[ti+1]-t-1;
        if(ls>lr)
            cout<<ls<<" "<<lr;
        else
            cout<<lr<<" "<<ls;


        cout<<endl;
}


return 0;
}
