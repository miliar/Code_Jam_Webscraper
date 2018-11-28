#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <fstream>

using namespace std;

class pancake
{
public:
    
    pancake(string s)
    {
        vs = tokenize(s);
        
        string::size_type sz;
        K = stoi(vs.at(1), &sz);
        
        stop_point = vs.at(0).size() - K;
    }
    
    vector<string> vs;
    int K;
    int stop_point;
    
    vector<string> tokenize(string str);
    void flip(int start);
    int perform();
};

vector<string> pancake::tokenize(string str)
{
    istringstream iss(str);
    vector<string> ret {istream_iterator<string>(iss), 
                        istream_iterator<string>()};
    return ret;
}

void pancake::flip(int start)
{
    for(int i = start; i < start + K; i++)
    {
        if(vs.at(0).at(i) == '+')
            vs.at(0).at(i) = '-';
        
        else
            vs.at(0).at(i) = '+';
    }
}

int pancake::perform()
{
    int count = 0;
    for(int i = 0; i <= stop_point; i++)
    {
        if(vs.at(0).at(i) == '-')
        {
            flip(i);
            count++;
        }
    }
    
    size_t found = vs.at(0).find('-');
    
    if(found != string::npos)
        return -1;
    else
        return count;
    
    
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("out.txt");
    
    string k;
    getline(fin, k);
    string::size_type sz;
    int T = stoi(k, &sz);
    
    vector<string> v;
    
    for(int i = 0; i < T; i++)
    {
        string s;
        getline(fin, s);
        
        pancake p(s);
        int x = p.perform();
        ostringstream oss;
        
        oss << "Case #" << i + 1 << ": ";
        if(x == -1)
            oss << "IMPOSSIBLE";
        else
            oss << x;
        
        v.push_back(oss.str());
    }
    
    for(int i = 0; i < v.size(); i++)
        fout << v.at(i) << endl;
    
    fin.close();
    fout.close();
}