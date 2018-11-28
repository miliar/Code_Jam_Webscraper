#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("B-small-attempt0.in");
    f2.open("B-small-attempt0.out");
    int t = 0 ;
    long long int n = 0, i = 1 , temp = 0, num = 0 , a = 0;
    f1 >> t;
    while(t)
    {
        f1 >> n;
        while(n >= 10)
        {
            temp = n;
            num = temp %10;
            a = num;
            while(temp != 0)
            {
                num = temp % 10;
                if(a < num)
                    break;
                else
                {
                    temp = temp / 10;
                    a = num;
                }
            }
            if(temp == 0)
                break;
            else
                n--;
        }
        f2 << "Case #" << i << ": " << n << endl;
        i++;
        t--;
    }
    return 0;
}
