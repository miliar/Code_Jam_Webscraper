#include <iostream>

using namespace std;

#define FALSE   0
#define TRUE    1

#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <stdint.h>

using namespace std;

class tidyNum
{
private:
    char strV[256];
    int size;

    int getN(char c);
    void setMinus(int i);
    void setNine(int i);
    void printN();
    void solve1();
    int check();
public:
    tidyNum(uint64_t n);
    virtual ~tidyNum();

    string solve();
};


int tidyNum::getN(char c)
{
    char tmp[2] = {0,};
    tmp[0] = c;

    return atoi(tmp);
}

void tidyNum::setMinus(int i)
{
    char tmp[2] = {0,};
    tmp[0] = strV[i];

    int n = atoi(tmp);
    sprintf(tmp, "%d", n-1);

    strV[i] = tmp[0];
}

void tidyNum::setNine(int i)
{
    char tmp[2] = {0,};
    sprintf(tmp, "%d", 9);

    for(int j = i; j < size; j++)
        strV[j] = tmp[0];
}

void tidyNum::solve1()
{
    int i;
    for(i = 0; i < size - 1; i++)
    {
        int n1, n2;
        n1 = getN(strV[i]);
        n2 = getN(strV[i+1]);

        if(n1 > n2)
        {
            setMinus(i);
            setNine(i+1);
            break;
        }
    }
}

int tidyNum::check()
{
    int i;
    for(int i = 0; i < size - 1; i++)
    {
        int n1, n2;
        n1 = getN(strV[i]);
        n2 = getN(strV[i+1]);

        if(n1 > n2)
        {
            return FALSE;
        }
    }
    return TRUE;
}

tidyNum::tidyNum(uint64_t n)
    : size(0)
{
    sprintf(strV, "%lu", n);
    size = strlen(strV);
}

tidyNum::~tidyNum()
{

}

string tidyNum::solve()
{

    while(1)
    {
        solve1();
        if(check() == TRUE)
            break;
    }

    string ans("");
    for(int j = 0; j < size; j++)
    {
        if(j == 0 && strV[j] == '0')
            continue;
        char t[2] = {0,};
        t[0] = strV[j];
        ans.append(t);
    }
    return ans;
}

int main()
{
    int t;
    uint64_t n;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> n;
        tidyNum tn(n);
        cout << "Case #" << i << ": " << tn.solve() << endl;
    }
    return 0;
}

