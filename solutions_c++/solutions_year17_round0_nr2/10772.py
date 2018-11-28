#include<fstream>
#include<iostream>

using namespace std;

int tidy_check(int n)
{
    int rem1, rem2;

    do
    {
        rem1 = n%10;
        n /= 10;
        rem2 = n%10;

        if(rem1 < rem2)
        {
            return 0;
        }
    }while(n > 0);

    return 1;
}

int main()
{
    int t, number, tidy;

    ifstream input;
    ofstream output;

    input.open("B-small-attempt0.in",ios::in);
    output.open("tidy.out",ios::out | ios::trunc);

    input>>t;

    if(input.is_open())
    {
        for(int i=0; i<t; i++)
        {
            input >> number;

            while(1)
            {
                tidy = tidy_check(number);

                if(tidy)
                {
                    output<<"Case #"<<i+1<<": "<<number<<"\n";
                    break;
                }
                else
                {
                    number--;
                }
            }
        }
    }

    input.close();
    output.close();

    return 0;
}
