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


bool isCompletePlus(string input){
	for(int i=0;i<input.length();i++){
		if(input[i] == '-')
			return false;
	}
	return true;
}

int main(){
	int t, number,p;
	string input;
	p=1;
	cin>>t;
	while(t--){
		cin>>input;
		cin>>number;


		int answer = 0;
		bool flag = true;
		size_t pos;
		for(int i=0;i<=input.length()-number;i++){
			if(input[i] == '-'){
				answer++;
				for(int j=i;j<i+number;j++){
					if(input[j] == '+')
						input[j] = '-';
					else
						input[j] = '+';
				}
			}
		}

		cout<<"Case #"<<p<<": ";
		p++;

		if(!isCompletePlus(input))
			flag = false;

		if(flag)
			cout<<answer<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

}
