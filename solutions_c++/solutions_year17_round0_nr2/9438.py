#include <bits/stdc++.h>
using namespace std;
int main()
{

    long long N;
    int T;
    cin >> T;
    for (int j = 0; j < T; ++j)
    {  
        cin >> N;
        string w = to_string(N);
        int size = w.length();
        for (int i = size-1; i > 0 ; --i)
        {
            if (w[i]-'0' < w[i-1]-'0')
            {
                w[i-1] = w[i-1] - 1;
                for (int f = i; f < size ; ++f)
                {
                    w[f] = '9';
                }
            }
        }
        if (w[0]=='0')
        {
            w.erase(0,1);
        }
        cout <<"Case #" << j+1 <<": " << w <<endl;
    }
   
    return 0;
}
