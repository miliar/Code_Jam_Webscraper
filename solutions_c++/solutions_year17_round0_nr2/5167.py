#include <bits/stdc++.h>

using namespace std;

bool tidy(int n)
{
    if(n == 1) return true;
    vector<int> nums;
    while(n)
    {
        nums.push_back(n%10);
        n/=10;
    }

    for(int i = 0;i < nums.size()-1; i++)
    {
        if(nums[i] < nums[i+1]) return false;
    }
    return true;
}

int main()
{
    int c; cin >> c;
    for(int t = 1; t <= c; t++)
    {
        int num; cin >> num;

        while(!tidy(num)) num--;
        printf("Case #%d: %d\n", t, num);
    }
    return 0;
}
