#include <string>
#include <iostream>
using namespace std;

unsigned long long buildsmallest(unsigned long long number);
bool nondecreasingfix(string &string_number);

int main ()
{
    int number_testcases;
    cin >> number_testcases;
    for (int i = 0;  i < number_testcases; i++)
    {
        unsigned long long testcase;
        cin  >> testcase;
        
        unsigned long long result = buildsmallest(testcase);
        cout << "Case #" << i+1 << ": " << result << endl;
    }
}

// unsigned long long findsmallest(unsigned long long number)
// {
//     string str_testcase = to_string(number);
//     size_t found = str_testcase.find("0");
//     if (found != string::npos)
//     {
//         int string_length = (int) str_testcase.length();
//         string stringrep = string(string_length-1, '9');
//         return stoull(stringrep);
//     }
//     for (unsigned long long j = number; j > 0; j--)
//     {
//         string str_testcase = to_string(j);
//         if (nondecreasing(str_testcase))
//         {
//             return j;
//         }

//     }
//     return -999;
// }

// bool nondecreasing(string string_number)
// {
//     int string_length = (int) string_number.length();
//     for (int i = 0; i < (string_length-1); i++)
//     {
//         if (string_number[i] > string_number[i+1])
//         {
//             return false;
//         }
//     }
//     return true;
// }

unsigned long long buildsmallest(unsigned long long number) {
    // IF THE NUMBER HAS A ZERO ANYWHERE IN IT
    string str_testcase = to_string(number);

    bool flag = true;
    while (flag)
        flag = nondecreasingfix(str_testcase);
    return stoull(str_testcase);
}

bool nondecreasingfix(string &string_number) {
    int string_length = (int) string_number.length();
    for (int i = 0; i < (string_length-1); i++)
    {

        if (string_number[i] > string_number[i+1])
        {
            // decrease current digit by one, make rest of string 9
            // cout << string_number[i] << endl;
            string_number[i] = string_number[i] -1;
            // cout << string_number[i] << endl;
            for (int j = i+1; j < string_length; j++) {
                string_number[j] = '9';
            }
            return true;
        }
    }
    return false;
}

// void foundzero(string &number)
// {
//     size_t found = str_testcase.find("0");
//     if (found != string::npos)
//     {
//         int string_length = (int) str_testcase.length();
//         string stringrep = string(string_length-1, '9');
//         number = stringrep;
//         // return stoull(stringrep);
//     }
// }