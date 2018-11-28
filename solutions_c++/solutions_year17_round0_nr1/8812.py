#include <fstream>
#include <cstring>
#include <math.h>
#include <limits.h>
using namespace std;

int main()
{
    ifstream cin ("A-small-attempt0.in.txt");
    ofstream cout ("A-small-attempt0.out.txt");

    int T(0);
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        char pancakes[10] = {};
        int K(0);
        int S(0);
        cin >> pancakes >> K;
        for (int j = 0; j <= 10; j++)
        {
            if (pancakes[j] == '+' || pancakes[j] == '-')
                continue;
            else
            {
                S = j;
                break;
            }
        }

        //cout << S << " " << K << endl;
        int num_states = pow(2, (S - K + 1));
        bool feasible[512] = {};

        for (int j = 0; j < num_states; j++)
        {
            //cout << j << endl;
            char tmp[10] = {};
            memcpy(tmp, pancakes, 10);
            int p(0);

            for (int k = j; k > 0; k /= 2)
            {
                if (k % 2 == 1)
                {
                    for (int l = p; l < p + K; l++)
                    {
                        if (tmp[l] == '+')
                            tmp[l] = '-';
                        else if (tmp[l] == '-')
                            tmp[l] = '+';
                    }
                }
                p++;
            }

            /*
            for (int k = 0; k < 10; k++)
                cout << tmp[k] << " ";
            cout << endl;
            */

            bool flag(true);
            for (int k = 0; tmp[k] == '+' || tmp[k] == '-'; k++)
            {
                if (tmp[k] == '-')
                {
                    flag = false;
                    break;
                }
            }
            if (flag)
                feasible[j] = true;
        }

        int min_flips = INT_MAX;

        for (int j = 0; j < num_states; j++)
        {
            if (feasible[j])
            {
                int sum(0);
                for (int k = j; k > 0; k /= 2)
                    sum = sum + k % 2;
                if (sum < min_flips)
                    min_flips = sum;
            }
        }

        if (min_flips < INT_MAX)
            cout << "Case #" << i + 1 << ": " << min_flips << endl;
        else
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }

    cin.close();
    cout.close();

    return 0;
}
