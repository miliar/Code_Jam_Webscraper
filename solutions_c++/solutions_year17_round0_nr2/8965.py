#include <fstream>
using namespace std;

bool is_tidy(long long int n)
{
    bool result = true;

    while (n >= 10)
    {
        int last = n % 10;
        long long int next_n = n / 10;
        int second_last = next_n % 10;
        if (last >= second_last)
        {
            n = next_n;
            continue;
        }
        else
        {
            result = false;
            break;
        }
    }

    return result;
}

int main()
{
    ifstream cin ("B-small-attempt0.in.txt");
    int T(0);
    cin >> T;
    long long int max_tidy[100] = {};
    int max_tidy_count(0);
    for (int i = 0; i < T; i++)
    {
        long long int N(0LL);
        cin >> N;
        for (long long int j = N; j > 0; j--)
        {
            if (is_tidy(j))
            {
                max_tidy[max_tidy_count++] = j;
                break;
            }
        }
    }
    cin.close();

    ofstream cout ("B-small-attempt0.out.txt");
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": " << max_tidy[i] << endl;
    }
    cout.close();

    return 0;
}
