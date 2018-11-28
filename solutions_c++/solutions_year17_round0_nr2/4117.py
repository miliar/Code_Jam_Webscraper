#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; kase++)
    {
        cout << "Case #" << kase << ": ";
        string a;
        cin >> a;
        int l = -1;
        for (int i = 0; i < a.length()-1; ++i)
        {   if (a[i] > a[i+1])
            {
                l = i;
                break;
            }
        }
        if (l == -1) cout << a << endl;
        else 
        {   
            int i = 0;
            for (i = l; i > 0; i--)
                if (a[i-1] < a[i])
                {   break; }
            a[i] = a[i]-1;
            for (int j = i+1; j < a.length(); ++j)
                a[j] = '9';
            for (i = 0; i < a.length() && a[i] == '0'; ++i);
            for (; i < a.length(); ++i) cout << a[i];
            cout << endl;
        }   
    }
}
