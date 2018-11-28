#include <iostream>

using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int i=0;i<test;i++)
    {
        string str;
        cin>>str;
        int k;
        cin>>k;
        int count=0;
        int l=str.length(),c,arr[l];
        for(int j=0;j<l;j++)
        {
            if(str[j]=='+')
                arr[j]=1;
            else
                arr[j]=0;
        }
        int flag=1;
        for(int j=0;j<l;j++)
        {
            if(arr[j]==0)
            {
                for(c=0;(c<k && j+k<=l);c++)
                {
                    arr[j+c]=arr[j+c] ^ 1;
                }
                if(c!=k)
                {
                    flag=0;
                    break;
                }
                count++;
            }
        }
        if(flag==0)
            cout<<"Case #"<<i+1<<": IMPOSSIBLE";
        else
            cout<<"Case #"<<i+1<<": "<<count;
        cout<<endl;
    }

    return 0;
}
