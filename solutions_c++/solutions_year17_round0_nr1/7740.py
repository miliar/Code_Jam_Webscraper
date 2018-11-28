

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cstring>

using namespace std;
ofstream out("pankaflip.out");
ifstream in("pankaflip.in");

#define dim 1009

int T;
int n;
int v[dim];
string noSolution = "IMPOSSIBLE";

bool isCorect()
{
    if(n == 0)
        return true;

    for(int i = 1 ; i<=n; ++i)
        if(v[i] == -1)
            return false;
    return true;
}


int main()
{
    in >> T;
    for(int test = 1;  test<=T; ++test)
    {
        out << "Case " << "#" << test << ":" << " ";
        int sol = 0;
        string s;
        int k;
        in >> s >> k;
        n = 0;

        for(int i = 0 ; i < s.length(); ++i)
        {
            if(s[i] == '-')
            {
                v[++n] = -1;
            }
            else
            {
                v[++n] = 1;
            }
        }
        if(isCorect())
        {
            out << 0 << '\n';
        }
        else
        {
            int pozMinus = -1;
            for(int i = 1 ; i<=n-k+1; ++i)
            {
                if(v[i] == -1)
                {
                    //cout << "I : " << i << " si acuma j-urile ";
                    int step = k;
                    for(int j = i; j<=n && step; ++j)
                    {
                        //cout << "J-ul " << j << " si elementul ";
                        v[j] = (-1) * v[j];
                        //cout << v[j] << " ";
                        if(v[j] == -1 && pozMinus == -1)
                        {
                            pozMinus = j;
                        }
                        --step;
                    }
                    ++sol;
                }
                //cerr << "I-ul: " << i << " ";
               // for(int j = 1 ; j<=n; ++j)
                 //   cerr << v[j] << " ";

                //cerr << '\n';

                if(pozMinus != -1)
                {
                    if(pozMinus > n-k+1)
                    {
                        sol = -1;
                        break;
                    }
                    i = pozMinus-1;
                    pozMinus = -1;
                }
            }

            if(!isCorect())
            {
                sol = -1;
            }

            if(sol == -1)
            {
                out << noSolution << '\n';
                continue;

            }

            out << sol << '\n';
        }

        //cerr << '\n' << "----------------" << '\n';

    }
}

