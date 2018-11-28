#include <iostream>
#include <fstream>

using namespace std;

ofstream fout;

std::string minusOne (std::string s);
bool isTidy(std::string s);

int main()
{
    ifstream fin;
    fin.open("B-small-attempt0.in");
    if (!fin.is_open())
    {
        cout << "Error in Opening Input file ";
        return -1;
    }
    fout.open("B-small-attempt0.out");
    int num_cases;

    fin >> num_cases;
    for (int n=0;n<num_cases;++n)
    {
        fout << "Case #" << n+1 << ": ";
        char input[19];
        std::string s, result;
        fin >> s;
        bool tidy = false;
        do {
            tidy = isTidy(s);
            if (!tidy)
                s = minusOne(s);
        } while (!tidy);

        fout << s ;
        fout << endl;
    }
    if (fin)
        fin.close();
    if (fout)
        fout.close();
    return  0;
}

bool isTidy(std::string s) {
    for (int i=s.length()-1;i>0;--i) {
        if ((int)(s[i] - '0') < (int)(s[i-1] - '0')) {
            return false;
        }
    }
    return true;
}

std::string minusOne (std::string s) {
    for (int i=s.length();i>=0;--i) {
        if ((int)(s[i] - '0') >= 1) {
            s[i] = (int)(s[i] - '0') - 1 + '0';
            break;
        } else {
            s[i] = '9';
        }
    }
    if (s[0] == '0') {
        s = s.substr(1, s.length()-1);
    }
    return s;
}
