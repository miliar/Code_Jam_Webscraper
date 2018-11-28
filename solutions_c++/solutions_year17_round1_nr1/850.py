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
#include <vector>
using namespace std;


int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    int cases;
    fin >> cases;
    int height, width;
    vector< vector<string> > Board;
    vector<string> row;
    bool first;
    int count;
    bool refillFirst;
    string input;
    int start = -1;
    for (int i=0;i<cases;i++){
        start = -1;
        fin >> height >> width;
        Board.clear();
        //Board.resize(height);
        row.resize(width);
        for (int j=0;j<height;j++){
            Board.push_back(row );
        }
        for (int k = 0;k<height;k++){
            fin >> input;
            for (int l = 0;l<width;l++)
                //cout <<input[l];
                Board[k][l] = input[l];
        }
        
        refillFirst = true;
        for (int k= 0;k<width;k++){
            first = true;
            count = 0;
            for (int j = 0;j<height;j++){
                
                if (Board[j][k] != "?"){
                    if (first){
                        for (int d = j;d>=0;d--){
                            Board[d][k] = Board[j][k];
                        }
                        first = false;
                    }
                    count ++;
                }
                else{
                    if (j>0){
                        Board[j][k] = Board[j-1][k];
                    }
                }
            }
            if (count == 0){
                if (refillFirst){
                    start = k;
                    
                }
                else{
                    for (int d = 0;d<height;d++){
                        Board[d][k] = Board[d][k-1];
                    }
                
                }
            }
            else{
                refillFirst = false;
            }
            
        
        for (int m = start;m>=0;m--)
            for (int l = 0;l<height;l++){
                Board[l][m] = Board[l][start+1];
            }
        }
        fout << "Case #" << i+1 << ": "  << endl;
        for (int j = 0;j<height;j++){
            for (int l = 0;l<width;l++){
                fout << Board[j][l];
                
            }
            fout <<endl;
        }
    }
    fout.close();
}
