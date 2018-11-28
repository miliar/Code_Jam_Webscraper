//
//  main.cpp
//  cppsample
//
//  Created by 刘颖珊 on 2017/4/6.
//  Copyright © 2017年 刘颖珊. All rights reserved.
//

#include <iostream>

using namespace std;


long long tidy_number(long long max_number)
{
    long long x = max_number;
    long long exp = 1;
    long long result = max_number;
    long long negative = 0;
    while (x > 0)
    {
        long long last_number = x % 10 + negative;
        long long second_last_number = x % 100 / 10;
        exp *= 10;
        if (second_last_number > last_number)
        {
            negative = -1;
            result = max_number / exp * exp - 1;
        }
        else
        {
            negative = 0;
        }
        x /= 10;
    }
    return result;
}

void problemB()
{
    freopen("b_large_in.txt","r",stdin);
    freopen("b_large_out.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        long long x;
        cin >> x;
        cout << "Case #" << i + 1 << ": " << tidy_number(x) << endl;
    }
}

int main(int argc, const char * argv[])
{
    problemB();
    return 0;
}

