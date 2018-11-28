#include <iostream>
#include <string>

typedef uint64_t llu;
typedef int64_t ll;

using namespace std;

int main()
{
    llu n;
    cin >> n;

    for (llu c = 0; c < n; c++)
    {
        llu num = 0;
        cin >> num;

        // check digits from front to last
        string ans = to_string(num);
        
        for (int i = ans.size() - 2; i >= 0; i--)
        {
            if (ans[i] > ans[i + 1] || 
                (ans[i] == '0' && ans[i+1] == '0'))
            {
                // fill with 9s
                for (int j = i+1; j < ans.size(); j++)
                {
                    ans[j] = '9';
                }

                if (ans[i] > '0')
                {
                    ans[i] = ans[i] - 1;
                }
            }
        }

        if (ans[0] == '0')
        {
            ans = ans.substr(1, ans.size() - 1);
        }

        cout << "Case #" << c + 1 << ": " << ans << endl;
    }
    return 0;
}