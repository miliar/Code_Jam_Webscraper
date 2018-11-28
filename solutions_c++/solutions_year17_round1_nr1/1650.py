//
//  main.cpp
//  Cake
//
//  Created by Guanyao Huang on 4/14/17.
//  Copyright © 2017 Guanyao Huang. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
int T, R, C;
int main(int argc, const char * argv[]) {
    // insert code here...
    cin >> T;
    for(int i=0; i<T; i++){
        cin >> R >> C;
        vector<string > matrix(R, "");
        for(int j=0; j<R; j++){
            string str;
            cin >> matrix[j];
        }
        
        vector<int> countsPerRow(R, -1);
        for(int j=0; j<R; j++){
            int k = 0;
            for(k = 0; k<C; k++){
                if(matrix[j][k] != '?'){
                    countsPerRow[j] = k;
                    break;
                }
            }
        }
        
        int firstRow = 0;
        for(int j=0; j<R; j++){
            if(countsPerRow[j] != -1){
                firstRow = j;
                break;
            }
        }
        
        int prevColmn = 0;
        for(int k=0; k<countsPerRow[firstRow]; k++){
            matrix[firstRow][k] = matrix[firstRow][countsPerRow[firstRow]];
        }
        char cur = matrix[firstRow][countsPerRow[firstRow]];
        for(int k=countsPerRow[firstRow]+1; k<C; k++){
            if(matrix[firstRow][k] == '?'){
                matrix[firstRow][k] = cur;
            }
            else
                cur = matrix[firstRow][k];
        }

        for(int j1 = 0; j1<firstRow; j1++){
            matrix[j1] = matrix[firstRow];
        }
        
        string curRow =matrix[firstRow];
        for (int j=firstRow+1; j<R; j++){
            //process this row
            if(countsPerRow[j] == -1)
                matrix[j] = curRow;
            else{
                for(int k=0; k<countsPerRow[j]; k++){
                    matrix[j][k] = matrix[j][countsPerRow[j]];
                }
                char cur = matrix[j][countsPerRow[j]];
                for(int k=countsPerRow[j]+1; k<C; k++){
                    if(matrix[j][k] == '?'){
                        matrix[j][k] = cur;
                    }
                    else
                        cur = matrix[j][k];
                }
                
                curRow = matrix[j];
                
            }
        }
        cout << "Case #"<<i+1<<":"<<endl;
        for(int j=0; j<R; j++){
                cout<<matrix[j];
            cout<<endl;
        }

    }
    return 0;
}
