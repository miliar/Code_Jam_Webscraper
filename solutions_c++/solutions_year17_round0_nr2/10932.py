#include<iostream>
#include<fstream>
using namespace std;

ifstream fin ("B-small-attempt0.in");
ofstream fout ("B-small-attempt0.out");

bool isTidy (long long int n)
{
    long long int holder1, holder2;
    for (long long int i = 0; n > 9; i++)
    {
        holder1 = n % 10;
        holder2 = (n / 10) % 10;
        if (holder2 > holder1)
            return false;
        n /= 10;
    }
    return true;
}

int main()
{
    long long int t, n;
    fin >> t;
    for (long long int i = 0; i < t; i++)
    {
        fin >> n;
        for (long long int k = n; k > 0; k--)
        {
            if (isTidy(k))
            {
                fout << "Case #" << i + 1 << ": " << k << endl;
                break;
            }
        }
    }
}
