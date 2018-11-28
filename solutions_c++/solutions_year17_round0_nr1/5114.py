#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{

    int nn;
    cin >> nn;

    for(int kk=1; kk<=nn; kk++)
    {
        string str;
        int K;
        cin >> str >> K;
        const unsigned n = str.size();
        vector<bool> s(n);
        for(int i=0; i<n; i++)
        {
            s[i] = str[i] == '+';
        }

        int res = 0;
        int i;
        for(i=0; i<n-K+1; i++)
        {
            if(!s[i])
            {
                res++;
                for(int j=0; j<K; j++)
                {
                    s[i + j] = !s[i + j];
                }
            }
        }

        bool good = true;
        for(; i<n; i++)
        {
            if(!s[i])
            {
                good = false;
                break;
            }
        }

        cout << "Case #" << kk << ": ";
        if(good)
        {
            cout << res << endl;
        }
        else
        {
            cout << "IMPOSSIBLE" << endl;
        }
        
        
    }

}
