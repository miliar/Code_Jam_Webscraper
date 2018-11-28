//
//  main.cpp
//  googlecodejam3
//
//  Created by Kefan XIAO on 4/8/17.
//  Copyright (c) 2017 Kefan XIAO. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <queue>
#include <math.h>
#include <unordered_map>

using namespace std;

class location
{
public:
    double left;
    double right;
    double loc;
    location(): left(0), right(0), loc(0){}
    location(double l, double r, double lo): left(l), right(r), loc(lo){}
};

class comparison
{
public:
    bool operator ()(location a, location b){
        if(min(a.left, a.right) > min(b.left, b.right)) return false;
        else if(min(a.left, a.right) < min(b.left, b.right)) return true;
        else
        {
            //maximum compare;
            if(max(a.left, a.right) > max(b.left, b.right)) return false;
            else if(max(a.left, a.right) < max(b.left, b.right)) return true;
            else
            {
                if(a.loc > b.loc) return true;
                else return false;
            }
        }
    }
};

bool compare(location a, location b){
    if(min(a.left, a.right) > min(b.left, b.right)) return true;
    else if(min(a.left, a.right) < min(b.left, b.right)) return false;
    else
    {
        //maximum compare;
        if(max(a.left, a.right) > max(b.left, b.right)) return true;
        else if(max(a.left, a.right) < max(b.left, b.right)) return false;
        else
        {
            if(a.loc > b.loc) return false;
            else return true;
        }
    }
}

/*
pair<int,int> getMaxMin(int rest_room_num, int person_num)
{
    //priority_queue<location, vector<location>, function<bool(location* a, location* b)> > store(compare);
    //store(comparison());
    priority_queue<location, vector<location>, comparison > store;
    double my_room_num = static_cast<double>(rest_room_num);
    double maximum = ceil((my_room_num-1)/2);
    double minimum = floor((my_room_num-1)/2);
    store.push(location(minimum, maximum, ceil((my_room_num-2)/2)));
    while(person_num>1)
    {
        auto head = store.top();
        person_num--;
        store.pop();
        location left(floor((head.left-1)/2), ceil((head.left-1)/2), head.loc - ceil((head.left-1)/2)-1);
        location right(floor((head.right-1)/2), ceil((head.right-1)/2), head.loc + floor((head.right-1)/2) + 1);
        store.push(left);
        store.push(right);
        //minimum =min(minimum,min( min(left.left, left.right), min(right.left, right.right)));
    }
    return make_pair(static_cast<int>(max(store.top().left, store.top().right)),static_cast<int>(min(store.top().left, store.top().right)));
}
*/
pair<long long,long long> getMaxMin(long long rest_room_num, long long person_num){
    std::priority_queue<double, std::vector<double>, std::less<double> > store;
    unordered_map<double, long long> record;
    double my_room_num = static_cast<double>(rest_room_num);
    store.push(my_room_num);
    record[my_room_num] = 1;
    while(person_num>1)
    {
        double myhead = store.top();
        long long count = record[myhead];
        if(person_num<=count) break;
        store.pop();
        record.erase(myhead);
        
        person_num -= count;
        double big = ceil((myhead-1.0)/2);
        double small = floor((myhead-1.0)/2);
        if(big!=0.0)
        {
            auto target = record.find(big);
            if(target==record.end())
            {
                store.push(big);
                record[big] = count;
            }
            else target->second+=count;
        }
        if(small!=0.0)
        {
            auto target = record.find(small);
            if(target==record.end())
            {
                store.push(small);
                record[small] = count;
            }
            else target->second+=count;
        }
    }
    double myhead = store.top();
    return make_pair( static_cast<long long>(ceil((myhead-1.0)/2)), static_cast<long long>( floor((myhead-1.0)/2))  );
    //return make_pair(myhead,myhead);
}

int main(int argc, const char * argv[]) {
    
    string line;
    ifstream game_file;
    ofstream output_file;
    game_file.open("Csmall2.in");
    int case_num = 0;
    vector<string> result;
    if (game_file)
    {
        getline (game_file,line);
        case_num = stoi(line);
        int show = 1;
        while ( getline (game_file,line) )
        {
            auto split = line.find(' ');
            long long rest_room_num = stoll(line.substr(0,split));
            long long person_num    = stoll(line.substr(split+1, line.size() - split - 1));
            auto myresult = getMaxMin(rest_room_num, person_num);
            result.push_back(to_string(myresult.first)+" "+to_string(myresult.second));
            cout<<"case: "<< show<<endl;
            show++;
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
