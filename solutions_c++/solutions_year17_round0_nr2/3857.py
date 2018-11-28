#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <fstream>
#include <limits>
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

/*bool checkValid(long long k) {
    long long pre = numeric_limits<long long>::max();
    long long num = k;
    while(num != 0LL){
        long long cur = num % 10LL;
        if (cur <= pre){
            pre = cur;
            num = num/10LL;
        }
        else return false;  
    }
    return true;
}*/

/*long long tidyNums(long long k) {
    while(k>=1) {
        if (checkValid(k)) {
            return k;
        }
        else k = k-1LL;    
    }
    return k;
}*/
string tidyNums(string& s) {
    int i = 0;
    while(i+1 < s.length() && s[i] <= s[i+1]){
        i++;
    }
    if (i == s.length()-1) return s;
    else{
        while(i >=1 && s[i] == s[i-1]){
            i--;
        }
        s[i]--;
        i++;
        while(i < s.length()){
            s[i] = '9';
            i++;
        }
        int j = 0;
        while(s[j] == '0') j++;
        return s.substr(j);   
    }
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
       string input = testcases[t];
       string res = tidyNums(input);
       ans[t-1] = "Case #"+to_string(t)+": "+res;
       cout << ans[t-1] << endl;
    }
    writeToFile(ans, outputfile);
}
