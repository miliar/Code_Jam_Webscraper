#include<cstdio>
#include<string>
#include<vector>
#include<iostream>

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int TestCase, p = 0;
    scanf("%d",&TestCase);
    while(TestCase--)
    {
        printf("Case #%d: ",++p);
        std::string strPancake;
        int K,len,ans=0,count=0;
        std::cin>>strPancake>>K;
        len = strPancake.length();
        std::vector<int> V(len+1,0);
        for(int i=0;i<len-K+1;i++)
        {
            if(strPancake[i] == '-')
            {
                if(count%2==0)
                    ans++,count++,V[i+K-1] = 1;
            }
            else
            {
                if(count%2==1)
                    ans++,count++,V[i+K-1] = 1;
            }
            if(V[i])
                count--;
        }
        bool flag = 0;
        for(int i = len-K+1; i<len;i++)
        {
            if(count%2==0 && strPancake[i] == '-' || count%2==1 && strPancake[i] == '+')
            {
                printf("IMPOSSIBLE\n");
                flag=1;
                break;
            }
            if(V[i])
                count--;
        }
        if(!flag)
            printf("%d\n",ans);
    }
    fclose(stdout);
    return 0;
}
