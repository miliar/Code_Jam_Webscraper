#include <iostream>
using namespace std;
typedef long long int lli;
bool isSorted(char str[])
{
    for(int i=1;str[i];i++)
    {
        if(str[i-1]>str[i])
            return false;
    }
    return true;
}
int main()
{
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/TidyNumbers/B-large.in","r",stdin);
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/TidyNumbers/output2.txt","w",stdout);
    int t,test=1;
    char str[102];
    int n,zero;
    cin>>t;
    while(t--)
    {
        cin>>str;
        n=(int)strlen(str);
        int i=n-1;
        while(!isSorted(str))
        {
            if(str[i]>=str[i-1])
            {
                str[i]='9';
            }
            else
            {
                if(str[i-1]!='0')
                    str[i-1]--;
                else
                    str[i-1]='9';
                str[i]='9';
            }
            --i;
        }
        zero=0;
        for(int i=0;i<n;i++)
        {
            if(str[i]=='0')
                zero++;
            else
                break;
        }
        for(int i=0;i+zero<=n;i++)
            str[i]=str[i+zero];
        cout<<"Case #"<<test++<<": "<<str<<endl;
    }
    return 0;
}
