#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void turn(int a, int flips, string& str) {
    for(int i=0; i<flips; i++) {
        if(str[a+i]=='+') str[a+i] = '-';
        else str[a+i]='+';
    }
}
int main()
{
    ifstream cinn("input.txt");
    ofstream coutt("output.txt");

    int T;
    int flips;
    int answer=0;
    int flag=0;
    string str;

    cinn>>T;
    for(int i=0; i<T; i++) {
        answer = 0;
        cinn >> str >> flips;
        for(int i=0; i<str.length()-flips+1; i++) {
            if(str[i]=='-') {
                turn(i, flips, str);
                answer++;
            }
        }

        flag = 0;
        for(int i=0;i<str.length();i++)
            if(str[i]=='-')
                flag=1;

        if(flag==0)
            coutt << "Case #" << i+1 << ": " << answer << endl;
        else coutt << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
