#include <iostream>

using namespace std;

void process_number( string &number ) {
    const int length = number.length();

    int non_tidy_position = -1;
    for( int i = 0; i < length - 1; ++i ) {
        if( number[ i ] > number[ i + 1 ] ) {
            non_tidy_position = i;
            break;
        }
    }

    // cout << number << ", " << non_tidy_position << "\n";
    
    // Is tidy
    if( non_tidy_position == -1 ) return;

    // Make tidy
    
    // // Subsecuents will be '9'
    for( int i = non_tidy_position + 1; i < length; ++i) {
        number[ i ] = '9';
    }

    // cout << number << "\n";

    // // Substract 1 to current and if necessary to is predecesors
    for( int i = non_tidy_position; i >= 0; --i ) {
        if( number[ i ] != '0' ) {
            --number[ i ];
            if( i == 0 ) break;
            if( number[ i - 1 ] <= number[ i ] ) break;
        }
        number[ i ] = '9';
    }

    // cout << number << "\n";
}

int main() {

    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t) {
        string number;
        cin >> number;

        process_number( number );

        cout << "Case #" << t << ": ";
        
        bool leading_zeros = true;
        for( int i = 0; i < number.length(); ++i ) {
            if( leading_zeros && number[ i ] == '0' ) continue;
            cout << number[ i ];
        }

        cout << "\n";
    }

    return 0;
}