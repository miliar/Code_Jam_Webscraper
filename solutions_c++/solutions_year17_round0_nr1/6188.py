#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::endl;

int main()
{
    int64_t T, size, k, count;
    bool flag;
    std::string s;
    cin >> T;
    std::vector<bool> pancake;
    std::string pattern = "Case #";
    std::string tmp;
    std::vector<int64_t> cnt;
    for (int64_t i = 0; i < T; ++i)
    {
        tmp = pattern;
        flag = true;
        count = 0;
        cin >> s >> k;
        size = s.size();
        pancake.assign(size, false);
        cnt.assign(size, 0);
        for (int64_t j = 0; j < size; ++j)
        {
            pancake[j] = ((s[j] == '+') ? true : false);
        }
        for (int64_t j = 0; j <= size - k; ++j)
        {
            if ((pancake[j] && cnt[j] % 2 != 0) || (!pancake[j] && cnt[j] % 2 == 0))
            {
                for (int64_t l = 0; l < k; ++l)
                    ++cnt[l + j];
                ++count;
            }
        }
        for (int64_t j = size - k + 1; j < size; ++j)
        {
            if ((pancake[j] && cnt[j] % 2 != 0) || (!pancake[j] && cnt[j] % 2 == 0))
            {
                flag = false;
                break;
            }
        }
        if (!flag)
        {
            tmp += std::to_string(i + 1);
            tmp += ": IMPOSSIBLE";
        }
        else
        {
            tmp += std::to_string(i + 1);
            tmp += ": ";
            tmp += std::to_string(count);
        }
        cout << tmp << endl;
    }
}
