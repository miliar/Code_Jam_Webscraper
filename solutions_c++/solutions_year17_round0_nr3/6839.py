/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: sally090230
 *
 * Created on April 7, 2017, 8:48 PM
 */

#include <cstdlib>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>    // std::reverse
#include <vector>
#include <set>
#include <map>
#include <utility>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void tidy_numbers(long bound_number, int case_number);
void bathroom_stall(long num_stall, long num_people, int case_num);

struct max_num{
  bool operator() (const long& lhs, const long& rhs) const
  {return lhs >= rhs;}
};

int main() {
  int t;
  long stall_num,people_num;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 0; i < t; ++i) {
    cin >> stall_num >> people_num;  // read n and then m.
    if(stall_num == people_num){
        cout << "Case #" << i+1 << ": "<<0<<" "<<0<<endl;
        continue;
    }
    bathroom_stall(stall_num,people_num,i);
  }
}

void tidy_numbers(long bound_number, int case_number){
    vector<int> digits;
    while (bound_number > 0){
        int digit = bound_number%10;
        bound_number /= 10;
        digits.push_back(digit);
    }
    
    if(digits.size()==1){
        cout << "Case #" << case_number+1 << ": " << digits.front()<< endl;
        return;
    }else{
        reverse(digits.begin(),digits.end());
        
        //go through from last digit
        for(int i = digits.size()-1; i >= 1; --i){
            //if number after is smaller than before, then change later number to 9, before number to current -1, and make anything after that to be 0
            
            if(digits[i-1] > digits[i]){
                digits[i-1]--;
                for(int j = i; j < digits.size();j++)
                    digits[j] = 9;
            }
        }
        
        
        //cut 0 from front
        if(digits.front() == 0)
            digits.erase(digits.begin());
        
        cout << "Case #" << case_number+1 << ": ";
        for(int i = 0; i < digits.size(); i++){
            cout<<digits[i];
        }
        cout<<endl;
    }
}

void bathroom_stall(long num_stall, long num_people, int case_num){
    
    //marks if stalls are occupied
    vector<bool> stall_marker(num_stall+2, 0);
    stall_marker[0] = 1;
    stall_marker[num_stall+1] = 1;
    
    
    
    long final_chosen_ls;
    long final_chosen_rs;
    
    vector<long> index_occupied;
    
    
    for(long people_index = 0; people_index < num_people; people_index++){
        //keeps track of the scores
        vector<pair<long,long> > Ls_Rs(num_stall+2, make_pair(0,0));

        //pair of key-> min(ls,rs) value-> index 
        map<long,long,max_num > max_min_score;
        map<long,long, max_num > max_max_score;
        
        index_occupied.clear();
        //keep track of index of occupied stalls
        for(long i = 0; i < stall_marker.size(); i++){
            if(stall_marker[i])
                index_occupied.push_back(i);          
        }
        for(long i = 0; i < index_occupied.size()-1; i++){
            for(long j = index_occupied[i]+1; j < index_occupied[i+1]; j ++){
                
                Ls_Rs[j].first = (j-index_occupied[i]-1);
                Ls_Rs[j].second = (index_occupied[i+1]-j-1);
               
                max_min_score.insert(make_pair(min(Ls_Rs[j].first,Ls_Rs[j].second), j));

            }
        }
        if(max_min_score.size() == 1){
            stall_marker[max_min_score.begin()->second] = 1;
            final_chosen_ls = Ls_Rs[max_min_score.begin()->second].first;
            final_chosen_rs = Ls_Rs[max_min_score.begin()->second].second;
        }else{
            for(map<long,long, max_num>::iterator i = max_min_score.begin(); i != max_min_score.end(); i++){
                if( i->first == max_min_score.begin()->first){
                    long index = (i)->second;
                    long max_score = max(Ls_Rs[index].first,Ls_Rs[index].second);
                    max_max_score.insert(make_pair(max_score,index));
                }
            }
            if(max_max_score.size() == 1){
                stall_marker[max_max_score.begin()->second] = 1;
                final_chosen_ls = Ls_Rs[max_max_score.begin()->second].first;
                final_chosen_rs = Ls_Rs[max_max_score.begin()->second].second;
            }else{
                map<long,long> left_most;
                for(map<long,long, max_num>::iterator i = max_max_score.begin(); i != max_max_score.end() ; i++){
                    if(i->first == max_max_score.begin()->first){
                        long index = i->second;
                        long max_score = i->first;
                        left_most.insert(make_pair(index,max_score));
                    }
                }
                stall_marker[left_most.begin()->first] = 1;
                final_chosen_ls = Ls_Rs[left_most.begin()->first].first;
                final_chosen_rs = Ls_Rs[left_most.begin()->first].second;
            }
        }
    }
    cout << "Case #" << case_num+1 << ": "<<max(final_chosen_ls,final_chosen_rs)<<" "<<min(final_chosen_ls,final_chosen_rs)<<endl;
    

}