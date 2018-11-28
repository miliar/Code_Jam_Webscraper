#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int solve(string &str, int k)
{
    int cnt = 0;
    int len = str.size() - k + 1;
    for(int i = 0; i < len; ++i) {
        if(str[i] == '-') {
            for(int j = 0; j < k; ++j) {
                str[i+j] = str[i+j]=='+'?'-':'+';
            }
            ++cnt;
        }
    }
    for(int i = len - 1; i < len + k - 1; ++i) {
        if(str[i] != '+') {
            return -1;
        }
    }
    return cnt;
}

int main()
{
    ofstream out("out.txt");
    int k, num = 0;
    string str;
    cin>>num;
    for(int i = 0; i < num; ++i) {
        cin>>str>>k;
        int result = solve(str, k);
        out<<"Case #"<<i+1<<": ";
        if(result != -1) {
            out<<result<<endl;
        } else {
            out<<"IMPOSSIBLE"<<endl;
        }
    }

    return 0;
}
