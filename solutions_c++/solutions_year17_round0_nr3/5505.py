#include<iostream>
using namespace std;
int main()
{
    int a,b,i,cnt,cnt2,temp,pos,j,tt;
    cin>>tt;
    for(int tt2=0;tt2<tt;tt2++)
    {
        cout<<"Case #"<<tt2+1<<": ";
    cin>>a>>b;
    string l="l";
    for(i=0;i<a;i++)
        l+='-';
    l+='l';
    for(i=0;i<b;i++)
    {
        cnt=0;
        cnt2=0;
        pos=-1;
        for(j=0;j<a+2;j++)
        {
            if((l[j])=='-')
                cnt2++;
            else
            {
                if(cnt2>cnt)
                {
                    cnt=cnt2;
                    pos=j;
                }
                cnt2=0;
            }
        }
        if(cnt%2==0)
        {
            temp=pos-cnt/2-1;
            l[temp]='l';
        }
        else
        {
            temp=pos-((cnt+1)/2);
            l[temp]='l';
        }
    }
    if(cnt%2==0)
    {
        cout<<cnt/2<<" "<<cnt/2-1;
    }
    else
    {
        cout<<(cnt+1)/2-1<<" "<<(cnt+1)/2-1;
    }
    cout<<endl;
    }
}
