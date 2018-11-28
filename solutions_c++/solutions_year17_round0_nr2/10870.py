#include <iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<sstream>
#include <algorithm>

using namespace std;
long long int tidy(long long int td)
{

    while(td)
    {
        string input="";
        long long int a = td;
        stringstream ss;
        ss << a;
        input =ss.str();
        //cout<<input<<endl;
        bool ans=false;
        if(input.length()==1)return td;
        for (int i = 1; i < input.length(); ++i) {
            char  temp=input[i];
            if(temp-0>=input[i-1]-0)
            {
                ans=true;
                continue;
            }
            else
            {
                ans=false;
                break;
            }
        }

        if(ans==true)return td;
        td--;
    }

}
int main()
{
    freopen("B-small-attempt0.in", "r",stdin);
    freopen("output.out", "w",stdout);
    long long int t,n;
    scanf("%lld",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%lld",&n);
        long long int td=tidy(n);
        printf("Case #%d: %lld\n",i,td);
    }

    return 0;
}