#include <iostream>
#include <cstring>
#include <fstream>

#define RUE(a, b, i) for(int (i)=(a) ; (i)<(b) ; (i)++) //run until end
#define BTB(a, b, i) for(int (i)=(a) ; (i)>=(b) ; (i)--) //back to begin
#define AR(a, i) RUE(0, (a), (i)) //all run

using namespace std;

bool check(int n);

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    fstream f, out;
    int t;
    int n;
    int o[100+10];
    bool flag;

    f.open("B-small-attempt1.in", ios::in);
    f >> t;
    AR(t, i)
    {
        f >> n;
        flag = false;
        while(n)
        {
            flag = check(n);
            if(flag) break;
            n--;
        }
        o[i] = n;
    }
    f.close();
    out.open("out.txt",ios::out);
    AR(t, i)
    {
        out << "case #";
        out << i+1 << ": ";
        out << o[i] << endl;
    }
}

bool check(int n)
{
    int l = n%10;
    n /= 10;
    while(n)
    {
        if(n%10 > l) return false;
        else
        {
            l = n%10;
            n /= 10;
        }
    }
    return true;
}
