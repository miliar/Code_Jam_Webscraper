#include <iostream>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, k;
        cin >> n >> k;
        set< pair<int, int> > S;
        S.insert({-n, 1});
        int a, b;
        for (int j = 0; j < k; ++j)
        {
            pair<int, int> x = *S.begin();
            S.erase(S.begin());
            x.first *= -1;
            if (x.first % 2 == 0)
            {
                S.insert({-(x.first / 2 - 1), x.second});
                S.insert({-(x.first / 2), x.second + (x.first / 2)});
                if (j == k - 1)
                {
                    a = x.first / 2;
                    b = x.first / 2 - 1;
                }
            }
            else
            {
                S.insert({-(x.first / 2), x.second}) ;
                S.insert({-(x.first / 2), x.second + (x.first / 2 + 1)});
                if (j == k - 1)
                {
                    a = x.first / 2;
                    b = x.first / 2;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << a << " " << b << endl;
    }
    return 0;
}
