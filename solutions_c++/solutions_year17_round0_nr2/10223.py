#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;


vector<int> stringToVec(string inp)
{
    vector<char> cVec = vector<char>(inp.begin(), inp.end());
    vector<int> nVec = vector<int>();
    for(const auto& c: cVec)
    {

        int val = c - '0';
        nVec.push_back(val);
    }
    return nVec;
}


bool strictIncreasing(vector<int> inp)
{
    bool works = true;
    for(int i = 0; i < inp.size() - 1; i++)
    {
        if(inp[i] > inp[i+1])
        {

            return false;
        }
        
    }
    return works;

}



vector<int> numToVec(int inp)
{
    string s = to_string(inp);
    return stringToVec(s);

}



int main(int argc, char **argv)
{
    if(argc != 3)
    {
        cout << "incorrect arguments"<< endl;
        return -1;
    }
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    string str;
    int cs = 1;
    int mx;
    getline(in, str);
    mx = atoi(str.c_str());
    for(int i = 0; i< mx; i++)
    {
        getline(in, str);
        int val = atoi(str.c_str());
        auto nv = stringToVec(str);
        if(val < 10)
        {
            out << "Case #"<< cs << ": " << val << endl;
        }
        else if(strictIncreasing(nv) )
        {
            out << "Case #"<< cs << ": " << val << endl;
        }
        else
        {
            while(!strictIncreasing(nv))
            {
                val -=1;
                nv = numToVec(val);

            }
            out << "Case #"<< cs << ": " << val << endl;
        }
        cs++;
    }
    in.close();
    out.close();

    return 0;
}
