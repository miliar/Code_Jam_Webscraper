#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <set>
#include <vector>
using namespace std;

bool istiny(long long no)
{
    int a = 10;
    while (no != 0)
    {
        int b = no%10;
        if (a < b) return false;
        a = b;
        no /= 10;
    }
    return true;
}

long long cal(long long no)
{
    int cnt = 0;
    while (1)
    {
        if (istiny(no)) break;
        no /= 10;
        no--;
        cnt++;
    }

    while (cnt--)
    {
        no *= 10;
        no += 9;
    }
    return no;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    long long T,TT;

    cin>>T;
    for(TT = 1; TT <= T; TT++)
    {
        long long no;
        cin>>no;
        cout<<"Case #"<<TT<<": "<<cal(no)<<endl;
    }

    return 0;
}
