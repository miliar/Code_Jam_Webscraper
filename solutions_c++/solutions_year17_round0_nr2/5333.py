#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

long long untidyPos(long long n) { //convert to string

    stringstream ss;
    ss << n;
    string str = ss.str();

    int i;
    for (i=0; i<=str.length()-2; i++) {
        if (str[i] > str[i+1]){ //?
            str[i]--;
            break;
        }
    }
    for (i=i+1; i<=str.length()-1; i++)
        str[i] = '9'; //?

    long long value;
    stringstream sss(str);
    sss >> value; 
    return value;
}

int main()
{
    //read
    freopen("B-large.in", "rt", stdin);
    freopen("tidy2.out", "wt", stdout);
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++){
        long long N;
        cin >> N;

        long long res = N;
        int ii=1;
        while (ii<=20) {
            if (res<10) break;
            res = untidyPos(res);
            ii++;
        }
        cout << "Case #" << t << ": " << res << endl;

    }


    return 0;
}
