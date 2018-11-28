#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
    freopen("B-small-attempt3.out","w",stdout);
    long long int test ,t=0,ak;
    cin>>test;
    while(test--)
    {

    long long int  i;
    cin>>ak;
    for(i=ak;i>=1;i--)
    {
        string num;
        stringstream ak;
        ak<<i;
        num=ak.str();
        int findproblem=0;
        for(int k=0;k<num.length();k++)
        {
            if(num[k]=='0'|| ((num[k]>num[k+1])&&k<(num.length()-1)))
                findproblem=1;
        }
        if(findproblem==0)
        {
            cout<<"Case #"<<++t<<": "<<i<<endl;
            break;
        }

    }

    }



    return 0;
}
