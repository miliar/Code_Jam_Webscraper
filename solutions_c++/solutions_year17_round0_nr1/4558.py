#include <iostream>
#include <string>

using namespace std;


string minFlipCount(string s, int k)
{
    int counter = 0;

    int i = 0;
    for(; i < s.size() - k + 1; i++)
    {
        if(s[i] != '+')
        {
            for(int j = i; j < i + k; j++)
                s[j] = (s[j] == '+') ? '-' : '+';

            counter++;
        }
    }

    for(; i < s.size(); i++)
    {
        if(s[i] != '+')
        {
            return "IMPOSSIBLE";
        }
    }

    return to_string(counter);
}

int main()
{
    int t;
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        string s;
        int    k;

        cin >> s >> k;

        cout << "Case #" << (i + 1) << ": " << minFlipCount(s, k) << endl;
    }
}