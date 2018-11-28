#include<iostream>
using namespace std;
int main()
{
    unsigned long long int a,s;
    int t,rem,rem1;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>a;
        while(a>0)
        {
            s=a;
            int flag=0;
            while(s>0)
            {
                rem=s%10;
                s=s/10;
                rem1=s%10;
                if(rem<rem1)
                    flag=1;
            }
            if(flag==1)
                a--;
            else
                break;
        }
        cout<<"Case #"<<i+1<<":  "<<a<<endl;
    }
}
