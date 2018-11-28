#include <bits/stdc++.h>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    for(int caso = 1; caso <= cases; caso++)
    {
        int n, p;
        cin >> n >> p;
        vector<int> count(p);
        for(int i = 0; i < n; i++)
        {
            int tmp;
            cin >> tmp;
            count[tmp % p]++;
        }
        size_t result = 0;
        if(p == 2)
        {
            result = count[0] + count[1] / 2 + count[1] % 2;
        }
        else if(p == 3)
        {
            result += count[0];
            while(count[1] > 0 && count[2] > 0)
            {
                count[1]--;
                count[2]--;
                result++;
            }
            if(count[1] > 0)
            {
                result += count[1] / 3 + ((count[1] % 3 == 0) ? (0) : (1));
            }
            else if(count[2] > 0)
            {
                result += count[2] / 3 + ((count[2] % 3 == 0) ? (0) : (1));
            }
        }
        else if(p == 4)
        {
            result += count[0];
            while(count[1] > 0 && count[3] > 0)
            {
                count[1]--;
                count[3]--;
                result++;
            }
            while(count[2] > 1)
            {
                count[2] -= 2;
                result++;
            }
            if(count[2] > 0)
            {
                if(count[1] > 1)
                {
                    count[2]--;
                    count[1] -= 2;
                    result++;
                }
                else if(count[3] > 1)
                {
                    count[2]--;
                    count[3] -= 2;
                    result++;
                }
                else if(count[1] == 0 && count[3] == 0)
                {
                    result++;
                }
            }
            if(count[1] > 0)
            {
                result += count[1] / 4 + ((count[1] % 4 == 0) ? (0) : (1));
            }
            else if(count[3] > 0)
            {
                result += count[3] / 4 + ((count[3] % 4 == 0) ? (0) : (1));
            }
        }
        else
        {
            assert(!"Invalid p");
        }
        cout << "Case #" << caso << ": " << result << endl;
    }
    return EXIT_SUCCESS;
}
