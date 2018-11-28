#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int T, K;
string S;


bool isOk(string& str)
{
    for(int i = 0; i < str.size(); ++i)
        if(str[i] == '-')
            return false;
    return true;
}

void inverse(string& str, int start, int count)
{
    if(isOk(str)){
        cout << count;
        throw string("OK");
    }

    int dashPos;
    for(int i = start; i < str.size(); ++i){
        if(str[i] == '-'){
            dashPos = i;
            break;
        }
    }

    if(str.size() - dashPos < K){
        throw string("KO");
    }

    for(int i = dashPos; i < dashPos + K; ++i){
        if(str[i] == '-')
            str[i] = '+';
        else
            str[i] = '-';
    }
    inverse(str, dashPos, count + 1);
}


int main(int argc, char *argv[])
{
    ifstream myCin;
    myCin.open("A-large.in", ifstream::in);
    if (myCin.is_open()) {


        myCin >> T;

        for(int i = 0; i < T; ++i)
        {
            myCin >> S;
            myCin >> K;

            cout << "Case #" << (i + 1) << ": ";
            try{
                inverse(S, 0, 0);
            }
            catch(string s){
                if(s == "KO")
                    cout << "IMPOSSIBLE";
            }

            cout << endl;
        }


    }
    myCin.close();
}
