#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstring>

using namespace std;

int t;
string str;
int n;


int main(void)
{
    freopen("A-large.in", "r", stdin);
    freopen("codejam_output.txt", "w", stdout);

    cin >> t;
    for(int p=1;p<=t;p++)
    {
        bool check = false;
        int cnt = 0;
        cin >> str >> n;

        for(int i=0;i<=str.size()-n;i++)
        {
            if(str[i] == '-')
            {
                cnt++;
                for(int j=i;j<i+n;j++)
                {
                    if(str[j] == '-')
                        str[j] = '+';
                    else if(str[j] == '+')
                        str[j] = '-';
                }
            }
        }

        for(int i=0;i<str.size();i++)
        {
            if(str[i] == '-')
            {
                check = true;
                break;
            }
        }
        if(check)
            printf("Case #%d: IMPOSSIBLE\n", p);
        else
            printf("Case #%d: %d\n", p, cnt);

    }
}
