#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for ( int testCase = 1; testCase <= t; ++testCase ) {
        string input;
        cin >> input;
        vector<short> inputNum( input.length());
        for ( int i = 0; i < input.length(); ++i ) {
            inputNum[i] = input[i] - '0';
        }
        bool dummy = false;
        int decpoint = -1;
        for ( int i = 0; i < inputNum.size() - 1; ++i ) {
            if ( inputNum[i] > inputNum[i + 1] ) {
                decpoint = i;
                inputNum[i]--;
            }
            if ( decpoint >= 0 )
                break;
        }
        if ( decpoint >= 0 ) {
            for ( int i = decpoint + 1; i < inputNum.size(); ++i ) {
                inputNum[i] = 9;
            }
            for ( int i = decpoint; i > 0; --i ) {
                if(inputNum[i]<inputNum[i-1]){
                    inputNum[i]=9;
                    inputNum[i-1]--;
                }
            }
        }

        cout<<"Case #"<<testCase<<": ";
        for ( int i = 0; i < inputNum.size(); ++i ) {
            if ( inputNum[i] )
                break;
            else
                inputNum[i] = -1;
        }
        for ( auto &&num  :inputNum ) {
            if ( num >= 0 ) {
                cout << num;
            }
        }
        cout << endl;
    }
    return 0;
}