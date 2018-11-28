#include <algorithm>
#include <functional>
#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <math.h>
#include <time.h>
#include <stack>
#include <queue>
#include <limits>
#include <map>

using namespace std;

struct FlipInfo{

    bool possible;
    long long int tflips;

    FlipInfo( bool possible, long long int tflips ){

        this->possible = possible;
        this->tflips = tflips;
    }
};

class CheckPattern{

    public:

        FlipInfo isFlipPossible( vector <char> vec, long long int flips ){

            long long int tflips = 0;

            for( long long int i=0 ; i<vec.size()-flips+1; i++ ){

                if( vec[i] == '-' ){

                    for( long long int j=i ; j<i+flips ; j++ ){
                        if( vec[j] == '+' ){
                            vec[j] = '-';
                        } else {
                            vec[j] = '+';
                        }
                    }

                    tflips ++;
                }
            }

            for( long long int i=vec.size()-flips+1 ; i<vec.size(); i++ ){
                if( vec[i] == '-' ){
                    return FlipInfo(false,-1);
                }
            }

            return FlipInfo(true,tflips);
        }

        FlipInfo checkPattern( string pattern, long long int flips ){

            vector <char> vec;
            for( long long int i=0 ; i<pattern.length() ; i++ ){
                vec.push_back( pattern[i] );
            }

            return isFlipPossible( vec,flips );
        }
};

int main(){

    int T;
    cin >> T;

    ofstream fout;
    fout.open("output.txt", ios::out);

    for( long long int i=0 ; i<T ; i++ ){

        string pattern;
        cin >> pattern;

        long long int flips;
        cin >> flips;

        CheckPattern cp;

        FlipInfo flipInfo = cp.checkPattern( pattern, flips );

        if( !flipInfo.possible ){
            fout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        } else {
            fout << "Case #" << i+1 << ": " << flipInfo.tflips << endl;
        }
    }

    return 0;
}
