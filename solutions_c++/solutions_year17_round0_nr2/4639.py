#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define MP make_pair

void check_it(vector <int> &vec)
{
    int i, l = vec.size(), j;
    for(i = 0; i< l-1 ; ++i)
    {
        if(vec[i] <= vec[i+1])
            continue;
        else
        {
            vec[i] -= 1;
            j = i+1;
            for(; j < l ; ++j)
            {
                vec[j] = 9;
            }
            check_it(vec);
        }
    }
    return;
}
int main()
{
    ofstream file;
    file.open("output.txt");
    ifstream infile;
    infile.open("B-large.in");

    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);


    int T, l, i;
    string s;
    infile >> T;
    infile.ignore();
    for(int lel = 1; lel <= T; ++lel)
    {
        getline(infile, s);
        vector <int> myvec;
        bool flag = true;
        l = s.length();
        for(i = 0; i< l; ++i)
        {
            myvec.pb(s[i]-'0');
        }

        check_it(myvec);

        file << "Case #"<< lel<<": ";
        if(myvec.size() == 1)
        {
            file << myvec[0]<<"\n";
            continue;
        }
        for(i = 0; i< l ; ++i)
        {
            if(myvec[i] == 0 && flag)
                continue;
            else
            {
                if(flag)
                {
                    flag = false;
                }
                file << myvec[i];
            }
        }
        file <<"\n";
    }
    return 0;
}
