#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>  // includes cin to read from stdin and cout to write to stdout

#include <string>
#include <vector>
#include <algorithm>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

std::string solve(vector<char> K);

int main() {
    int tc;
    std::string K;
    
    ifstream file("./a.txt");
    ofstream ofile("./o.txt");
    file >> tc;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int i = 1; i <= tc; ++i)
    {
        
        file >> K;
        
        auto str = solve(std::vector<char>(K.begin(), K.end()));
        auto v = std::stol(str);

        cout << "Case #" << i << ": " << v << " " << endl;
        ofile << "Case #" << i << ": " << v << " " << endl;
        
    }
    return 0;
}

bool isTidy(vector<char> buf)
{
    if(buf.size() == 1) return true;
    
    std::string str(buf.begin(), buf.end());
        std::sort(str.begin(), str.end());
    return  std::string(buf.begin(), buf.end()) == str;

}

std::string solve(vector<char> K)
{
    if (isTidy(K))
        return std::string(K.begin(), K.end());
    
    auto it = K.rbegin();
    while(it != K.rend())
    {
        if (*it != '9')
        {
            *it = '9';
            it++;
            int v = *(it) - '0';
            while(v == 0)
            {
                *it = '9';
                it++;
                v = *(it) - '0';
                //*(it-1) = (v == 0 ? 9 : v-1) + '0';
            }
            *it=(v-1) + '0';
            return solve(K);
        }
        ++it;
    }
    
    return "0";
}
