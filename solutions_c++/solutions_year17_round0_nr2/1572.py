/*
 * A.cpp
 *
 *  Created on: 11 Apr 2016
 *      Author: xing
 */


#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

#define DEBUG

/*
vector<vector<long> > M(19, vector<long>(10, 0));

void solve(int index){
	long N, presum = 0, sum = 0;

	cin>>N;
	string res;
	int i, j;
	for(i = 1;i<19;i++){
		for(j = 1;j<10;j++){
			if(M[i][j]==0){
				//cal M[i][j]
				if(i == 1){
					M[i][j] = 1;
				}
				else{
					if(j == 1){
						for(int k = 1;k<10;k++)
							M[i][j] += M[i-1][k];
					}
					else{
						M[i][j] = M[i][j-1]-M[i-1][j-1];
					}
				}
			}
			sum += M[i][j];
#ifdef DEBUG
	cout<<"i j M[i][j] sum "<<i<<" "<<j<<" "<<M[i][j]<<" "<<sum<<endl;
#endif
			if(sum >= N)
				goto END_OF_CAL;
			presum = sum;
		}
	}

	END_OF_CAL:	;

#ifdef DEBUG
	cout<<"sum presum N "<<sum<<" "<<presum<<" "<<N<<endl;
#endif

	while(sum > N){
		res.append(1, '0'+j);
		N -= presum;
		i--;
		sum = 0;
		for(;;j++){
			sum += M[i][j];
			if(sum>=N)
				break;
			presum = sum;
		}
	}
	res.append(1, '0'+j);
	res.append(i-1, '9');

	cout<<"Case #"<<index<<": "<<res<<endl;
}
*/

void solve(int index){
	string str;
	getline(cin, str);
	//cout<<"str: "<<str<<endl;

	int n = str.size(), i;
	for(i = 0;i<n-1 && str[i]<=str[i+1];i++){

	}
	if(i == n-1){
		cout<<"Case #"<<index<<": "<<str<<endl;
		return;
	}
	for(int j = i+1;j<n;j++)
		str[j] = '9';
	str[i]--;
	while(i>0&&str[i]<str[i-1]){
		str[i] = '9';
		str[i-1]--;
		i--;
	}
	if(str[0] == '0')
		str = str.substr(1);

	cout<<"Case #"<<index<<": "<<str<<endl;
	return;

}

int main(){


	int T;

	cin>>T;
	string str;
	getline(cin, str);

	for(int i = 0;i<T;i++){
		solve(i+1);
	}

}
