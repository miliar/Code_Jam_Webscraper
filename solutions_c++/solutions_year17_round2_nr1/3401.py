#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <stdint.h>

using namespace std;

#define STATIC_TEST 0

#define FALSE   0
#define TRUE    1

class aRound2
{
private:
    int d;
    double maxt;
public:
    aRound2(int dest);
    virtual ~aRound2();

    void set(int d1, int k);
    string solve();
};

aRound2::aRound2(int dest)
    : maxt(0)
{
    d = dest;
//    cout << "dest: " << d << endl;
}

aRound2::~aRound2()
{

}

void aRound2::set(int di, int ki)
{
    int dt = d - di;
    double t = (double)dt / ki;

    if(maxt < t)
        maxt = t;
//    cout << "maxt " << maxt << endl;
}

string aRound2::solve()
{
    string a;
    char tmp[64];

    double t = (double)d / maxt;
    sprintf(tmp, "%lf", t);
    a = tmp;

    return a;
}

int main()
{
    int t;
    int d, n;
    int ki, di;

#if STATIC_TEST
    t = 1;
#else
    cin >> t;
#endif
    for (int i = 1; i <= t; ++i)
    {

#if STATIC_TEST
        cin >> d >> n;

        aRound2 r(d);

        cout << d << " " << n << endl;
        for(int j = 0; j < n; j++)
        {
            cin >> di >> ki;
            cout << di << " " << ki << endl;
//            r.set(di, ki);
        }
#else
        cin >> d >> n;

        aRound2 r(d);

//        cout << d << " " << n << endl;
        for(int j = 0; j < n; j++)
        {
            cin >> di >> ki;
//            cout << di << " " << ki << endl;
            r.set(di, ki);
        }
#endif

        cout << "Case #" << i << ": " << r.solve() << endl;
    }
    return 0;
}

