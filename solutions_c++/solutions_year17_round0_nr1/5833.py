#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int cases;
    long long output;
    int k;
    int starting;
    bool not_pos = false;
    bool done;
    string s;
    cin >> cases;

    for (int i = 1; i <= cases; i++) {
        cin >> s >> k;
        starting = 0;
        output = 0;
        not_pos = false;

        // Find first -
        while (1) {
            done = true;

            for (int j = 0; j < s.length(); j++) {

                if (s[j] == '-') {
                    if (j < starting || j+k > s.length()) {
                        not_pos = true;
                        break;
                    }
                    done = false;
                    starting = j;
                    output++;

                    for (int l = 0; l < k; l++) {
                        if (s[j+l] == '-')
                            s[j+l] = '+';
                        else
                            s[j+l] = '-';
                    }
                    break;
                }
            }
            if (done)
                break;
        }

        if (not_pos)
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i << ": " << output << endl;

    }
}
