#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    int T, l, j;
    char * ch = new char[20];
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> ch;
        l = int(strlen(ch));
        for (j = 0; j < l-1; j++) {
            if (ch[j] > ch[j+1]) {
                ch[j]--;
                for (int k = j+1; k < l; k++)
                    ch[k] = '9';
                break;
            }
        }
        while (j > 0 && ch[j] < ch[j-1]) {
            ch[j] = '9';
            j--;
            ch[j]--;
        }
        printf("Case #%d: ", i);
        if (ch[0] == '0') cout << ch+1 << endl;
        else cout << ch << endl;
    }
    delete [] ch;
    return 0;
}