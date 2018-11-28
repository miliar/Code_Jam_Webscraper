#include <bits/stdc++.h>

using namespace std;

int main () {
    int t, caso = 1;
    scanf ("%d", &t);
    while (t--) {
        string n;
        cin >> n;
        for (int i = n.length()-1; i > 0 ; i--) {
            if (n[i] < n[i-1]) {
                n[i] = '9';
                if (n[i-1] != '0')
                    n[i-1] -= 1;
                for (int j = i; j < n.length(); j++)
                    n[j] = '9';    
            } else if (n[i] == '0') {
                n[i] = '9';
            }
            //else if (n[i] < n[i-1])
                //n[i] = '9';
        }
        printf ("Case #%d: ", caso++);
        if (n[0] == '0')
            for (int i = 1; i < n.length(); i++)
                printf ("%c", n[i]);
        else       
            cout << n;
        printf ("\n");
    }
    return 0;
}
