#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int casenum = 1;casenum<=t;casenum++)
    {
        int answer = 0;
        string a;
        cin >> a;
        unsigned K;
        cin >> K;
        for(unsigned test = 0;test <= a.size()-K ;test++)
        {
            if(a[test] == '-')
            {
                //flip next K
                for(unsigned i = 0;i<K;i++)
                {
                    if(a[test+i] == '-')
                    {
                        a[test+i] = '+';
                    }
                    else
                    {
                        a[test+i] = '-';
                    }
                }
                answer++;
            }
        }

        bool d = true;
        for(unsigned i =0;i<a.size();i++)
        {
            if(a[i] == '-')
            {
                d = false;
            }
        }
        cout << "Case #" << casenum << ": ";
        if(d)
        {
            cout << answer << endl;
        }
        else
        {
            cout << "IMPOSSIBLE" << endl;
        }

    }
}
