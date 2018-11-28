#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <limits.h>
#include <iomanip>
#include <stdint.h>
#include <string>
#include <stdio.h>  
#include <stdlib.h>

using namespace std;

int main(){

	int TC;
	cin>>TC;
	int k = 0;


	while(TC--){
		
		k++;
		unsigned long long N;
		cin>>N;

		if (N<10)
		{
			cout<<"Case #"<<k<<":"<<" "<<N<<endl;
		}
		else{
			string numstr = to_string(N);
			int i = 0;
			while(i<numstr.length()-1){

				// cout<<"t "<<i<<endl;
				if (numstr[i+1]<numstr[i])
				{
					// cout<<"y"<<endl;
					for (int j = i+1; j < numstr.length(); ++j)
					{
						numstr[j] = '9';
					}
					int j = i;
					while((j>0) && (numstr[j]==numstr[j-1])){
						numstr[j] = '9';
						j--;
					}
					numstr[j] = (numstr[j] - '0' -1 + '0');
					break;
				}
				i++;
				
			}
			unsigned long long v = std::stoull(numstr);
			cout<<"Case #"<<k<<":"<<" "<<v<<endl;
		}

	}
}