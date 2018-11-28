#include <iostream>
#include <fstream>

using namespace std;

#define INF 10000000000000000001

int t;
unsigned long long int n;

unsigned long long int v[6906901];
unsigned long long int k = 0;
void gen(long long int p = 0, long long int s = 0, long long int n = 19)
{
    if (n == 0)
        v[k++] = p;
    else
        for(int i=s;i<10;i++)
            gen(10*p+i, i, n-1);
}

unsigned long long int binsearch(const unsigned long long int* v, const unsigned long long int sz, const unsigned long long int val)
{
    unsigned long long int s = 1;
    unsigned long long int d = sz;
    unsigned long long int mij;

    while(s<=d)
    {
        mij = (s+d)/2;

        if(v[mij] == val)
            return val;

        if(val > v[mij])
            s = mij+1;
        else
            d = mij-1;
    }

    while(v[mij] > val) mij--;

    return v[mij];
}

int main()
{
    cout << "Hello world!" << endl;

    ifstream f("date.in");
    ofstream g("date.out");

    gen();
    //cout << k;

    f >> t;
    for(int i = 1; i <= t; i++)
    {
        f >> n;
        g << "Case #" << i << ": " << binsearch(v,k,n) << '\n';
    }

    return 0;
}
