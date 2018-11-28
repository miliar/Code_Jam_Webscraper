#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("date.in");
ofstream fout("date.out");

string s;
int l;
int cas;

void write()
{
    fout << "Case #" << cas << ": ";
    fout << s << "\n";
}

bool tidy()
{
    if (s.find("0") != string::npos)
        return false;

    for (int i = 0; i < l - 1; i ++)
        if (s[i] > s[i + 1])
        {
            return false;
        }
    return true;
}

void down()
{
    if (s[0] == '0')
    {
        s.erase(0, 1);
        l --;
        return;
    }

    for (int i = l - 1; i > 0; i --)
    {
        if (s[i] == '0')
        {
            for (int j = i; j < l; j ++)
                s[j] = '9';
            int k = 1;
            while(s[i - k] == '0')
            {
                s[i - k] = '9';
                k ++;
            }
            s[i - k] --;
            return;
        }
        if (s[i] < s[i - 1])
        {
            for (int j = i; j < l; j ++)
                s[j] = '9';
            s[i - 1] --;
            int k = 1;
            while(s[i - k] < s[i - k - 1])
            {
                s[i - k] = '9';
                s[i - k - 1] --;
                k ++;
            }
            return;
        }
    }
}

void rez()
{
    fin >> s;
    l = s.length();

    while(!tidy())
    {
        down();
    }
    write();
}

int main()
{
    int t;
    fin >> t;
    for (int i = 0; i < t; i ++)
    {
        cas ++;
        rez();
    }
}
