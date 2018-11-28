#include<iostream>
using namespace std;
int main()
{
    int t,l,sl;
    int n,copyn;
    cin>>t;
    int flag=1;
    for(int i=1;i<=t;i++)
    {
        cin>>n;
        while(true)
        {
        flag=1;
        copyn=n;
        while(copyn!=0)
        {
            l=copyn%10;
            copyn=copyn/10;
            sl=copyn%10;
            if(sl>l)
            {
                flag=0;
                break;
            }

        }
        if(flag==1)
        {
            cout<<"Case #"<<i<<": "<<n<<endl;
            break;
        }
            else
            n--;

        }

    }
    return 0;
}
