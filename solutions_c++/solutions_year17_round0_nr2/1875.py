#include <iostream>
#include <fstream>
using namespace std;
ifstream ka("B-large.in");
ofstream ki("output.out");

int t;
string s;
int main()
{
    ka >> t;
    for(int caz = 1; caz <= t; caz++)
    {
        ka >> s;
        bool gasit = false;
        for(int i = 0; i < s.size() - 1 && !gasit; i++)
        {
            if(s[i] > s[i + 1])
            {
                gasit = true;
                int k = i + 1;
                while(i >= 0 && s[i] > s[i + 1])
                {
                    s[i + 1] = '9';
                    s[i]--;
                    i--;
                }
                while(k < s.size())
                {
                    s[k] = '9';
                    k++;
                }
            }
        }
        ki << "Case #" << caz << ": ";
        bool primele = true;
        for(int i = 0; i < s.size(); i++)
        {
            if(s[i] != '0')
            {
                primele = false;
                ki << s[i];
            }
            else if(!primele)
                ki << s[i];
        }
        ki << '\n';
    }
}
