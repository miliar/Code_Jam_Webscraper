#include <iostream>
#include <string>
#include <map>
using namespace std;

/* Testcases:
5
---+-++- 3
++++-++- 3
+++++ 4
-+-+- 4
---+ 3
---- 4
*/

int minus_count(string s)
{
    int count = 0;
    for(int i=0, n = s.size(); i<n; ++i)
        if (s[i] == '-')
            count++;
    return count;
}

void flip(string & s, int pos, int n)
{
    for(int i=pos; i<pos+n; ++i)
    {
        if(s[i] == '-')
            s[i] = '+';
        else s[i] = '-';
    }
}

int test(string s, int n)
{
    // Create string with only +
    int size = s.size();
    string pass(size, '+');
    if(s == pass) // if string already +
        return 0;

    //otherwise we have to flip
    int flip_count = 0;
    string varied_string = s; //copy string s

    // remember all checked combinations
    map<string, int> combinations;
    combinations[s] += 1;

    // flipping
    //cout << "before flip " << ": " << varied_string << endl;
    for(int i = 0; i<size; i++)
    {
        int minus_pos = varied_string.find('-');
        if(minus_pos <= size - n)
            flip(varied_string, minus_pos, n);
        else
            flip(varied_string, size - n, n);
        flip_count++;
        //cout << "after flip " << flip_count <<": " << varied_string << endl;

        if(varied_string == pass)
            return flip_count;

        if(combinations[varied_string] != 0)
            return -1;
        else
            combinations[varied_string] += 1;
    }
    return -2;
}

int main()
{
    int t, n;
    string s;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        //cout << endl;
        cin >> s >> n;

        int result = test(s,n);
        string m;
        if(result<0)
            m = "IMPOSSIBLE";
        else
            m = to_string(result);
        cout << "Case #" << i << ": " << m << endl;
    }

    return 0;
}
