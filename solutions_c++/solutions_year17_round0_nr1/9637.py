#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <set>
#include <queue>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int convert(string s){
	int answer = 0;
	int len = s.length();
	for(int i = len-1; i >=0; i--){
		int add = 1 << (len-1-i);
		if(s.at(i) == '+')
			answer += add;
	}
	return answer;
}

string flip(string s, int position, int size){
	string str = s;
	for(int i = 0; i < size; i++)
		if(str.at(position+i) == '+')
			str.at(position+i) = '-';
		else
			str.at(position+i) = '+';
	return str;
}

int main() {
  int t, size;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> s >> size; 
    int len = s.length();
   	int arr_size = 1 << len;
   	bool visited[arr_size];
    for(int k = 0; k < arr_size; k++)
      visited[k] = false;
   	bool found = false;
	  string target;
  	target.append(s.size(), '+');

   	//set<string> myset;
   	queue<string> myQ;
   	queue<int> depthQ;

    //myset.insert(s);
    myQ.push(s);                      
    depthQ.push(0);

    while(!myQ.empty()){
    	string current = myQ.front();
    	int depth = depthQ.front();
    	myQ.pop();
    	depthQ.pop();
    	//cout << current << " " << depth << " " << target << endl; 
    	if(current.compare(target) == 0){
			 cout << "Case #" << i << ": " << depth << endl;
			 found = true;
			 break;
    	}
    	else{
    		if(visited[convert(current)])
    			continue;
    		visited[convert(current)] = true;
    		for(int i = 0; i <= s.length()-size; i++){
				string a = flip(current, i, size);
				//myset.insert(a);
    			myQ.push(a);  
    			depthQ.push(depth+1);
			  }
    	}
    }
    if(!found)
    	cout << "Case #" << i << ": IMPOSSIBLE" << endl;
  }
  return 0;
}