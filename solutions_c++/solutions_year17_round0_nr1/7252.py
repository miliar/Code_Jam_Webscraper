#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
    ifstream in("A-large.in");
    ofstream out("output");
    int t, l;

    in >> t;

    for(l = 1 ; l <= t ; l++)
    {
        int k, i, j;
        string s;
        in >> s >> k;

        int len = s.size();
        int ctr = 0;
        for(i = 0 ; i <= (len-k) ; )
        {
            if(s[i] == '-')
            {
                ctr++;
                for(j = i ; j < i+k ; j++)
                {
                    if(s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
                for(j = i ; j < len ; j++)
                {
                    if(s[j] == '-')
                    {
                        i = j;
                        break;
                    }
                }
            }
            else
            {
                i++;
            }
        }
        bool check = true;
        for(i = 0 ; i < len ; i++)
        {
            if(s[i] == '-')
            {
                check = false;
                break;
            }
        }
        if(check == false)
            out <<"Case #"<< l << ": " <<"IMPOSSIBLE\n";
        else
            out <<"Case #"<< l << ": " << ctr << '\n';
    }
    return 0;
}
