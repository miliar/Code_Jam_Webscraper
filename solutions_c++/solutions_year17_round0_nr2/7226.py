#include <iostream>
#include <sstream>
#include <cstdlib>

using namespace std;

template < typename T >
T FromString (string s)
{
    stringstream ss(s);
    T t;

    ss >> t;
    return t;
}

void changeRange(string & N, int moment)
{
    N[moment] = N[moment]-1;
    for(int i = moment+1; i < N.length(); i++)
        N[i] = '9';
}

unsigned long long newNumber(unsigned long long N)
{
    /// konwert z int na string
    ostringstream ss;
    ss << N;
    string number = ss.str();

    for(int i = 0; i < number.length()-1; i++)
    {
        if(number[i] != '0')
            if(number[i] > number[i+1])
            {
                changeRange(number,i);
                i=-1;
            }
    }

    return FromString<unsigned long long>(number.c_str());
}

bool checkTiny(unsigned long long N)
{
    /// konwert z int na string
    ostringstream ss;
    ss << N;
    string number = ss.str();

    for(int i = 0; i < number.length()-1; i++)
    {
        if(number[i] != '0')
        {
            if(number[i] > number[i+1]) return false;
        } else return false;
    }
    if(number[number.length()-1] == '0') return false;

    return true;
}

unsigned long long lastTinyNumber(unsigned long long N)
{
    while(true)
    {
        if(checkTiny(N)) return N;
        else N = newNumber(N);
    }
}

int main()
{
    int T;
    unsigned long long N;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> N;
        cout << "Case #" << i+1 << ": " << lastTinyNumber(N) << endl;
    }
    return 0;
}
