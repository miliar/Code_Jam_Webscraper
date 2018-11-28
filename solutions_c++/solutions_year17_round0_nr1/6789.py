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
int t,n=0,temp;//;m,z;
cin>>t;
vector <string> test;
vector<int> k;
string s;
vector<int> res;
for(int i=0;i<t;i++){
	cin>>s;
	cin>>temp;
	test.push_back(s);
	k.push_back(temp);
}

for(int i=0;i<t;i++){
	int count =0;int flag=0;
	// cout<<" "<<k[i]<<" "<<test[i].size()<<" "<<test[i]<<endl;
	for(int j=0;j<=test[i].size()-k[i];j++){
		if(test[i][j]!='+')
			{count ++;
				for(int x=j;x<j+k[i];x++){
					if(test[i][x]=='+') test[i][x]='-';
					else test[i][x]='+';
				}
	}}

	for(int j=0;j<test[i].size();j++)
		if(test[i][j]=='-') flag=1;

	if(flag==1) res.push_back(-1);
	else res.push_back(count);


}
	ofstream myfile;
  myfile.open ("example.txt");
for(int i=0;i<t;i++){
	if(res[i]>=0)
	myfile<<"Case #"<<i+1<<": "<<res[i]<<endl;
	else
		myfile<<"Case #"<<i+1<<": Impossible"<<endl;
}

  myfile.close();

//printf("%d %d\n",mini,count);
return 0;

}