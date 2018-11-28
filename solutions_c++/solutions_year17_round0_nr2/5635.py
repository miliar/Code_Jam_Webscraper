#include <iostream>

#define MAX_DIGITS 19

using namespace std;

int modulo(int x, int N)
{
    return (x % N + N) % N;
}

bool isTidy(int digits[])
{
    for (int i = 1; i < MAX_DIGITS; i++)
    {
        if (digits[i] > digits[i - 1])
            return false;
    }

    return true;
}

int numberToArray(unsigned long long number, int digits[])
{
    int counter = 0;
    int length = 0;
    while (number > 0)
    {
        digits[counter++] = number % 10;
        number /= 10;
        length++;
    }

    return length;
}

unsigned long long arrayToNumber(int digits[])
{
    unsigned long long number = 0;

    for (int i = 0; i < MAX_DIGITS; i++)
    {
        number += digits[i] * ((unsigned long long) pow(10, i));
    }

    return number;
}

void carry(int digits[], int pos)
{
    digits[pos] = modulo(digits[pos] - 1, 10);
    if (digits[pos] == 9) // we need to carry
    {
        for (int i = 0; i < pos; i++)
            digits[i] = 9;
        carry(digits, pos + 1);        
    }
}

unsigned long long fastTidyCounter(unsigned long long ourNumber)
{
    int digits[MAX_DIGITS] = { 0 };

    // store all digits in the array so we dont have to recalc every time
    numberToArray(ourNumber, digits);

    // array is now [last digit ------ offset, zeros]

    while (!isTidy(digits))
    {
        for (int i = 0; i < MAX_DIGITS - 1; i++)
        {
            if (digits[i] < digits[i + 1])
            {
                carry(digits, i);
                
                break;
            }
        }
    }

    return arrayToNumber(digits);
}

void main()
{
    int numberOfInputs;
    cin >> numberOfInputs;

    for (int i = 1; i <= numberOfInputs; i++)
    {
        long long int countUntil;
        cin >> countUntil;

        long long int lastNumber;

        lastNumber = fastTidyCounter(countUntil);

        cout << "Case #" << i << ": " << lastNumber << "\n";

    }
}