#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int getPos(string& s)
{
    int pos = 0;
    while( pos+1 < s.length() && s[pos] <= s[pos+1] )
        ++pos;
    return pos;
}

int main()
{
    //ifstream in("small-practice.in");
    ifstream in("large-practice.in");
    ofstream out("output.out");

    int T;
    in >> T;

    for( int t = 1; t <= T; t++ )
    {
        out << "Case #" << t << ": ";
        
        string s;
        in >> s;

        int pos = getPos(s);
        
        while( pos+1 < s.length() ) //while number is not tidy
        {
            string result = string( s.length()-(pos+1),'9');
            long prefix = stol( s.substr(0,pos+1) );
            --prefix;

            if(prefix != 0)
                result = to_string(prefix) + result;
        
            s = result;
            pos = getPos(s);
        }

        out << s;
        out << endl;
    }

    return 0;
}
