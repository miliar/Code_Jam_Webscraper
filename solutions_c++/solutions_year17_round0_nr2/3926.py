#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    ifstream input;
    ofstream output;
    input.open("data/B-large.in");
    output.open("data/B-large.out");
    input >> n;
    for (int test = 0; test < n; test++)
    {
        long long num;
        input >> num;
        int len = (int) floor(log10(num)) + 1;
        int arr[len];
        for (int i = 0; i < len; i++)
        {
            arr[len - i - 1] = num % 10;
            num /= 10;
        }

        for (int i = len - 2; i >= 0; i--)
        {
            if (arr[i] > arr[i + 1])
            {
                arr[i]--;
                for (int j = i + 1; j < len; j++)
                {
                    arr[j] = 9;
                }
            }
        }

        output << "Case #" << (test + 1) << ": ";
        for (int i = 0; i < len; i++)
        {
            if (i != 0 || arr[i] != 0)
                output << arr[i];
        }
        output << endl;
    }
}
