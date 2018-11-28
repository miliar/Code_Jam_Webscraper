#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

bool fixed(string ss, int ii) {
    for (int q = ii; q <= ss.length() - 1; q++)
    {
        if (ss[q] == '-')
        {
            return false;
        }
    }
    return true;
}
string flip(string ss, int start, int N) {
    for (int j=start; j<=N+start-1; j++) {
        if (ss[j]=='+') ss[j] = '-';
        else if (ss[j]=='-') ss[j] = '+';
    }
    return ss;
}

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("A.out", "wt", stdout);
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++){
        string s = "";
        int K;
        cin >> s >> K; //space?
        
        int i; int res=0;
        for (i = 0; i<= s.size() - K; i++){//
            if (s[i]=='-') {
                s = flip(s, i, K);
                res++;
            }
        }

        //check
        if (fixed(s, i))
            cout << "Case #" << t << ": " << res << endl;
        else
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;


    }


    return 0;
}
