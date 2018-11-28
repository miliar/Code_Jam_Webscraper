#define _USE_MATH_DEFINES
#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(int argc, char** argv)
{
    ifstream fin; 
    ofstream fout;
    if (argc != 3)
    {
        cout << "incorrect usage" << endl;
        return -1;
    }
    fin.open(argv[1]);
    if (!fin)
    {
        cout << "input file not open error" << endl;
        return -1;
    }
    fout.open(argv[2]);
    if (!fout)
    {
        cout << "output file not open error" << endl;
        return -1;
    }
    int n;
    fin >> n;
    for (int i = 0; i < n; i++)
    {
        int k;
        string s;
        fin.ignore();
        fin >> s;
        fin >> k;
        string sad = "-";
        int n = s.find_first_of('-');
        int c = 0;
        if (n == string::npos)
            fout << "Case #" << i + 1 << ": 0" << endl;
        else
        {
            bool im = true;
            while (n != string::npos)
            {
                im = true;
                c++;
                for (int j = 0; j < k && im ; j++)
                {
                    if (n + j < s.length())
                    {
                        if (s[n + j] == '-')
                            s[n + j] = '+';
                        else
                            s[n + j] = '-';
                    }
                    else
                        im = false;
                }
                if (im != false)
                    n = s.find_first_of('-');
                else
                    n = string::npos;
            }
            if (im==true)
            fout << "Case #" << i + 1 << ": "<<c << endl;
            else
                fout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}


