#include <string>
#include <iostream>
#include <fstream>
using namespace std;

void insertIn(vector<int>& numbers, long long int number)
{
    numbers.clear();
    int curr;
    while(number >= 10)
    {
        curr = number - (number / 10) * 10;
        numbers.insert(numbers.begin(), curr);
        number /= 10;
    }
    numbers.insert(numbers.begin(), number);
}

bool isOk(vector<int>& numbers)
{
    for(int i = 1; i < numbers.size(); ++i)
        if(numbers[i] < numbers[i - 1])
            return false;
    return true;
}

void print(vector<int>& numbers)
{
    long long int number = 0;
    for(int i = 0; i < numbers.size(); ++i)
        number += numbers[i] * pow(10, numbers.size() - i - 1);

    cout << number << endl;
}

void thinkOn(vector<int>& numbers)
{
    for(int i = numbers.size() - 2; i >= 0; --i)
    {
        if(numbers[i] > numbers[i + 1]){

            if(i + 2 == numbers.size()){
                numbers[i + 1] = 9;
                --numbers[i];
            }
            else
            {
                numbers[i + 1] = numbers[i + 2];
                --numbers[i];
            }
        }
    }
}




int main(int argc, char *argv[])
{
    ifstream myCin;
    myCin.open("B-small-attempt2.in", ifstream::in);
    if (myCin.is_open()) {

        int T;
        myCin >> T;

        for(int i = 0; i < T; ++i)
        {
            long long int number;
            myCin >> number;

            cout << "Case #" << (i + 1) << ": ";

            vector<int> numbers;
            insertIn(numbers, number);
            thinkOn(numbers);
            print(numbers);
        }

    }
    myCin.close();
}
