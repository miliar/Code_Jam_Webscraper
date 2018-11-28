#include <iostream>

#define FALSE   0
#define TRUE    1

#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <stdint.h>
#include <unistd.h>
using namespace std;

class pancakes
{
private:
    char v[1000];
    int size;
    int k;
    int count;

    void printV();
    int findBlank();
    int find(int n);
    void change(int pos, int n);
    int change(int n);
public:
    pancakes(const string & p, int kn);
    virtual ~pancakes();

    string solve();
};


void pancakes::printV()
{
    for(int i = 0; i < size; i++)
        printf("%c", v[i]);
    printf("\n");
}

int pancakes::findBlank()
{
    for(int i = 0; i < size; i++)
    {
        if(v[i] == '-')
        {
            return i;
        }
    }

    return -1;
}

int pancakes::find(int n)
{
    for(int i = 0; i <= size - n; i++)
    {

    }
    return 0;
}

void pancakes::change(int pos, int n)
{
    for(int i = pos; i < pos + n; i++)
    {
        if(v[i] == '-')
            v[i] = '+';
        else
            v[i] = '-';
    }
    count += 1;
}

int pancakes::change(int n)
{
    while(1)
    {
        int pos = findBlank();
        if(pos < 0)
            return TRUE;

        if(pos > size - n)
            return FALSE;

        change(pos,n);

    }
}

pancakes::pancakes(const string &p, int kn)
    : count(0)
{
    memcpy(v, p.c_str(), p.length());
    size = p.length();
    k = kn;
}

pancakes::~pancakes()
{

}

string pancakes::solve()
{
    string ans("1");

    if(change(k) == FALSE)
    {
        ans = "IMPOSSIBLE";
    }
    else
    {
        char tmp[32];
        sprintf(tmp, "%d", count);
        ans = tmp;
    }

    return ans;
}

int main()
{
    int t, n;
    string s;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s >> n;
        pancakes pc(s, n);
        cout << "Case #" << i << ": " << pc.solve() << endl;
    }
    return 0;
}
