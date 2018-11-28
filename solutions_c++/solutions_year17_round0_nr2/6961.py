#include <functional>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <iomanip>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <time.h>
#include <limits>
#include <stack>
#include <queue>
#include <list>

#include <assert.h>
#include <map>

using namespace std;

class TidyNumbers {

    public:

        string processNumber( string str ){

            stack <int> st;
            ostringstream iss;

            for( long long int i=0 ; i<str.length()-1 ; i++ ){
                if( str[i] > str[i+1] ){

                    long long int j;

                    int cur_num = (str[i]-'0')-1;
                    bool fixed = false;

                    for( j=i ; j>0 ; j-- ){

                        if( (str[j-1]-'0') > cur_num ){

                            st.push(9);
                            cur_num = (str[j-1]-'0')-1;
                        } else {

                            st.push(cur_num);
                            fixed = true;
                            break;
                        }
                    }

                    if( !fixed ){
                        st.push(cur_num);
                    } else {
                        j--;
                        for( ; j>=0 ; j-- ){
                            st.push(str[j]-'0');
                        }
                    }

                    bool check = true;
                    while( !st.empty() ){

                        if( !(check && st.top() == 0) ){

                            iss << st.top();
                            check = false;
                        }

                        st.pop();
                    }

                    for( long long int j=i+1 ; j<str.length() ; j++ ){
                        iss << 9;
                    }

                    return iss.str();
                }
            }

            return str;
        }

        long long int findNum( long long int num ){

            for( long long int i=num ; i>=0 ; i-- ){

                long long int n = i;
                int last = n%10;
                n = n/10;

                bool found = true;

                while ( n ){
                    if( n%10 > last ){
                        found = false;
                    }

                    last = n%10;
                    n = n/10;
                }

                if(found){
                    return i;
                }
            }
        }

        void test(){

            long long int num = 1000000000;

            while( num > 0 ){

                ostringstream oss2;
                oss2 << num;

                string onum = oss2.str();

                long long int fnum = findNum(num);

                //cout << "Checking for " << num << ":" << endl;

                ostringstream oss;
                oss << fnum;

                string str = oss.str();
                string str2 = processNumber( onum );

                if( !(str2.compare( str ) == 0) ){

                    //cout << "NOT CORRECT for " << num << ":" << fnum << endl;
                    //cout << "str2:" << str2 << endl;
                    break;
                } else {
                    //cout << "Success output:" << str2 << endl;
                    num = fnum-1;
                }
            }
        }
};

int main()
{
    int T;
    cin >> T;

    ofstream fout;
    fout.open("output1.txt", ios::out);

    for( int t=0 ; t<T ; t++ ){

        string num;
        cin >> num;

        TidyNumbers tn;
        fout << "Case #" << t+1 << ": " << tn.processNumber(num) << endl;
    }

    //TidyNumbers tn;
    //tn.test();

    return 0;
}
