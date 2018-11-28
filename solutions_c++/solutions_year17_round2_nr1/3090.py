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

int main(int argc, char* argv[]){
    /*
    string dummy = "a b c d e f g";
    vector<string> test = split(dummy, ' ');
    for(int i = 0; i < test.size(); i++){
       cout << test[i] << endl;
    }*/
    string inputfile = argv[1];
    string outputfile = argv[2];
    vector<string> input;
    input = readFromFile(inputfile);
    int numt = stoi(input[0]);
    vector<string> ans;
    int cc = 1;
    for(int i = 1; i < input.size(); i++) {
        vector<string> dn = split(input[i], ' ');
        int dis = stoi(dn[0]);
        int n = stoi(dn[1]);
        double maxt = 0.0;   
        for(int j = 1; j <= n; j++) {
            vector<string> kss = split(input[++i], ' ');
            int k = stoi(kss[0]);
            int s = stoi(kss[1]);
            double t = ((double)(dis - k))/((double) s);
            maxt = max(maxt, t);
        }
        double maxs = ((double) dis)/maxt;
        ans.push_back("Case #"+to_string(cc)+": "+to_string(maxs));
        cc++;
    }
    writeToFile(ans, outputfile);
}
