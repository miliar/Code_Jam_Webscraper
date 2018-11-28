#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define MP make_pair

int main()
{
    ofstream file;
    file.open("output.txt");
    ifstream infile;
    infile.open("A-large.in");

    //ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int T, k, n, l, i, j;
    string s;
    bool flag ;
    infile >> T;
    for(int lel = 1; lel <= T; ++lel)
    {
        flag = true;
        n = 0;
        infile >> s >> k;

        l = s.length();
        for(i = 0; i<= l-k; ++i)
        {
            if(s[i] == '-')
            {
                ++n;
                for(j = i; j < i + k; ++j)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        file << "Case #"<< lel <<": ";
        for(i = 0; i< l ; ++i)
        {
            cout << s[i];
            if(s[i] == '-')
            {
                file << "IMPOSSIBLE\n";
                flag = false;
                break;
            }
        }
        if(flag)
            file << n<<"\n";
        cout <<"\n";
    }
    return 0;
}
