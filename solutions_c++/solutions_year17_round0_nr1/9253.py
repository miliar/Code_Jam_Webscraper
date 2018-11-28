#include <iostream>
using namespace std;

void Reverse(string& input, size_t pos, int K)
{
    for (int i = pos; i< pos+K; i++)
    {
        if (input[i] == '+')
        {
            input[i] = '-';
        }
        else
        {
            input[i] = '+';
        }
    }
}

void Process(string& input, int K, int c)
{
    cout << "Case #" << c << ": ";
    size_t it = input.find_first_of('-');
    if (it == string::npos)
    {
        cout << 0 << endl;
        return;
    }
    int n = 0;
    do
    {
        if (it != string::npos && (K > input.size() || it + K > input.size()))
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        Reverse(input, it, K);
        n++;
        it = input.find_first_of('-', it+1);
    } while (it != string::npos);
    cout << n << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        string input;
        int K;
        cin >> input >> K;
        Process(input, K, i);
    }
    return 0;
}
