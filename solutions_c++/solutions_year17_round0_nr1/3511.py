#include<bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("out.txt","w+",stdout);
    int T,K,caseNum = 0;
    string s;

    cin >> T;
    while(T--)
    {
        int filpTime = 0;
        cin >> s >> K;
        for(int i = 0;i + K - 1< s.length();i++)
        {
            if(s[i] == '-')
            {
                for(int j = i;j < i + K;j++)
                    s[j] = s[j] == '-' ? '+' : '-';
                filpTime++;
            }
        }

        bool haveAnswer = true;
        for(int i = s.length() + 1 - K;i < s.length();i++)
        {
            if(s[i] == '-')
            {
                haveAnswer = false;
                break;
            }
        }

        if(haveAnswer)
            printf("Case #%d: %d\n",++caseNum,filpTime);
        else
            printf("Case #%d: IMPOSSIBLE\n",++caseNum);
    }
    return 0;
}
