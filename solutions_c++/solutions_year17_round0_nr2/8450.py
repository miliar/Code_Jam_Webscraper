#include <bits/stdc++.h>

using namespace std;

int checkIfTidyNumber(char input[20], const int& size)
{
    ///cout << "input = {" << input << "}\n";
    for (int ind = 0; ind < size - 1; ++ind)
        if (input[ind] > input[ind + 1])
            return ind;
    return -1;
}

long long int getLargestTidyNumber(char input[20], const int& size)
{
    int index = checkIfTidyNumber(input, size);
    ///cout << "index = " << index << endl;
    if (index != -1)
    {
        while ((index > 0) && (input[index - 1] == input[index])) --index;
        --input[index];
        for (++index; index < size; ++index)
            input[index] = '9';
    }
    long long int ret = 0;
    for (int ind = 0; ind < size; ++ind)
        ret = ret * 10 + (input[ind] - '0');
    return ret;
}

int main()
{
    int numberOfTests;
    char input[20];
    scanf("%d", &numberOfTests);
    for (int test = 1; test <= numberOfTests; ++test)
    {
        scanf("%s", &input);
        printf("Case #%d: %lld\n", test, getLargestTidyNumber(input, strlen(input)));
    }

	return 0;
}
