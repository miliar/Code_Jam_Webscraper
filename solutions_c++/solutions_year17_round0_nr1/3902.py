#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <fstream>
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


void flipPancakes(string& pancakes, int i, int k) {
    for (int j = i; j < i+k; j++) {
        if (pancakes[j] == '+') pancakes[j] = '-';
        else pancakes[j] = '+';
    }
}

int overSizedFlipper(string& pancakes, int k){
    int n = pancakes.length();
    int i = 0;
    int counter = 0;
    while(pancakes[i] == '+') {
        i++;
    }
    while(n-i >= k) {
        //cout << "before flipping " << pancakes << endl;
        flipPancakes(pancakes, i, k);
        //cout << "after flipping " << pancakes << endl;
        counter ++;
        while(pancakes[i] == '+') {
            i++;
        }
    }
    
    for (int k = i; k < n; k++) {
        if (pancakes[k] == '-') return -1;
    }
    return counter;
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
       string pcks = input[0];
       int count = overSizedFlipper(pcks, k);
       if (count != -1) {
           ans[t-1] = "Case #"+to_string(t)+": "+to_string(count);
       }
       else {
           ans[t-1] = "Case #"+to_string(t)+": IMPOSSIBLE";
       }
    }
    writeToFile(ans, outputfile);
}
