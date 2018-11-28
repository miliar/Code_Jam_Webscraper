#include <iostream>
#include<math.h>
#include <fstream>
#include <string>
using namespace std;

void numberIsTidy(int);
int makeTidy(int);
int digits[23];
int main ()
 {
    int cases;
    int number;
    ifstream input ("C:\\Users\\Pavilion\\Downloads\\B-small-attempt7.in");
    ofstream solution("H:\\sol.txt");
    input>>cases;
    for(int i=0; i<cases; i++)
    {
        input>>number;

            for(int i=0; i<23; i++)
            digits[i]=0;
        if(number%10 == number)
            solution<<"Case #"<<i+1<<": "<<number<<"\n";

        else
        {
            numberIsTidy(number);
            if(digits[19] == -1)
                solution<<"Case #"<<i+1<<": "<<number<<"\n";
            else
            {
                int number1 = makeTidy(number);
                solution<<"Case #"<<i+1<<": "<<number1<<"\n";

            }
        }
    }
  return 0;
}
void numberIsTidy(int number)
{
    int index = 0 , flag = 0;
    while(number > 0)
    {
        digits[index] = number%10;
        index++;
        number = number/10;
    }
    int greatest = digits[1];
    digits[20] = 1;
    for(int i=0; i<index-1; i++)
    {
        if(digits[i] < digits[i+1])
        {
            flag=1;
        }
        if(i <= index-3)
        {
        if(greatest <= digits[i+2])
        {
            greatest = digits[i+2];
            digits[20] = i+2;
        }
        }
    }

    if(flag == 0)
    {
        digits[19] = -1;
    }

    digits[21] = index-1;

}
int makeTidy(int number)
{

    int tidy = 0;
    int pos = digits[20];
    //cout<<pos<<" ";
    digits[pos] = digits[pos] - 1;
    for(int i = digits[21]; i>=0; i--)
    {
        if(i >= pos)
        {
           tidy = tidy + pow(10 , i)*digits[i];
        }
        else
        {
            tidy = tidy + pow(10 , i) * 9;

        }
    }
    if(digits[21] == 1 || number == 100 || number == 101 || number == 102 || number == 103 || number == 104 || number == 105 || number == 106 || number == 107 || number == 108 || number == 109)
        return tidy;
    else
        return tidy+1;
}
