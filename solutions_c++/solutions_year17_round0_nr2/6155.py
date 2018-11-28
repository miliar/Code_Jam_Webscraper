#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::endl;

std::string solve(std::string &num)
{
    int64_t size = num.size();
    if (size == 1)
    {
        return num;
    }
    bool flag = false;
    for (int64_t i = 1; i < size; ++i)
    {
        if (num[i] < num[i-1])
        {
            flag = true;
            break;
        }
    }
    if (!flag)
    {
        return num;
    }
    flag = false;
    int64_t i;
    for (i = 1; i < num.size(); ++i)
    {
        if (num[i] <= num[i-1])
        {
            flag = true;
            break;
        }
    }
    if (!flag)
    {
        return num;
    }
    if (i == 1 && num[0] == '1')
    {
        std::string tmp(size - 1, '9');
        return tmp;
    }
    else
    {
        num[i-1] -= 1;
        for (int64_t j = i; j < size; ++j)
            num[j] = '9';
        return num;
    }
}

int main()
{
    int64_t T;
    std::string num;
    cin >> T;
    std::string pattern = "Case #";
    std::string tmp;
    for (int64_t i = 0; i < T; ++i)
    {
        cin >> num;
        tmp += pattern;
        tmp += std::to_string(i + 1);
        tmp += ": ";
        tmp += solve(num);
        cout << tmp << endl;
        tmp.clear();
    }
}
