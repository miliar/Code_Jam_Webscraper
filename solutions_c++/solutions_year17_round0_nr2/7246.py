#include <fstream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
    ifstream in("B-large.in");
    ofstream out("output");
    int t, k;

    in >> t;

    for(k = 1 ; k <= t ; k++)
    {
        int i, j;

        string n;
        in >> n;

        out << "Case #"<<k<<":"<<" ";

        int len = n.size();

            for(i = 0 ; i < len-1 ; i++)
            {
                if(n[i]-'0' > n[i+1]-'0')
                {
                    break;
                }
            }
            if(n[i+1] == '\0')
            {
                out << n << '\n';
            }
            else
            {
            for(j = i+1 ; j < len ; j++)
                n[j] = '9';

            while(n[i]-'0' == n[i-1]-'0')
            {
                if(i == 0)
                    break;
                n[i] = '9';
                i--;
            }
            n[i] = --n[i];
            int ct = 0;

            for(i = 0 ; i < len ; i++)
            {
                if(n[i] != '0')
                {
                    ct++;
                }
                if(ct != 0)
                {
                    out << n[i];
                }
            }
            out << '\n';
            }


    }
    return 0;
}
