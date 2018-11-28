#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

char num[30];

int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
    int T;
    cin >> T;
    for(int k = 1; k <= T; ++k)
    {
        cin >> num;
        int len = strlen(num),i = 0;
        if(len == 1)
        {
            goto len1;
        }
        for(int t = 0; t <= len; ++t)
            for(i = 0; i < len - 1; ++i)
            {
                if(num[i] > num[i + 1])
                {
                    for(int j = i + 1; j < len; ++j)
                    {
                        num[j] = '9';
                    }
                    if(--num[i] < '0')
                    {
                        num[i] = '0';
                    }
                }
            }
        for(i = 0; num[i] == '0'; ++i);
len1:
        cout << "Case #" << k << ": ";
        cout << (num + i)<< endl;
    }
}
