#include<string>

#include<iostream>
using namespace std;


bool isCorrect(string s)
{ 
    if (s.length() == 1)
        return true;

    for (int i = 0; i <= s.length() -2; ++i) {
        if (!(s[i] - '0' <= s[i+1] -'0')) 
           return false;
    }
    return true;
}    

int main()
{
    string s = "---+-++-";
    int n = 132;
    int t = 1 , ct = 0;

    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        for (int j = n; j >= 1; --j) {
            if (isCorrect(std::to_string(j))) {
                cout << "case #" <<  i + 1<< ": " << j << endl;  
                break;
            }
        }
    }
    return 0;
} 
    
