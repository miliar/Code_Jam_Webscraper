#include<iostream>
using namespace std;
int main()
{
    string k;
    int f1,t1,t2,test,f3,f4;
    cin>>test;
    for(int z=0;z<test;z++)
    {
        cout<<"Case #"<<z+1<<": ";
        cin>>k;
        here:
        int len=k.length();
        if(k[len-1]=='0' && k[0]=='1')
        {
            f4=0;
            for(int rr2=1;rr2<len-1;rr2++)
            {
                if(k[rr2]!='0')
                {
                    f4=1;
                    break;
                }
            }
            if(f4==1)
            {
                goto n2;
            }
            for(int rr=0;rr<len-1;rr++)
                cout<<"9";
            cout<<endl;
            continue;
        }
        n2:
        f3=0;
        for(t1=0;t1<len-1;t1++)
        {
            if(k[t1]>k[t1+1])
            {
                f1=t1;
                f3=1;
                break;
            }
        }
        if(f3==1)
        {
            k[t1]--;
            for(t2=t1+1;t2<len;t2++)
                k[t2]='9';
            goto here;
        }
        if(k[0]=='0')
        {
        for(int z2=1;z2<len;z2++)
        {
            cout<<k[z2];
        }
        cout<<endl;
        }
        else
        {
        cout<<k<<endl;
        }
    }
}
