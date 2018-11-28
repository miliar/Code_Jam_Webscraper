#include <iostream> 
#include <fstream>
#include <map>
#include <sstream>
#include <cmath>
#include <vector>

using namespace std; 

int main() { 
  unsigned long long int n = 0, k = 0;
  string s2;
  string s="";
  int count = 0;
  int round = 1;
  
  ifstream inFile("input.in");
  ofstream outFile("output.out");

  if(inFile.is_open()){
    getline(inFile,s);
    while(getline(inFile,s, ' ')){
      getline(inFile,s2);
      istringstream f(s);
      istringstream f2(s2);
      int r,c;
      f >> r;
      f2 >> c;
      
      string str = "";
      vector<string> grid;
  
      map<pair<int,int>, string> filled;
      for(int i = 0; i < r; i++){
        getline(inFile,str);
        grid.push_back(str);
        for(int j = 0; j < c; j++){
          if(str[j] != '?'){
            filled[make_pair(i,j)] = str[j];
          }
        }
      }
      for(auto & start: filled){
        for(int i = start.first.first; i < r; i++){
          k = start.first.second;
          while(k != c-1 && grid[i][k+1] == '?' ){
            char c = grid[i][k];
            k++;
            grid[i][k] = c;
            filled[make_pair(i,k)] = c;
          }
          
        }
      }
      for(auto & start: filled){
        for(int i = start.first.first; i < r; i++){
          k = start.first.second;
          while(k != 0 && grid[i][k-1] == '?' ){
            char c = grid[i][k];
            k--;
            grid[i][k] = c;
            filled[make_pair(i,k)] = c;
          }
          
        }
      }
      for(auto & start: filled){
        for(int i = start.first.second; i < c; i++){
          k = start.first.first;
          while(k != r-1 && grid[k+1][i] == '?' ){
            char c = grid[k][i];
            k++;
            grid[k][i] = c;
          }
          
        }
      }
      for(auto & start: filled){
        for(int i = start.first.second; i < c; i++){
          k = start.first.first;
          while(k != 0 && grid[k-1][i] == '?' ){
            char c = grid[k][i];
            k--;
            grid[k][i] = c;
          }
          
        }
      }
      outFile << "Case #: " << round << endl;
      for(int i = 0; i < grid.size(); i++){
        outFile << grid[i] << endl;
      }

    }
    
  }

  inFile.close();
  outFile.close();
} 





