#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
typedef long long ll;

using namespace std;

const string kInputFilename = "input.txt";
const string kOutputFilename = "output.txt";

ifstream in("input.txt");
ofstream out("output.txt");

int main() {
  int T;
  in >> T;
  for (int ti=0;ti<T;ti++){
    string s;
    in>>s;
    int len=s.length();
    int inc=0;
    for (int i=0;i<len-1;i++){
        if (s[i]>s[i+1]){
            break;
        }
        else{
            inc++;
        }
    }
    int tinc=inc;
    for (int i=tinc-1;i>=0;i--){
        if (s[i]==s[i+1]){
            inc--;
        }
        else{
            break;
        }
    }
    bool already=true;
    for (int i=1;i<len;i++){
        if (s[i]<s[i-1]){
            already=false;
        }
    }
    string t=s;
    if (!already){
        if (inc==0){
        if (s[0]=='1'){
            t=t.substr(0,len-1);
            for (int i=0;i<len-1;i++){
                t[i]='9';
            }
        }
        else{
            t[0]--;
            for (int i=1;i<len;i++){
                t[i]='9';
            }
        }
    }
    else{
        t[inc]--;
        for (int i=inc+1;i<len;i++){
            t[i]='9';
        }
    }
    }
  //  cout<<ti+1<<" "<<t<<" "<<s<<endl;
    out<<"Case #"<<ti+1<<": "<<t<<endl;
  }
  out.close();
  return(0);
}
