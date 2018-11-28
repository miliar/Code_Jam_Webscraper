#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,n,j;
    int p=0;
    scanf("%d",&t);
    while(t--)
    {
        p++;
        int flag=1;
        scanf("%d",&n);
        vector<int> v;
        for(i=n;i>=1;i--)
        {
            int temp=i;
            flag=1;
            while(temp)
            {
                v.push_back(temp%10);
                temp/=10;
            }
            sort(v.begin(),v.end());
            temp=i;
            for(j=v.size()-1;j>=0;j--)
            {
                if(v[j]==temp%10)
                {
                    temp/=10;
                }
                else
                {
                    flag=-1;
                    break;
                }
            }
            if(flag==1)
                break;
            v.clear();
        }
        printf("Case #%d: %d\n",p,i);
    }
    return 0;
}

