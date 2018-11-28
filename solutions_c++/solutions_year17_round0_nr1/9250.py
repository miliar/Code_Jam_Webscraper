#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <sstream>

using namespace std;

int T;
int K;

int check(string S,int K,int count){

	for(int j=0; j<S.length(); j++){

		if(S[j]=='-'){
           if(j+K>S.length())
			   return -1;
		   else{

			   count++;
			   for(int i=0;i<K;i++)
				   if(S[j+i]=='-')
				     S[j+i]='+';
				   else 
                     S[j+i]='-';
			   return check(S,K,count);

		   }
		}
	}
	    
	return count;
}

int main() {

        FILE *fin = freopen("A-large.in", "r", stdin);
	    assert( fin!=NULL );
	    FILE *fout = freopen("A-large.out", "w", stdout);

		cin >> T;

		for(int i=1; i<=T; i++){

			string S;
		
			cin >> S >> K;
		
			cout << "Case #" << i << ": ";
			
			int count=0;
			int result=check(S,K,count);

			if(result==-1)
			   cout << "IMPOSSIBLE" << endl;
			else
			   cout << result << endl;
			
		}
		

		cin.clear();
		cin.ignore();
		cin.get();

		return 0;
}