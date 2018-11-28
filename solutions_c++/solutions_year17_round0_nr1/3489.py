#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("out.txt");

    int t;
    infile>>t;
    for(int cas =1;cas<=t;cas++)
    {
        string s;
        int k;
        infile >> s >> k;
        int i = 0, cnt = 0;
        while (i <= s.length() - k) {
            if (s[i] == '-') {
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                }
                cnt++;
            }
            i++;
        }
        int flag = 1;
        for (int j = 0; j < s.length(); j++)
            if (s[j] != '+') {
                flag = 0;
                break;
            }
        outfile<<"Case #"<<cas<<": ";
        if (flag == 0)
            outfile << "IMPOSSIBLE\n";
        else
            outfile << cnt << endl;
    }
    return 0;

}
