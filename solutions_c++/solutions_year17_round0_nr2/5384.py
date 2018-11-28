#include <iostream>
#include <stdio.h>
using namespace std;

long long findNum(long long num, long long start, long long N, long long maxNum)
{
    if(num > N)
        return -1;
    if(num > maxNum)
        maxNum = num;
    for(long long i = start; i <= 9; i++){
        maxNum = max(maxNum, findNum(num*10 + i, i, N, maxNum));
    }
    return maxNum;
}


int main()
{
    int T;
    long long N;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> N;
        cout << "Case #" << i+1 << ": " << findNum(0, 1, N, 0) << endl;
    }
    return 0;
}
