#include <iostream>
#include <fstream>

using namespace std;


bool isTidy(int n)
{
    int lastDigit = n%10;
    n /= 10;
    while(n > 0)
    {
        if(lastDigit < n%10)
            return false;
        lastDigit = n%10;
        n /= 10;
    }

    return true;
}
int main()
{
    ofstream output("B-small-attempt0.out");
    ifstream input("B-small-attempt0.in");
    int T;
    input>>T;

    cout<<"Begin !"<<endl;
    for(int t = 0; t < T; t++ )
    {
        output<<"Case #"<<t+1<<": ";
        int n;
        input>>n;

        while(n > 0 && !isTidy(n))
        {
            n--;
        }
        if(n > 0)
        {
            output<<n<<endl;
        }
    }
    return 0;
}

