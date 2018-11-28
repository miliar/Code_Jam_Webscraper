#include <fstream>
using namespace std;

int main()
{
    ifstream cin ("C-small-1-attempt0.in.txt");
    ofstream cout ("C-small-1-attempt0.out.txt");
    int T(0);
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int N(0);
        int K(0);
        cin >> N >> K;
        bool stalls[1002] = {};
        stalls[0] = true;
        stalls[N + 1] = true;

        for (int j = 0; j < K; j++)
        {
            int min_max(-1);
            int max_max(-1);
            int choice(-1);
            for (int k = 1; k <= N; k++)
            {
                if (stalls[k])
                    continue;

                int L_S(0);
                int R_S(0);

                for (int l = k - 1; l >= 1; l--)
                {
                    if (stalls[l])
                        break;
                    else
                        L_S++;
                }

                for (int l = k + 1; l <= N; l++)
                {
                    if (stalls[l])
                        break;
                    else
                        R_S++;
                }

                if (min(L_S, R_S) > min_max)
                {
                    min_max = min(L_S, R_S);
                    max_max = max(L_S, R_S);
                    choice = k;
                }
                else if (min(L_S, R_S) == min_max)
                {
                    if (max(L_S, R_S) > max_max)
                    {
                        max_max = max(L_S, R_S);
                        choice = k;
                    }
                }

                /*
                for (int k = 0; k <= N + 1; k++)
                    cout << stalls[k] << " ";
                cout << endl << L_S << " " << R_S << " " << choice << endl;
                */
            }

            stalls[choice] = true;

            if (j == K - 1)
                cout << "Case #" << i + 1 << ": " << max_max << " " << min_max << endl;
        }
    }

    cin.close();
    cout.close();

    return 0;
}
