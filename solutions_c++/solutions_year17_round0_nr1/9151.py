#include <iostream>
#include <string>
#include <vector>

using namespace std;

// +: 43
// -: 45
int flips(const char* input, int flip_size)
{
    int count = 0;
    vector<int> temp;

    for (int i = 0; input[i] != '\0'; ++i)
        temp.push_back(input[i] - 44);

    int pancakes = (int) temp.size();

    for (int i = 0; i <= pancakes - flip_size; ++i)
    {
        if (temp[i] == 1)
        {
            for (int j = 0; j < flip_size; ++j)
            {
                temp[i + j] *= -1;
            }
            count++;
        }
    }

    for (int i = pancakes - flip_size; i < pancakes; ++i)
        if (temp[i] == 1) return -1;

    return count;
}

int main()
{
    int tests = 0;
    string pancakes;
    int flip_size;
    int count;

    cin >> tests;

    for (int i = 1; i <= tests; i++)
    {
        cin >> pancakes >> flip_size;
        count = flips(pancakes.c_str(), flip_size);
        if (count == -1)
            printf("Case #%d: IMPOSSIBLE\n", i);
        else
            printf("Case #%d: %d\n", i, count);
    }

    return 0;
}
