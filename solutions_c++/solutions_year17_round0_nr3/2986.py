#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<set>
#include <bitset>
//#define cin in
//#define cout out
using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");


void printCase (int number)
{
    cout << "Case #" << number << ": ";
}

int main()
{
    int tests;
    cin >> tests;
    for (int i = 0; i < tests; i++)
    {
        printCase(i + 1);
        long long N, K, remK;
        cin >> N;
        cin >> K;
        remK = K;
        int level = 0;
        while (K > 1)
        {
            level++;
            K /= 2;
        }
        long long sum = N, meow = 1, bigger, smallerNum;
        for (int j = 0; j < level; j++)
            meow = meow * 2;
        sum = sum - meow + 1;
        bigger = sum % meow;
        smallerNum = sum / meow;
        if (remK - (meow - 1) > bigger)
            cout << smallerNum / 2 << " " << (smallerNum - 1) / 2 << endl;
        else
            cout << (smallerNum + 1) / 2 << " " << (smallerNum) / 2 << endl;
    }

    return 0;//Your program should return 0 on normal termination.
}
