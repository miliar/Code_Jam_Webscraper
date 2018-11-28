#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <sstream>
#include <deque>
#include <bitset>

using namespace std;

typedef unsigned long long ullong;

string trim_zeros(string s)
{
    while(s[0]=='0')
        s.erase(0,1);
    return s;
}

template<typename T> string print_bin(T n)
{
    stringstream ss;
    ss << bitset<sizeof(T)*8>(n);
    return trim_zeros(ss.str());
}

ullong generate_q(deque<ullong> &spaces, ullong i)
{
    ullong curr = spaces[i];

}

ullong log2(ullong n)
{
    ullong targetlevel = 0;
    while (n >>= 1) ++targetlevel;
    return targetlevel;
}

pair<ullong,ullong> test_case(ullong n, ullong k)
{
    /*deque<ullong> spaces(1,n);
    ullong generated = 1;
    for(int i=0; i<k; ++i)
    {
        ullong curr = spaces[i];
        ullong c1 = curr/2;
        ullong c2 = c1 - 1 + curr%2;
        if(c1!=0 && generated<k)
        {
            spaces.push_back(c1);
            ++generated;
        }
        else
            break;
        if(c2!=0 && generated<k)
        {
            spaces.push_back(c2);
            ++generated;
        }
        else
            break;
    }

    for(int i=0; i<spaces.size(); ++i)
    {
        //cout << print_bin(spaces[i]) << "  ";
        //cout << spaces[i] << "  ";
    }
    //cout << endl;
    if(spaces.size()!=k)
    {
        cout << "!!!!!" << spaces.size() << " " << k << " " << generated << endl;
        for(int i=0; i<spaces.size(); ++i)
        {
            //cout << print_bin(spaces[i]) << "  ";
            cout << spaces[i] << " ";
        }
        cout << endl;
    }
    */


    ullong u = 1<<log2(k);

    ullong spaces = n/u - 1*((k%u) > (n%u));

    cout << n << " " << k << " " << u << " " << spaces << endl;


    ullong mi = (spaces-1)/2;
    ullong ma = mi + (spaces-1)%2;

    return pair<ullong,ullong>(ma,mi);
}

int main()
{
    ifstream fin("C-small-2-attempt0.in");
    ofstream fout("C-small-2-attempt0.out");
    int n_cases;
    fin >> n_cases;
    for(int h=0; h<n_cases; ++h)
    {
        ullong n,k;
        fin >> n >> k;
        pair<ullong,ullong> nos = test_case(n,k);
        fout << "Case #" << h+1 << ": ";
        fout << nos.first << " " << nos.second << endl;
    }
}

