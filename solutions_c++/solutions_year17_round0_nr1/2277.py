#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    int i,j,k,counter,testcase,testcaseno=0,flippersize;
    int a[2000],tempsize;

    cin>>testcase;

    while(testcaseno++ <testcase)
    {
        cin>>s>>flippersize;
        tempsize = s.size();

        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')a[i+1]=1;
            else a[i+1] = 0;
        }

        counter=0;

        for(i=1; i <= tempsize - flippersize +1; i++)
        {
            if(a[i])
            {
                counter++;

                for(j=i;j<= i+ flippersize - 1; j++)
                {
                    a[j]=(a[j] + 1)% 2;
                }
            }
        }
        bool impossible = false;

        for(i=1;i<=tempsize;i++)
        {
            if(a[i]==1)
            {
                impossible = true;
                break;
            }
        }
        if(impossible)
        {
            printf("Case #%d: IMPOSSIBLE\n",testcaseno);
        }
        else
        {
            printf("Case #%d: %d\n",testcaseno,counter);
        }
    }
    return 0;
}
