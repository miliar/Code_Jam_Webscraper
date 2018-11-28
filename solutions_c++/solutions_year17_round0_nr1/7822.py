#include<bits/stdc++.h>
using namespace std;
int count(vector<bool> bits, int N){
  queue<int> fl;
  int moves = 0;
   int size=(int)bits.size();
  for (int i = 0;i<size; ++i) {
    if (!fl.empty() && fl.front() <= i - N)
      fl.pop();

    if ((bits[i]^(fl.size()%2==0))==1){
      if (i>size-N)
        return -1; // IMPOSSIBLE
      moves++;
      fl.push(i);
    } 
  }
  return moves;
}
int main(){
	std::ios::sync_with_stdio(false);
	fstream in("A-large.in", ios::in);
	fstream out("pan3.out",ios::out);
	int tc;
	in>>tc;
	for(int j=1;j<=tc;j++){
		string s;
		int w_len;
		in>>s>>w_len;
		int s_len=(int)s.length();
		vector <bool> fl;
		for(int i=0;i<s_len;i++){
			if(s[i]=='+')
				fl.push_back(true);
			else
				fl.push_back(false);
		}
		int c=count(fl,w_len);
		if(c==-1)
			out<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
		else
			out<<"Case #"<<j<<": "<<c<<endl;
	}
	return(0);
}
		
	
