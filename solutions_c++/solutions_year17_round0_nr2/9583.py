#include <iostream>
#include <string>
#include <vector>

using namespace std;

string flips(const char* input)
{
    vector<int> temp;
    vector<char> ans;
    int wrong = 0;
    int diff_index = 0;

    for (int i = 0; input[i] != '\0'; ++i)
        temp.push_back(input[i] - 48);

    int length = (int) temp.size();
    if (length == 1) return input;

    for (int i = length - 1; i != 0; --i)
    {
        if (temp[i - 1] >= temp[i])
        {
            diff_index = i;
            if(temp[i - 1] > temp[i])
                wrong++;
        }
    }

    if (wrong == 0) return input;

    temp[diff_index - 1] = temp[diff_index - 1] - 1;
    for (int i = diff_index; i < length; ++i)
        temp[i] = 9;

    for (int i = 0; i < length; ++i)
        ans.push_back((char) (temp[i] + 48));

    if (ans[0] == 48)
        ans.erase(ans.begin());

    string str(ans.begin(), ans.end());

    return str;
}

int main()
{
    int tests = 0;
    string number;
    string maximum;

    cin >> tests;

    for (int i = 1; i <= tests; ++i)
    {
        cin >> number;
        maximum = flips(number.c_str());
        printf("Case #%d: %s\n", i, maximum.c_str());
    }

    return 0;
}
