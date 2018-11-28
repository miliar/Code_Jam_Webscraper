#include "iostream"
#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"

using namespace std;

int main() {
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++) {
		string line;
		int k;
		cin>>line>>k;
		int ans=0;
		for(int i=0;i+k<=line.size();i++){
			if(line[i]=='+') continue;
			ans++;
			for(int j=0;j<k;j++) {
				line[i+j] = line[i+j]=='+'?'-':'+';
			}
		}
		int isgood=1;
		for(int i=0;i<line.size();i++) {
			if(line[i]=='-') isgood=0;
		}
		if(isgood) {
			cout<<"Case #"<<tc+1<<": "<<ans<<endl;
		} else {
			cout<<"Case #"<<tc+1<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}