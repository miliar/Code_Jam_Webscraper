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
#include <algorithm>
#include <cmath>
using namespace std;


int main(){
    ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");
    int cases;
    fin >> cases;
    int number, packages;
    vector<int> require;
    vector< vector<double> > resource;
    vector<int> food;
    vector<double> normal;
    vector<int> indices;
    double minimum, maximum;
    int max_in, min_in;
    int count = 0;
    bool stillon;
    for (int i=0;i<cases;i++){
        count = 0;
        fin >>number>>packages;
        require.resize(number);
        resource.clear();
        food.resize(packages);
        normal.resize(packages);
        for (int j = 0;j<number;j++){
            fin >> require[j];
        }
        for (int j= 0 ;j<number;j++){
            
            for (int l = 0;l<packages;l++){
                fin >> food[l];
            }
            sort(food.begin(), food.end());
            for (int l=0;l<packages;l++){
                normal[l] = food[l] / (double)require[j];
            }
            resource.push_back(normal);
        }
        indices.resize(number);
        for (int j=0;j<number;j++){
            indices[j] = 0;
        }
        stillon = true;
        while (stillon){
            minimum = INT_MAX;
            maximum = INT_MIN;
            for (int j = 0;j<number;j++){
                if (resource[j][indices[j]] < minimum){
                    minimum = resource[j][indices[j]];
                    min_in = j;
                }
                if (resource[j][indices[j]] > maximum){
                    maximum = resource[j][indices[j]];
                    max_in = j;
                }
            }
            if (int(minimum / 0.9) >= ceil(maximum / 1.1)){
                count ++;
                for (int j = 0;j<number;j++){
                    indices[j] ++;
                    if (indices[j]>=packages){
                        stillon = false;
                    }
                }
            }
            else{
                indices[min_in]++;
                if (indices[min_in]>=packages){
                    stillon = false;
                }
            }
        }
        fout << "Case #" << i+1 << ": " <<count << endl;
        
    }
    fout.close();
}
