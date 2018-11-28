#include <fstream>
using namespace std;

int main()
{
    ifstream cin ("A-large.in");
    ofstream cout ("A-large.out");

    int T(0);
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int R(0), C(0);
        char G[25][25] = {};
        cin >> R >> C;

        for (int j = 0; j < R; j++)
        {
            for (int k = 0; k < C; k++)
            {
                cin >> G[j][k];
            }
        }

        for (int j = 0; j < R; j++)
        {
            bool E(true);
            for (int k = 0; k < C; k++)
            {
                if (G[j][k] == '?')
                    continue;
                else
                {
                    E = false;
                    for (int l = k - 1; l >= 0; l--)
                    {
                        if (G[j][l] != '?')
                            break;
                        else
                            G[j][l] = G[j][k];
                    }
                    for (int l = k + 1; l < C; l++)
                    {
                        if (G[j][l] != '?')
                            break;
                        else
                            G[j][l] = G[j][k];
                    }
                }
            }

            if (E && j != 0)
                for (int k = 0; k < C; k++)
                    G[j][k] = G[j - 1][k];
        }

        int H(0);
        for (H = 0; H < R; H++)
            if (G[H][0] != '?')
                break;

        for (int j = 0; j < C; j++)
            for (int k = 0; k < H; k++)
                G[k][j] = G[H][j];

        cout << "Case #" << i + 1 << ":" << endl;
        for (int j = 0; j < R; j++)
        {
            for (int k = 0; k < C; k++)
            {
                cout << G[j][k];
            }
            cout << endl;
        }

    }

    cin.close();
    cout.close();
    return 0;
}
