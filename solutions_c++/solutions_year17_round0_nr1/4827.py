//
//  main.cpp
//  googlecodejam_1
//
//  Created by Kefan XIAO on 4/7/17.
//  Copyright (c) 2017 Kefan XIAO. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <vector>


using namespace std;

int getFlipTimes(string &pancake, int fliper_size)
// return -1: impossible
// return >=0: number of times needs
{
    auto length = pancake.size();
    if(length==0) return 0;
    vector<bool> states(length, false);
    int move = 0;
    int times = 0;
    while(move!=length)
    {
        
        if(pancake[move]=='-')
        {
            if(length - move < fliper_size) return -1;
            else
            {
                for(int i = 0; i<fliper_size;i++)
                {
                    if(pancake[move+i]=='-') pancake[move+i]='+';
                    else pancake[move+i]='-';
                }
            }
            times++;
        }
        move++;
    }
    return times;
}



int main(int argc, const char * argv[]) {
    
    string line;
    ifstream game_file;
    ofstream output_file;
    game_file.open("Alarge.in");
    int case_num = 0;
    vector<string> result;
    if (game_file)
    {
        getline (game_file,line);
        case_num = stoi(line);
        while ( getline (game_file,line) )
        {
            auto move = line.find(' ');
            string pancake = line.substr(0,move);
            int flip_size  = stoi(line.substr(move+1, line.size()-move-1));
            int got_times = getFlipTimes(pancake, flip_size);
            if(got_times==-1) result.push_back("IMPOSSIBLE");
            else result.push_back(to_string(got_times));
        }
        game_file.close();
    }
    output_file.open("output.txt");
    int number = 1;
    for(auto m : result)
    {
        output_file<<"Case #"<<number<<": "<<m<<"\n";
        number++;
    }
    output_file.close();
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}


