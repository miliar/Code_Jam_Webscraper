//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Ivan Bylinkin on 4/7/17.
//  Copyright © 2017 Ivan Bylinkin. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

string read(ifstream &file);
void write(ofstream &file, string data);
bool pancakes(int caseT, ifstream &in, ofstream &out);

int main(){
    // MARK: Definitions
    ifstream input ("input.txt");
    ofstream output ("output.txt");
    
    // read T
    int T = stoi(read(input));
    
    // read the next T cases
    for (int i=0; i<T; i++){
        pancakes(i+1, input, output);
    }
    
    // close files before ending program
    input.close();
    output.close();
    
    // exit
    return 0;
}

// main objective is to count how many flips to make a happy row
bool pancakes(int caseT, ifstream &in, ofstream &out){
    // setup the output
    string output = "Case #"+to_string(caseT)+": ";
    
    // dumb bit of breaking up into sections
    string line = read(in);
    string::size_type endOfPancakes = line.find(' ');
    
    string pancakes = line.substr(0,endOfPancakes);
    int K = stoi(line.substr(endOfPancakes+1, line.length()));
    
    // check if all the pancakes are already happy
    string::size_type sadPancake = pancakes.find('-');
    if (sadPancake == string::npos){
        output += "0";
        write(out, output);
        return true;
    }
    // sadly most of the time, pancakes will not be all happy
    // but our job is to make them happy so the customers are happy
    
    // if they are all sad faced AND divisable by K, you can easily flip them to all happy faces
    // by using S / K moves
    string::size_type happyPancake = pancakes.find('+');
    if (happyPancake == string::npos && pancakes.length() % K == 0){
        output += to_string(pancakes.length() / K);
        write(out, output);
        return true;
    }
    
    //cout << caseT << " " << pancakes << " : " << K << endl;
    // otherwise we play the flip game...
    bool possible = true;
    int flips = 0;
    while (pancakes.find('-') != string::npos && possible){
        // as long as it's possible, flip those pancakes man!
        string::size_type firstSad = pancakes.find('-');
        unsigned long fromSadToEnd = pancakes.length() - firstSad;
        if (fromSadToEnd < K){
            // sorry... can't make that flip
            possible = false;
        }
        else {
            // otherwise, let's flip 'em
            flips++;
            for (unsigned long i=firstSad; i<firstSad+K; i++){
                if (pancakes[i] == '+'){
                    pancakes[i] = '-';
                }
                else {
                    pancakes[i] = '+';
                }
            }
        }
    }
    
    if (possible){
        output += to_string(flips);
        write(out, output);
        return true;
    }
    
    output += "IMPOSSIBLE";
    write(out, output);
    return false;
}

string read(ifstream &file){
    string line = "unable to open file";
    if (file.is_open()){
        line = "";
        getline(file,line);
    }
    return line;
}

void write(ofstream &file, string data){
    if (file.is_open()){
        file << data;
        file << "\n";
    }
}
