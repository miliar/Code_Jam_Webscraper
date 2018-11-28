#include <fstream>
#include <iostream>
using namespace std;


int main(int argc, char * argv[])
{
    if (argc != 2)
        return -1;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, t, i;
    string line;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> line;
        
        i = 0;
        
        while (i < line.length() - 1 && line[i] <= line[i+1])
            i++;
        
        if (i < line.length() - 1) {
            while (i > 0 && line[i] == line[i-1])
                i--;
            
            line[i++]--;
            
            while (i < line.length())
                line[i++] = '9';
            
            if (line[0] == '0')
                line.erase(0, 1);
        }
        
        fout << "Case #" << t << ": " << line << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
