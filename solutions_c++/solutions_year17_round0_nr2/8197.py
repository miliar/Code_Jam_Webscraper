#include <iostream>
#include <string>

using namespace std;
typedef unsigned long long ull;

ull N;


bool tidy(string str)
{
    for(int i=0;i<str.size()-1;i++){
        if(str[i] > str[i+1]) return false;
    }
    return true;
}

string solve(string str)
{
    int k = 0;
    for(int i=0;i<str.size()-1;i++){
        if(str[i] >= str[i+1]){
            k = i;
            break;
        }
    }
    string ret = str;
    ret[k]--;
    for(int i=k+1;i<ret.size();i++){
        ret[i] = '9';
    }
    return ret;
}

void print(string str)
{
    int k=0;
    while(str[k]=='0') k++;
    for(int i=k;i<str.size();i++)
        cout << str[i];
    cout << '\n';
}
int main()
{
    freopen("B-small-attempt0.in","r", stdin);
    freopen("B-small-attempt0.out","w", stdout);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++){
        string s;
        cin >> s;
        string ret = s;
        if(!tidy(s)){
            ret = solve(s);
        }
        cout << "Case #" << tc << ": ";
        print(ret);
    }
    return 0;
}
