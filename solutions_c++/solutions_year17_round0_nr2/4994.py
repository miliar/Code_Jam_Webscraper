#include <iostream>

using namespace std;

string prev_tidy(string& n)
{
    auto size = n.size();
    size_t i = 1;

    while (i < size and n[i - 1] <= n[i])
        ++i;

    if (i == size)
        return n;

    while (i > 0 and n[i - 1] > n[i])
    {
        n[i - 1]--;
        --i;
    }

    for (size_t j = i + 1; j < size; ++j)
        n[j] = '9';

    return n;
}

int main()
{
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test)
    {
        string n;
        cin >> n;

        cout << "Case #" << test << ": " << stoll(prev_tidy(n)) << endl; 
    }

    return 0;
}    
