#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        vector<bool> pancakes;
        string s;
        cin >> s;
        for(int j = 0; j < s.size(); j++)
        {
            if(s[j] == '+')
                pancakes.push_back(true);
            else
                pancakes.push_back(false);
        }
        int k;
        cin >> k;
        int n = pancakes.size();
        bool possible = (k <= n);
        int uses = 0;
        int cur = 0;
        while(cur + k <= n)
        {
            if(not(pancakes[cur]))
            {
                uses++;
                for(int j = cur; j < cur + k; j++)
                    pancakes[j] = not(pancakes[j]);
            }
            cur++;
        }
        for(int j = 0; j < n; j++)
            possible = possible && pancakes[j];
        cout << "Case #" << i << ": " ;
        if(possible)
            cout << uses << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}
