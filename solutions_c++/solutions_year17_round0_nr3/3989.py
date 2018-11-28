#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <fstream>
#include <queue>          // std::priority_queue
#include <functional>     // std::greater
using namespace std;

vector<string> split(const string &s, char delim) {
  stringstream ss(s);
  string item;
  vector<string> elems;
  while (std::getline(ss, item, delim)) {
    //elems.push_back(item);
    elems.push_back(move(item)); // if C++11 (based on comment from @mchiasson)
  }
  return elems;
}

vector<string> readFromFile(string filename) {
  vector<string> res;
  string line;
  ifstream myfile (filename);
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
        res.push_back(line);
    }
    myfile.close();
  }
  else cout << "Unable to open file";
  return res; 
}

void writeToFile(vector<string>& res, string filename) {
  ofstream myfile (filename);
  if (myfile.is_open())
  {
    for (string s : res) {
        myfile << s << endl;
    }
    myfile.close();
  }
  else cout << "Unable to open file";
}

vector<int> findStalls(int N, int k){
    priority_queue<int> maxHeap;
    vector<int> res(2);
    maxHeap.push(N);
    for(int i = 1; i <= k; i++){
        int num = maxHeap.top();
        maxHeap.pop();
        int ls = (num-1)/2;
        int rs = num-1-ls;
        if (i == k){
            res[0] = ls;
            res[1] = rs;
            return res;
        }
        maxHeap.push(ls);
        maxHeap.push(rs); 
    }
    return res;
}

int main(int argc, char* argv[]){
    /*vector<string> input;
    input = readFromFile("test_input.txt");
    writeToFile(input, "test_output.txt");*/
    //vector<string> testcases = {"---+-++- 3","+++++ 4","-+-+- 4"};
    string inputfile = argv[1];
    string outputfile = argv[2];
    cout << inputfile << endl;
    cout << outputfile << endl;
    vector<string> testcases = readFromFile(inputfile);
    //for (string ss : testcases) cout << ss << endl;
    cout << testcases[0] << endl;
    int ts = stoi(testcases[0]);
    vector<string> ans(ts);
    for(int t = 1 ; t < testcases.size(); t++) {
       vector<string> input = split(testcases[t], ' ');
       int k = stoi(input[1]);
       int N = stoi(input[0]);
       vector<int> res = findStalls(N, k);
       ans[t-1] = "Case #"+to_string(t)+": "+to_string(res[1])+" "+to_string(res[0]);
    }
    writeToFile(ans, outputfile);
}
