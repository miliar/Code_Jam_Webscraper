#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


void impossible(int i) {
    cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
}
    
void ok(int i, int j) {
    cout << "Case #" << i << ": " << j << endl;
}

void flip(string &str, int size, int start) {
   
    for (int i=start; i<start+size; ++i)
    {
        if(str[i] == '-')
            str[i] = '+';
        else
            str[i] = '-';
    }
}

bool finished(string s) {
 
    for(int i=0; i < s.size(); i++) {
        if(s[i] != '+')
            return false;
    }   
    return true;
}

int nextFlip(string s) {
    
    for(int i=0; i < s.size(); i++) {
        if(s[i] != '+')
            return i;
    } 
    return -1;
}


int main() {
    
  int t;
  
  string s;
  int k;
  
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  
  
  for (int i = 1; i <= t; ++i) {
    cin >> s >> k;  // read n and then m.
 
    int j = 0;
    
    bool cont = true;
    
    while(cont) {
    int nextF = nextFlip(s);
    
    if(nextF == -1) {
        cont = false;
        ok(i, j);
    }
    
    if(nextF + k > s.size()) {
        impossible(i);
        cont = false;
    }
    flip(s, k, nextF);
    j++;
    
  }
    
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  
  
  return 0;
}

