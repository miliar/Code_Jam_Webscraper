#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        string str;
        cin>>str;
        int k;
        cin>>k;
        int count=0;
        int len=str.length(),p;
        bool flag=true;
        for(int j=0;j<len;j++)
        {
            if(str[j]=='-')
            {
                for(p=0;(p<k && j+k<=len);p++)
                {
                    if(str[j+p]=='-')
                        str[j+p]='+';
                    else
                        str[j+p]='-';
                }
                if(p!=k)
                {
                    flag=false;
                    break;
                }
                count++;
            }
        }
        if(!flag)
            cout<<"Case #"<<i+1<<": IMPOSSIBLE";
        else
            cout<<"Case #"<<i+1<<": "<<count;

        cout<<endl;
    }

    return 0;
}
