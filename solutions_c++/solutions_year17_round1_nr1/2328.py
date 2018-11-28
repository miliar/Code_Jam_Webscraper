#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <queue>
#include <utility>
#include <set>
#include <bitset>
#include <stdio.h>

using namespace std;

int main(int argc, char const *argv[])
{

	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		int r,c;
		cin>>r>>c;
		char alpha[r][c];
		vector<string> rows;
		string nochar="";
		for (int k = 0; k < c; ++k)
		{
			nochar+='?';
		}
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				cin>>alpha[j][k];
				
			}
			string temp="";
			for (int k = 0; k < c; ++k)
			{
				temp+=alpha[j][k];
			}
			rows.push_back(temp);
			// cout<<temp<<"here"<<endl;
		}

		for (int j = 0; j < r; ++j)
		{
			if(rows[j].compare(nochar)!=0)
			{
				for (int k = 0; k < c; ++k)
				{
					if(alpha[j][k]!='?'){
						int left=k-1;
						while(left>=0){
							if(alpha[j][left]=='?')
							{
								alpha[j][left]=alpha[j][k];
							}
							else
								break;
							left--;
						}
						int right = k+1;
						while(right<c){
							if(alpha[j][right]=='?')
							{
								alpha[j][right]=alpha[j][k];
							}
							else
								break;
							right++;
						}
					}
				}
			}
		}

		// for (int j = 0; j < r; ++j)
		// {
		// 	for (int k = 0; k < c; ++k)
		// 	{
		// 		cout<<alpha[j][k];
		// 	}
		// 	cout<<""<<endl;
		// }

		for (int j = 0; j < r; ++j)
		{
			if(rows[j].compare(nochar)!=0){
				int up=j-1;
				while(up>=0){
					if(rows[up].compare(nochar)==0){
						for (int k = 0; k < c; ++k)
						{
							alpha[up][k]=alpha[j][k];
						}
					}
					else
						break;
					up--;
				}
				int down=j+1;
				while(down<r){
					if(rows[down].compare(nochar)==0){
						for (int k = 0; k < c; ++k)
						{
							alpha[down][k]=alpha[j][k];
						}
					}
					else
						break;
					down++;
				}
			}

		}
		cout<<"Case #"<<i<<": "<<endl;
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
			{
				cout<<alpha[j][k];
			}
			cout<<""<<endl;
		}

	}
	return 0;
}