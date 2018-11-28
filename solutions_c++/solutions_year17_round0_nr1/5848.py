#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void flip(string& s, int n, int k)
{
    for(int i = n; i < n+k; i++)
    {
        if(s[i] == '+') s[i] = '-';
        else s[i] = '+';
    }
}

int main()
{
    int t, k;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in >> t;
    for(int i = 0; i < t; i++){
        string s; in >> s; in >> k;
        bool pos = true;
        int j, count = 0, n = s.length();
        for(j = 0; j < n - k + 1; j++){
            if(s[j] == '-') {
                flip(s, j, k);
                count++;
            }
        }
        for(; j < n; j++){
            if(s[j] == '-'){
                pos = false; break;
            }
        }
        if(n < k)
            pos = false;
        if(pos) out << "Case #" << i+1 << ": " << count << endl;
        else out << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
