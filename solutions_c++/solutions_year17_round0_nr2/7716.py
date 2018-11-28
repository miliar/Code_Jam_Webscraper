#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

string reflux(int startIndex, string targetNumber)
{
    int len = targetNumber.size();
    for(int i=startIndex; i<len; i++)
    {
        if(targetNumber[i]!='9')
        {
            targetNumber[i] = '9';
        }
    }
    return targetNumber;
}
string getMainNumber(string number)
{
    int len = number.size();
    bool foundfirstNumber = false;
    for(int i=0; i<len; i++)
    {
        if(!foundfirstNumber && number[i]!='0')
        {
            number = number.substr(i);
            break;
        }
    }
    return number;
}
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int z = 1; z <= t; z++) {
        string number;
        cin >> number;
        printf("Case #%d: ", z);
        int len = number.size();
        for(int i=len-1; i>0; i--)
        {
            if(number[i-1]>number[i])
            {
                number = reflux(i, number);
                number[i-1] = (number[i-1] - '0' - 1) + '0';
            }
        }
        cout << getMainNumber(number) << endl;
    }
}

