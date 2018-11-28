#include <iostream>
using namespace std;
int checknum(unsigned long long a)
{
    unsigned long long temp = a;
    int checktemp1, checktemp2;
    checktemp1 = temp % 10;
    int flag = 1;
    while(temp>0)
    {
        //cout<<temp<<endl;
        checktemp2 = temp % 10;
        temp /= 10;
        if(checktemp2 <= checktemp1)
        {
            checktemp1 = checktemp2;
        }
        else
        {
            flag = 0;
            break;
        }
    }
    return flag;
}
int main()
{
    int t;
    cin>>t;
    for(int i=0; i<t; ++i)
    {
        unsigned long long a;
        cin>>a;
        for(unsigned long long j=a; j>=0; --j)
        {
            int res = checknum(j);
            //int res = 1;
            if(res == 1){
                cout<<"Case #"<<(i+1)<<": "<<j<<endl;
                break;
            }
            else
                continue;
        }
    }
}
