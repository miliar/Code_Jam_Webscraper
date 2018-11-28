#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int t, k;
string s;
const char delim = ' ';

inline void flip(string& s, const int& k, const int& pos, const bool& mode)
{
    if(mode)
        for(int i = pos; i < pos+k; i++)
            if(s[i] == '+')
                s[i] = '-';
            else
                s[i] = '+';
    else
        for(int i = pos; i > pos-k; i--)
            if(s[i] == '+')
                s[i] = '-';
            else
                s[i] = '+';
}

int main()
{
    cout << "Hello world!" << endl;

    ifstream f("date.in");
    ofstream g("date.out");

    f >> t;
    f.get();
    for(int i = 1; i <= t; i++)
    {
        std::getline(f,s,' ');
        f >> k;
        f.get();

        int sol = 0;
        bool b = true;

        int ft = 0;
        while(s[ft] == '+') ft++;
        int l = s.length();
        while(s[l] == '+') l--;

        while(l-ft>=k)
        {
            if(b)
            {
                flip(s,k,ft, b);
                sol++;
                while(s[ft] == '+') ft++;
            }
            /*else
            {
                flip(s,k,l,b);
                sol++;
                while(s[l] == '+') l--;
                b = !b;
            }*/
        }

        //cout << s << endl;


        bool esol = true;
        for(int i = 0; i < s.length(); i++)
            if(s[i] != '+')
                esol = false;
        if(esol)
            g << "Case #" << i << ": " << sol << '\n';
        else
            g << "Case #" << i << ": IMPOSSIBLE" << '\n';


    }

    return 0;
}
