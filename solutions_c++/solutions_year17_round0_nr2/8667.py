#include <iostream>
#include <vector>
#include <bitset>
#include <iterator>
#include <algorithm>
#include <string>
#include "brick-query"

using namespace std;
using namespace brick::query;
void repair( string & num ) {
    bool oveflow = true;
    for (int i = num.size() - 1; i >= 0; --i) {
        int d = num[i] - '0' - 1;
        if ( i == 0 && d == 0 ){
            num.erase(num.begin());
            break;
        }

        int prev = i > 0 ? num[i - 1] - '0' : 0;
        num[i] = '0' + d;
        if ( prev <= d )
            break;
        else
            d = 9;
    }
}

string process(string & num) {
    string res;
    bool overflow = false;
    for( int i = 0; i < num.size(); ++i ) {
        int d = num[i] - '0';
        int r;
        int prev = i > 0 ? num[i - 1] - '0' : 0;
        int next = i + 1 < num.size() ? num[i + 1] - '0' : 9;
        if ( overflow ) {
            r = 9;
            overflow = next != 9;
        } else {
            if ( d <= next ) {
                r = d;
            }else{
                r = d - 1;
                if ( r < prev ) {
                    repair( res );
                    r = 9;
                }
                overflow = true;
            }
        }
        if ( i != 0 || r != 0 )
            res = res + to_string(r);
    }
    return res;
}

int main() {
    int rows;
    cin >> rows;
    cin.ignore();

    for ( int i = 0; i < rows; ++i ) {
        string num;
        getline(cin, num);
        auto res = process(num);
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
}
