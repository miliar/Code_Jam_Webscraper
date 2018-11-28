#include <iostream>
#include <cstdio>
#include <math.h>
#include <fstream>

#define f0(i,n) for(int i = 0; i < n; i++)
#define f1(i,n) for(int i = 1; i <= n; i++)

using namespace std;

bool isTidyNumber(int num)
{
    if(num == 0)
    {
        return true;
    } else {
        if((num % 10) >= (int(floor(num/10))%10)){
            isTidyNumber(floor(num/10));
        } else {
            return false;
        }
    }

}

int main()
{
    int cases;
    cin >> cases;

    f1(cases_i,cases)
    {
        int num;
        cin >> num;
        printf("Case #%d: ",cases_i);
        //Processing
        while(!isTidyNumber(num))
        {
            num--;
        }

        cout << num << endl;
    }
}
