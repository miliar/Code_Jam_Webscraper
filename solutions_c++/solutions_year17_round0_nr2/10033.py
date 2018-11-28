#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        long long int n,j;
        cin>>n;
        bool flag;
        for(j=n;j>0;j--)
        {
            flag=true;
            long long int p=j;
            while(p)
            {
                int k=p%10;
                p/=10;
                if(k<p%10)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)
                break;
        }
        cout<<"Case #"<<i+1<<": "<<j<<endl;
    }
    return 0;
}
