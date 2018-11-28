#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    int T=0;
    cin >> T;

    for (int i=1; i<=T;i++){
        unsigned long long int N=0L;

        cin >> N;
        stringstream ss;
        ss << N;
        string s = ss.str();

        string s2 = "";
        s2 += s[0];
        string tidy = "";

        for(int j=1; j<s.size(); j++)
            s2 += s[0];

        while(s2 <= s)
        {
            tidy += s[0];
            s = s.substr(1, s.size()-1);

            s2 = "";
            s2 += s[0];
            for(int j=1; j<s.size(); j++)
                s2 += s[0];

        }

        long long int n = 1LL * pow(10, s2.size()-1) * (s2[0] - '0');
        n -= 1;
        stringstream ss2; ss2 << tidy << n;


        cout << "Case #" << i << ": " << atoll(ss2.str().c_str()) << endl;



    }
}
