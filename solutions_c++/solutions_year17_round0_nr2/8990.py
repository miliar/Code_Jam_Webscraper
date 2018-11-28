#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,t,num;
    string a;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cout<<"Case #"<<ca<<": ";
        cin>>a;
        if(a.size()==1)
            cout<<a<<endl;
        else
        {
            num=a[a.size()-1];
            t=a.size();
            for(int i=a.size()-2;i>=0;i--)
            {
                if(a[i]>num)
                {
                    a[i]--;
                    t=i+1;
                }
                num=a[i];
            }
            if(a[0]!='0')
                cout<<a[0];
            for(int i=1;i<t;i++)
                cout<<a[i];
            for(int i=t;i<a.size();i++)
                cout<<'9';
            cout<<endl;
        }
    }
    return 0;
}
