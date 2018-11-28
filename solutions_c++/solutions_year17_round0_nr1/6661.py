#include <iostream>
#include <cstring>
#include <sstream>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int test;
	cin>>test;
	char arr[1010];
	int k;
	stringstream ss;
	for(int testnum=1;testnum<=test;testnum++){
		cin>>arr>>k;
		int len = strlen(arr), ans = 0;
		for(int i=0;i+k-1<len;i++){
			if (arr[i]=='-'){
				for(int j=0;j<k;j++){
					arr[i+j] = (arr[i+j]=='-' ? '+' : '-' );
				}
				ans++;
			}
		}
		int off = len-k,i;
		for(i=1;i<k;i++){
			if (arr[off+i]=='-') break;
		}
		if (i==k){
			ss<<"Case #"<<testnum<<": "<<ans<<"\n";
		}
		else{
			ss<<"Case #"<<testnum<<": "<<"IMPOSSIBLE\n";
		}
	}
	cout<<ss.str();
}