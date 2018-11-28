#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>

using namespace std;

unsigned long long findTidy(unsigned long long num) {
    unsigned long long result;
    string str = to_string(num);
    int len = str.size() - 1;
    int tmp = len;
    result = num;
    bool done = false; 
    while ( !done ) { 
        str = to_string(result);
        len = str.size() - 1;
        done = true;
        for( string::iterator it = str.begin() ; it != str.end() - 1 ; it++ ) {
            if ( *it > *(it + 1) ) {
                result -= 1;
                done = false; 
            }
            len--;
        }
    }
    return result;
}

int main() {
    int n;
    int k = 1;
    scanf("%d",&n);
    while( n-- ) {
        unsigned long long num;
        scanf("%lld",&num);
        printf("Case #%d: %lld\n", k++, findTidy(num));  
    }
    return 0;
}
