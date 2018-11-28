#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define myLoop(x) for(int i=0;i<x;i++)
#define rangeLoop(x,y) for(int i=x;i<y;i++)
#define myNestedLoop(x) for(int j=0;j<x;j++)
#define MOD 1000000009
#define speedUp ios::sync_with_stdio(false)


inline  int sscan(){
	register  int n=0,c=getchar();
	while(c<'0'||c>'9')
		c=getchar();
		while(c<='9'&&c>='0'){
			n=n*10+c-'0';
			c=getchar();
	    }
	return n;
}



int main(){
	speedUp;
	int t;
	LL number;
	vector<int> myVec;
	int p =1;
	cin>>t;
	while(t--){
		cin>>number;
		LL myNum = number;
		myVec.clear();
		while(myNum>0){
			myVec.push_back(myNum%10);
			myNum = myNum/10;
		}
		reverse(myVec.begin(), myVec.end());

		for(int j=myVec.size()-2;j>=0;j--){
			if(myVec[j] <= myVec[j+1])
				continue;
			else{
				myVec[j] = myVec[j]-1;
				myVec[j+1] = 9;
				if(j+2<myVec.size()){
					int k = j+1;
					while(myVec[k+1]<myVec[k] && k+1<myVec.size()){
						myVec[k+1] = myVec[k];
						k++;
					}
				}
			}
		}

		//print

		cout<<"Case #"<<p<<": ";
		p++;
		int i=0;
		while(myVec[i++]==0){
			myVec.erase(myVec.begin());
		}
	
		LL myAnswer = 0;
		for(int i=0;i<myVec.size();i++){
			myAnswer = myAnswer*10+myVec[i];
		}

		cout<<myAnswer<<endl;
	}


}
