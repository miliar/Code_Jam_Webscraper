#include <iostream>
using namespace std;
const int MAXN=1003;
bool check(char str[])
{
    for(int i=0;str[i];i++)
        if(str[i]=='-')
            return false;
    return true;
}
int main()
{
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/OversizedPancakeFlipper/A-large.in","r",stdin);
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/OversizedPancakeFlipper/output2.txt","w",stdout);
    int t,test=1;
    int n,k;
    char str[MAXN];
    cin>>t;
    while(t--)
    {
        cin>>str;
        cin>>k;
        n=(int)strlen(str);
        int count=0,flag=1;
        for(int i=0;str[i];i++)
        {
            if(str[i]=='-')
            {
                if(i+k>n)
                {
                    flag=0;
                    break;
                }
                for(int j=i;j<i+k;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                ++count;
            }
        }
        if(flag)
            cout<<"Case #"<<test++<<": "<<count<<endl;
        else
            cout<<"Case #"<<test++<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
