#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    string s;
    int a[1000];
    for (int I = 1; I <= T; ++I)
    {
        cin >> s;
        int n = s.size();
        for (int i = 0; i < s.size(); ++i) {
            a[i] = s[i] - '0';
        }

        int i;
        for (i = 1; i < n; ++i) {
            if (a[i] < a[i-1]) 
                break;
        }
        int starter = 0;
        if (i < n)
        {
            int j;
            for (j = i; j > 0; --j)
                if (a[j] > a[j-1])
                    break;
            if (j > 0)
            {
                a[j]--;
                for (int k = j+1; k < n; ++k)
                    a[k] = 9;
            }
            else
            {
                a[0]--;
                for (int k = 1; k < n; ++k)
                    a[k] = 9;
                if (a[0] == 0) starter = 1;
            }
        }
        cout << "Case #" << I << ": ";
        for (int i = starter; i < n; ++i)
            cout << a[i];
        cout << endl;
    }
}
