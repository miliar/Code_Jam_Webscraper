#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

typedef int ll;

int main ( void )
{
    ll T; cin >> T;
    string line; getline( cin, line );
    for ( ll t = 0; t < T; ++t ) {
        getline( cin, line );
        istringstream iss( line );
        vector<int> v;
        
        char c;
        while ( iss >> c ) {
            v.push_back( c - '0' );
        }
        
        auto itProcess = v.begin();
        auto itAdvance = v.begin(); ++itAdvance;
        
        bool error = false;
        while ( itAdvance != v.end() ) {
            if ( *itProcess > *itAdvance ) {
                error = true;
                break;
            }
            ++itProcess; ++itAdvance;
        }
        
        if ( error ) {
            auto it = itAdvance; ++it;
            for ( ; it != v.end(); ++it )
                *it = 9;
            while ( itAdvance != v.begin() && *itProcess > *itAdvance ) {
                *itProcess -= 1; *itAdvance = 9;
                --itProcess; --itAdvance;
            }
        }
        
        cout << "Case #" << (t + 1) << ": ";
        auto itResult = v.begin();
        while ( *itResult == 0 ) ++itResult;
        while ( itResult != v.end() ) {
            cout << *itResult;
            ++itResult;
        }
        cout << endl;
    }
    
    return 0;
}