#include <iostream>
#include <string>

using namespace std;

bool checkTidy(long in)
{
    int c = in%10;
    in = in/10;
    while (in != 0)
    {
        if (in%10 <= c)
            c = in%10;
        else
            return false;
        
        in = in/10;
    }
    return true;
}

long checkMinOptions(long in)
{
    //if (in/10 == 0)
    //    return in;
        
    while (in >= 0)
    {
        if (checkTidy(in))
            return in;
        else
            in = in - 1;
    }
    
            
    
    
}

int main() {
    int T, i = 1;
    long lnum;
    
    cin >> T;

    while (T > 0)
    {
        cin >> lnum;

        cout << "Case #" << i++ << ": " << checkMinOptions(lnum) << endl;
        T--;
    }
    
	return 0;
}
