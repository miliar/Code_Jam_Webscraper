#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>
#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <tuple>

using namespace std;


int main()

{
    freopen("A-large.in.txt","rt",stdin);
	freopen("A-large.out.txt","wt",stdout);

    int N,counter=0,K;
    cin >> N;
    string stack;
    //getline(cin, stack);
	for (int caseN = 1; caseN <= N; ++caseN) {
		counter = 0;
		cin>>stack>>K;
		int n = stack.length();
		vector<bool> flipped(n,false);
		int i = 0;
		for(auto c: stack){
			if(c=='-')
				flipped[i]=false;
			else
				flipped[i]=true;
			i++;
		}
		
		for(int i = 0; i<=flipped.size()-K; i++){
			if(flipped[i]==false){
				for(int j = i; j<i+K; j++){
					flipped[j]=!flipped[j];
				}
			
			counter++;
			}
		}
		
		//for(auto c: flipped)
		//	cout<<c<<endl;
			
		
		cout << "Case #" << caseN << ": ";
		if(find(flipped.begin(),flipped.end(),false)==flipped.end())
			cout << counter << endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}
