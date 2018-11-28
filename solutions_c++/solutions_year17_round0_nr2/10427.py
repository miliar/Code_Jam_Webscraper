#include <iostream>

using namespace std;

bool areSorted(long int n)
{
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}

int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        unsigned long long int n;
        cin >>n;
        unsigned long long int j=n;
        while (j){

            if (areSorted(j)){
                cout <<"Case #"<<i<<": "<<j<<"\n";
                break;
            }

            j--;
        }
    }
    return 0;
}
