#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <string>
#include <cmath>
#include <list>
#include <cstring>
#include <functional>
#define INF 987654321
using namespace std;
int T;
string str;
int K;
int ans;
bool flag;
int main()
{
    //freopen("A-small-atempt0.in", "r", stdin);
    scanf("%d", &T);
    for(int test_case = 1; test_case <= T; test_case++)
    {
        ans = 0;
        cin >> str >> K;
        for(int i = 0 ; i < str.size(); i++)
        {
            if(str[i] == '+')
                continue;
            else
            {
                
                if(i + K >str.size())
                    break;
                ans++;
                for(int j = 0 ; j<K; j++)
                {
                    if(str[i+j]=='-')
                    str[i+j] = '+';
                    else
                    str[i+j] = '-';
                }
            }
        }
        flag = true;
        for(string::iterator it = str.begin(); it!= str.end(); it++)
        {
            if(*it=='-')
            {
                flag = false;
                break;
            }
        }
        if(flag)
        cout << "Case #"<<test_case<<": "<<ans<<endl;
        else
        cout <<"Case #"<<test_case<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}