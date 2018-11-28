#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int RG, BO, YV;
int n, R, O, Y, G, B, V;

string ans;

void print()
{
    for(;Y;)
    {
        ans += 'Y';
        --Y;

        if(B > R)
        {
            --B;
            ans += 'B';
        }
        else if(R >= B and R >= 1)
        {
            --R;
            ans += 'R';
        }
        else
        {
            ans = "IMPOSSIBLE";
            return;
        }
    }
    while(R > 0 and B > 0)
    {
        if(ans[ans.size() - 1] == 'R')
        {
            --B;
            ans += 'B';
        }
        else
        {
            --R;
            ans += 'R';
        }
    }
    if(R)
    {
        if(ans[ans.size() - 1] == 'B')
        {
            ans += 'R';
            --R;
        }
        string x = ans;
        ans.clear();
        ans += x[0];
        for(int i = 1;;++i)
        {
            if(R == 0)
            {
                for(int j = i;j < x.size();++j)
                    ans += x[j];
                break;
            }
            ans += 'R';
            if(x[i] == 'R')
            {
                ans = "IMPOSSIBLE";
                return;
            }
            ans += x[i];
            --R;
        }
    }
    else if(B)
    {
        if(ans[ans.size() - 1] == 'R')
        {
            ans += 'B';
            --B;
        }
        string x = ans;
        ans.clear();
        ans += x[0];
        for(int i = 1;;++i)
        {
            if(B == 0)
            {
                for(int j = i;j < x.size();++j)
                    ans += x[j];
                break;
            }
            ans += 'B';
            if(x[i] == 'B')
            {
                ans = "IMPOSSIBLE";
                return;
            }
            ans += x[i];
            --B;
        }
    }
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("sout.out", "w", stdout);
    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%d", &n);
        scanf("%d %d %d %d %d %d", &R, &O, &Y, &G, &B, &V);


        if(Y >= R and Y >= B)           print();

        else if(B >= R and B >= Y)
        {
            swap(Y, B);
            print();

            if(ans != "IMPOSSIBLE")
            {
                for(int i = 0;i < ans.size();++i)
                {
                    if(ans[i] == 'Y')           ans[i] = 'B';
                    else if(ans[i] == 'B')      ans[i] = 'Y';
                }
            }
        }
        else
        {
            swap(Y, R);
            print();

            if(ans != "IMPOSSIBLE")
            {
                for(int i = 0;i < ans.size();++i)
                {
                    if(ans[i] == 'Y')           ans[i] = 'R';
                    else if(ans[i] == 'R')      ans[i] = 'Y';
                }
            }
        }

//        RG = R - G;
//        BO = B - O;
//        YV = Y - V;
//        if(RG >= 0 and BO >= 1 and YV >= 0)
//        {
//            if((RG + BO - 1 == 0 and YV <= 1) or (YV >= 1))           GOV();
//        }
//        else if(RG >= 0 and YV >= 1 and BO >= 0)
//        {
//            if((RG + YV - 1 == 0 and BO <= 1) or (BO >= 1))           GVO();
//        }
//        else if()

        printf("Case #%d: %s\n", c, ans.c_str());
        ans.clear();
    }
    return 0;
}
