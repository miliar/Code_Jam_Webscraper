#include "iostream"
#include "string"


using namespace std;

string str;
int k;

void flip(int p) {
    for(int i=p;i<p+k;i++) {
        str[i] = (str[i]=='-')?'+':'-';
    }
}

int main(int argc, char const *argv[]) {
    int tc;
    cin >> tc;
    for(int ti=1;ti<=tc;ti++) {
        cin >> str;
        cin >> k;
        int count = 0;

        for(int i=0;i<=str.length()-k;i++) {
            if(str[i]=='-') {
                flip(i);
                count++;
            }
        }

        bool flag = true;
        for(int i=0;i<str.length();i++) {
            if(str[i]!='+') {
                flag = false;
                break;
            }
        }

        if (flag) {
            cout << "Case #" << ti << ": " << count;
        } else {
            cout << "Case #" << ti << ": IMPOSSIBLE";
        }
        cout << endl;


    }
    return 0;
}
