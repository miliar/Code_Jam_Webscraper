#include <cstring>
#include <fstream>

using namespace std;

//bool isTidy(int n)
//{
//    int lastDigit = n % 10;
//    n /= 10;
//    while(n > 0)
//    {
//        if (n % 10 > lastDigit)
//            return false;
//        lastDigit = n % 10;
//        n /= 10;
//    }
//    return true;
//}
//
//void generateNumbers()
//{
//    int p = 10;
//    int lastVal = 0;
//    int number = 0;
//    for (int i = 0; i < 1000000000; i++)
//    {
//        if (i == p)
//        {
//            cout << "Under " << p << ": " << number << "; " << number - lastVal << "\n";
//            p *=10;
//            lastVal = number;
//        }
//        if (isTidy(i))
//            number++;
//    }
//}

char number[21];

int computeTidyNumberUnder(char number[], int l)
{
    int i = 0;
    while (i < l - 1) {
        for (i = 0; i < l - 1; i++) {
            if (number[i] > number[i + 1]) {
                number[i]--;
                for (int j = i + 1; j < l; j++) {
                    number[j] = '9';
                }
                break;
            }
        }
    }
}

int main()
{
    ifstream f("tidy.in");
    ofstream g("tidy.out");
    int t, l, j;
    f >> t;
    for (int i = 0; i < t; i++)
    {
        f >> number;
        l = strlen(number);
        computeTidyNumberUnder(number, l);
        j = 0;
        while (j < l && number[j] == '0')
            j++;
        g << "Case #" << i + 1 << ": " << number + j << '\n';
    }
    f.close();
    g.close();
    return 0;
}