//
//  codejam.cpp
//  codejam
//
//  Created by Zimu Wang on 4/8/17.
//
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    int cases;
    fin >> cases;
    string cakes;
    int length;
    int count = 0;
    for (int i=0;i<cases;i++){
        
        fin >> cakes >> length;
        count = 0;
        for (int i=cakes.size() - length; i>=0;i--){
            if (cakes[i+length - 1] == '-'){
                for (int j=i; j< i+length; j++){
                    if (cakes[j] == '-')
                        cakes[j] = '+';
                    else{
                        cakes[j] = '-';
                        
                    }
                    
                }
                count += 1;
            }
        }
        for (int j = 0; j < cakes.size();j++){
            if (cakes[j] == '-'){
                count = -1;
                break;
            }
        }
        if (count != -1){
            fout << "Case #" << i+1 << ": " << count << endl;
        }
        else{
            fout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
            
        }
    }
    fout.close();
}
