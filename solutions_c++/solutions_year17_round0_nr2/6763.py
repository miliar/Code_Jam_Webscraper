#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
#include <climits>
#include <math.h>
#include <string>
#include <fstream>

int main(){
int t,n,temp;//;m,z;
cin>>t;
vector <string> test;
//vector<int> k;
string s;
vector<string> res;
for(int i=0;i<t;i++){
	cin>>s;
	//cin>>temp;
	test.push_back(s);
	//k.push_back(temp);
}

for(int i=0;i<t;i++){
	int count =0;int flag=0;
	// cout<<" "<<k[i]<<" "<<test[i].size()<<" "<<test[i]<<endl;
	for(int j=test[i].size()-1;j>0;j--){
		if(test[i][j]<test[i][j-1])
			{test[i][j-1]--;
			 for(int x=j;x<test[i].size();x++)
			 	test[i][x]='9';
			 j=test[i].size()-1;				
	}
}
	res.push_back(test[i]);


}
	ofstream myfile;
  myfile.open ("example.txt");
for(int i=0;i<t;i++){
	if(res[i][0]=='0') res[i].erase(res[i].begin());
	myfile<<"Case #"<<i+1<<": "<<res[i]<<endl;
	// else 
	// myfile<<"Case #"<<i+1<<": "<<res[i]+1<<endl;	
}

  myfile.close();

//printf("%d %d\n",mini,count);
return 0;

}