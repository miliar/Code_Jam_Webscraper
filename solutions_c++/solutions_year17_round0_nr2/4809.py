//
//  main.cpp
//  googlecodejam2
//
//  Created by Kefan XIAO on 4/7/17.
//  Copyright (c) 2017 Kefan XIAO. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void getTidy(string& input)
{
    auto length = input.size();
    if(length==1) return;
    int move = 0;
    while(move<length-1)
    {
        
        if(input[move]<=input[move+1]) move++;
        else
        {
            int back = move+1;
            while(back!=length)
            {
                input[back]='9';
                back++;
            }
            input[move] -=1;
            break;
        }
    }
    while(move>0)
    {
        if(input[move]>=input[move-1]) move--;
        else
        {
            input[move] = '9';
            input[move-1] -= 1;
            move--;
        }
    }
    if(input[0]=='0') input = input.substr(1,length-1);
    //else return input;
}

int main(int argc, const char * argv[]) {
    
    string line;
    ifstream game_file;
    ofstream output_file;
    game_file.open("Blarge.in");
    int case_num = 0;
    vector<string> result;
    if (game_file)
    {
        getline (game_file,line);
        case_num = stoi(line);
        while ( getline (game_file,line) )
        {
            //result.push_back(getTidy(line));
            getTidy(line);
            result.push_back(line);
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
