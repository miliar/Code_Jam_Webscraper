#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void FillCake(vector<string>& cake, int R, int C)
{
    for(auto& line: cake)
    {
        auto name = find_if(line.begin(), line.end(), [](char ch){return ch != '?';});
        if(name != line.end())
            for_each(line.begin(), name, [name](char& ch){ch = *name;});
        while(name != line.end())
        {
            auto next_name = find_if(next(name), line.end(), [](char ch){return ch != '?';});
            for_each(next(name), next_name, [name](char& ch){ch = *name;});
            name = next_name;            
        }    
    }
    if(cake[0][0] == '?')
    {
        auto line = find_if(cake.begin(), cake.end(), [](string& l){return l.front() != '?';});
        for(int i = 0;i < R;++i)
            if(cake[i][0] == '?')
                cake[i] = *line;
            else
                break;
    }        
    for(int i = 1;i < R;++i)
        if(cake[i][0] == '?')
            cake[i] = cake[i-1];    
}

int main() {
    ifstream ifile("input.in");
    ofstream ofile("output.txt");
    int T;
    ifile >> T;
    for(int t = 0;t < T;++t)
    {
        int R, C;
        ifile >> R >> C;
        vector<string> cake(R, string(C, '?'));
        for(int i = 0;i < R;++i)
            for(int j = 0;j < C; ++j)
                ifile >> cake[i][j];
        FillCake(cake, R, C);
        ofile << "Case #" << t+1 << ":" << endl;
        for(int i = 0;i < R;++i)
        {
            for(int j = 0;j < C; ++j)
                ofile << cake[i][j];
            ofile << endl;
        }        
    }    
	return 0;
}
