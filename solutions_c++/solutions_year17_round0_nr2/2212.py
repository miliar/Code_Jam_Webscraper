#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool f;
    string n;
    int t,s,j;
    long long a;
    scanf("%d",&t);
    for(int i=1; i<=t; ++i)
    {
        printf("Case #%d: ",i);
        cin>>n;
        s=n.size();
        f=1;
        while(f)
        {
            f=0;
            for(j=0; j<s-1; ++j)
            {
                if(n[j]>n[j+1])
                {
                    --n[j];
                    ++j;
                    while(j<s)
                    {
                        n[j]='9';
                        ++j;
                    }
                    f=1;
                }
            }
        }
        a=0;
        for(j=0; j<s; ++j)
        {
            a*=10;
            a+=(n[j]-'0');
        }
        cout<<a<<endl;
    }
    return 0;
}
