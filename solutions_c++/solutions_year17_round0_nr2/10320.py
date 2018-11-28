#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int solve(int n)
{
    if (n < 10)
        return n;

    for (int i = n; i > 0; i--)
    {
        vector<int> vec;
        string number = to_string(i);

        for (int j = 0; j < number.length(); j++)
            vec.push_back(number[j] - '0');

        int x = 0;

        for (int k = 0; k < vec.size() - 1; k++)
        {
            if (vec[k] <= vec[k + 1])
                x++;
        }

        if (x == vec.size() - 1)
            return i;
    }
}

int main() {

    ifstream infile("input");

    int cases, num;
    infile >> cases;
    for (int i = 1; i <= cases; i++) {
        infile >> num;
        cout << "Case #" << i << ": " << solve(num) << endl;
    }

    return 0;
}