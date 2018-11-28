#include <cstdio>
#include <iostream>

using namespace std;

int pancakes(string s, int K)
{
	int p_happy=0;
	int N=0;
	int length=s.length();

	for(int i=0; i<length; ++i) {
		if(s[i]=='+')
			p_happy++;
	}

	for(int i=0; i<length; ++i) {
		if(p_happy==length)
			return N;
		if(s[i]=='-') {
			for(int j=0; j<K; ++j) {
				if(s[i+j]=='-') {
					s[i+j]='+';
					p_happy++;
				}
				else {
					s[i+j]='-';
					p_happy--;
				}
			}
		N++;
		
		}

	}
	
	return -1;
}

int main(int argc, char const *argv[])
{
	int t, n, K;
	int N;
	string s;
  	cin >> t;  
  	for (int i = 1; i <= t; ++i) {
    	cin >> s >> K;  // read n and then m.
  
    	if((N=pancakes(s, K))>=0) 
    		cout << "Case #" << i << ": " << N<< endl;
    	else 
    		cout << "Case #" << i << ": IMPOSSIBLE\n";
  	}

	return 0;
}
