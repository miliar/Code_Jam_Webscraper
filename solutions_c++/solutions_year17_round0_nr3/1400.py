#include <bits/stdc++.h>

#define mp make_pair

typedef std::pair<int, int> pii;

void get_ans(long long int n, long long int k)
{
    std::set<long long int> segm;
    std::map<long long int, long long int> mp;
    segm.insert(n);
    mp[n] = 1;
    long long int memk = k;
    while (memk > 0)
    {
        long long int len = *(--segm.end());;
        segm.erase(--segm.end());
        long long int cnt = mp[len];
        long long new_len1 = (len - 1) / 2;
        long long new_len2 = len / 2;
        if (mp.count(new_len1))
            mp[new_len1] += cnt;
        else
        {
            mp[new_len1] = cnt;
            segm.insert(new_len1);
        }
        if (mp.count(new_len2))
            mp[new_len2] += cnt;
        else
        {
            mp[new_len2] = cnt;
            segm.insert(new_len2);
        }
        if (cnt >= memk)
            std::cout << new_len2 << " " << new_len1 << "\n";
        memk -= cnt;        
    }
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int w;
    scanf("%d", &w);
    w = 0;
    long long int n, k;
    while (std::cin >> n >> k)
    {
        printf("Case #%d: ", ++w);
        get_ans(n, k);
    }
    return 0;
}