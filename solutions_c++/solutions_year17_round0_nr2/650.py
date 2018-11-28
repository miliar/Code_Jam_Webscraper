#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for(int casenum = 1;casenum<=t;casenum++)
    {
        string a;
        cin  >> a;
        unsigned first_change = 0;
        while(a[first_change] <= a[first_change+1] and first_change < a.size() - 1)
        {
            first_change++;
        }
        //case already solved
        if(first_change == a.size() - 1)
        {
            //answer is correct
        }
        else if(a[first_change] == '1')
        {
            a[0] ='0';
            for(unsigned i = 1;i<a.size();i++)
            {
                a[i] = '9';
            }
        }
        else
        {
            //go back to first 9
            char k = a[first_change];
            while(a[first_change] == k and first_change >= 0)
            {
                first_change--;
            }
            first_change++;
            a[first_change]--;
            for(unsigned i = first_change+1;i<a.size();i++)
            {
                a[i] = '9';
            }
        }
        if(a[0] == '0')
        {
            a.erase(0,1);
        }
        cout << "Case #" << casenum << ": ";
        cout << a << endl;


    }
    return 0;
}
