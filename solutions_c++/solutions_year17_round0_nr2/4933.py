#include <iostream>
#include <vector>
#include <sstream>

using namespace  std;

int main()
{
    int T;
    cin >> T;
    for (int test = 1; test < T + 1; ++test)
    {
//        int N;
//        cin >> N;

//        int ans = 1;
//        for (int i = 1; i < N + 1; ++i)
//        {
//            stringstream ss;
//            ss << i;
//            string s = ss.str();
//            bool f = true;
//            for (int j = 0; j + 1 < (int) s.length(); ++j)
//            {
//                if (s[j] > s[j + 1])
//                {
//                    f = false;
//                    break;
//                }
//            }
//            if (f)
//            {
//                ans = i;
//            }
//        }

//        cout << "Case #" << test << ": " << ans << endl;

        string s;
        cin >> s;
        vector<int> a(s.length());
        cout << "Case #" << test << ": ";
        int zero = (int) s.length();

        for (int i = 0; i < (int) s.length(); ++i)
        {
            a[i] = static_cast<int>(s[i] - '0');
            if (a[i] == 0)
            {
                zero = i;
            }
        }

        int index = -1;
        for (int i = 1; i < (int) a.size(); ++i)
        {
            if (a[i - 1] > a[i])
            {
                index = i;
                break;
            }
        }

        if (index == -1)
        {
            cout << s << endl;
            continue;
        }

        for (int i = 0; i < index; ++i)
        {
            if (a[i] == a[index - 1])
            {
                index = i + 1;
                break;
            }
        }

        int j = index - 1;
        for (; j > -1; --j)
        {
            if (a[j] > 1)
            {
                break;
            }
        }
        if (j > -1)
        {
            a[j]--;

            for (int i = 0; i < j + 1; ++i)
                cout << a[i];
            for (int i = j + 1; i < (int) a.size(); ++i)
                cout << 9;
        }
        else
        {
            for (int i = 0; i + 1 < (int) a.size(); ++i)
            {
                cout << 9;
            }
        }
        cout << endl;
    }
}
