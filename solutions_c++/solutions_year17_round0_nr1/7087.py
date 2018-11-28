#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <limits.h>
#include <iomanip>

using namespace std;

int main(){

	int TC;
	cin>>TC;
	int k = 0;


	while(TC--){
		k++;
		int K;
		string S;
		cin>>S>>K;
		int flag = 0;
		int len = S.length();
		int res = 0;
		int i = 0;

		while(i + K <= len){
			if (S[i]=='-')
			{
				res++;
				for (int j = i; j < i + K; ++j)
				{
					if (S[j]=='-')
					{
						S[j] = '+';
					}
					else{
						S[j] = '-';
					}
				}
			}
			i++;
		}

		for (int j = i; j < len; ++j)
		{
			if (S[j]=='-')
			{
				cout<<"Case #"<<k<<":"<<" "<<"IMPOSSIBLE"<<endl;
				flag = 1;
				break;
			}
		}
		if(flag==0)
		cout<<"Case #"<<k<<":"<<" "<<res<<endl;

	}
}