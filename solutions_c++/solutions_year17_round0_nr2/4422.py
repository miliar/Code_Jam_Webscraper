#include <iostream>
#include <cstring>

using namespace std;

void solve(ostream& os, istream& is)
{
    char S[1024];
    is >> S;

    char *s = S;
    char *e;

    e = s + strlen(s);

    char *p = s;

    while(p < e - 1) {
        if(*p <= *(p + 1)) {
            ++p;
        } else {
            for(char *q = p + 1; q < e; ++q) {
                *q = '9';
            }

            --*p;
            if(p == s) {
                if(*p == '0') {
                    s = s + 1;
                }
            }
            p = s;
        }
    }

    os << s;
}

int main()
{
    int C;

    cin >> C;

    for(int c = 0; c < C; ++c) {
        cout << "Case #" << c + 1 << ": ";
        solve(cout, cin);
        cout << endl;
    }

    return 0;
}

