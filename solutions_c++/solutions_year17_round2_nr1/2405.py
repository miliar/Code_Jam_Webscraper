#include<iostream>
#include<cmath>
#include<vector>
#include<fstream>
#include<algorithm>
#include<iomanip>
//#define cin in
//#define cout out
using namespace std;



ifstream in("input.txt");
ofstream out("output.txt");

void printCase(int caseNum)
{
    cout << "Case #" << caseNum << ": ";
}

int main()
{
    int test;
    cin >> test;
    for (int i = 0; i < test; i++)
    {
        printCase(i + 1);
        long long d, h, di, si;
        double maxTime = 0.0;
        cin >> d >> h;
        for (int i = 0; i < h; i++)
        {
            cin >> di >> si;
            if ((((double)(d - di))/si) > maxTime)
                maxTime = ((double)(d - di))/si;
        }
        cout << setprecision(6) << fixed << (double)d / maxTime << endl;
    }
    return 0;
}

