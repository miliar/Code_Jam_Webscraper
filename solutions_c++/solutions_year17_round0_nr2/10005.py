#include<iostream>
#include<vector>
#include <string>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        int r;
        int max = 1;
        for (int j = 1; j <= n; j++)
        {
            
            int test = j;
            vector<int> v;
            while (test != 0)
            {
                r = test % 10;
                test = test / 10;
                v.push_back(r);
            }
            bool tidy = true;
            for (unsigned int k = 1; k < v.size(); k++)
            {
                if (v[k- 1] < v[k])
                    tidy = false;
            }
            if (tidy == true && j > max)
                max = j;
        }
        cout << "Case #" << i + 1 << ": " << max << endl;
    }

    return 0;
}


