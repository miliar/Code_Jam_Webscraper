#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000

int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		long long n;
		cin>>n;
		vector<int> d;
		while(n!=0){
			d.push_back(n%10);
			n /= 10;
		}
		reverse(d.begin(),d.end());
		int m = d.size();
		for(int i=0; i<m; i++){
			for(int j=0; j<m-1; j++){
				if(d[j]>d[j+1]){
					d[j]--;
					for(int k=j+1; k<m; k++)
						d[k] = 9;
					break;
				}
			}
		}
		cout<<"Case #"<<tc<<": ";
		int j=0;
		while(d[j]==0)
			j++;
		for(int i=j; i<m; i++)
			cout<<d[i];
		cout<<endl;
	}
}