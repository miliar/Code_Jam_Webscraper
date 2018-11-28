#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>

using namespace std;

vector<int> splitNumber(long long number)
{
    vector<int> digits;
    while (number > 0)
    {
        int digit = number%10;

        number /= 10;
        digits.insert(digits.begin(), digit);
    }
    return digits;
}

long long obtainMaxTidy(vector<int> digits, long long number)
{    
    if (digits.size()==1)
        return number;

    int carry = 0, i = 0, j;
    int output = 0;
    for (i = digits.size()-1; i > 0; i --)
    {        
        if(digits[i] < digits[i-1])
        {
            digits[i-1]--;
            j = i;
            while(j < digits.size() && digits[j] != 9)
            {
                digits[j] = 9;
                j++;
            }  
        }       
    }
    
    for (i = digits.size()-1; i >= 0; i --)
    {
        output += digits[i] * pow(10, digits.size()-1-i);
    }

    return output;
}

int main()
{
    int t;
    long long number, output;
    int i = 1;

    // cin >> t;
    // while(t > 0)
    // {
    //     cin >> number;
    //     vector<int> digits = splitNumber(number);
    //     number = obtainMaxTidy(digits, number);

    //     cout <<"Case #"<< i << ": " << number << endl;
    //     t--;
    //     i++;
    // }

    ifstream file( "B-small-attempt3.in.txt" );
    ofstream out; 
    out.open("B-small-out.txt");
  	if (file.is_open( ))
  	{
  		// Reading number of vertices
   		file >> t;
   		while(t > 0)
        {
            file >> number;
            vector<int> digits = splitNumber(number);
            output = obtainMaxTidy(digits, number);

            out <<"Case #" << i << ": " << output << "\n";
            t--;
            i++;
        }
    }
    file.close( );
    out.close( );

    return 0;
}