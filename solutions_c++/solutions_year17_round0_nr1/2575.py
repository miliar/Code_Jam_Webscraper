#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <climits>

#define ll long long
 
using namespace std;

int main(){
	int t;
	cin>>t;
	int a=0;

	while (t--){
		a++;
		cout<<"Case #"<<a<<": ";
		string s;
		int k;
		cin>>s;
		cin>>k;
		int arr[1005]={0};
		int i,ans=0,cur=0;
		for (i=0;i<=s.size()-k;i++){
			cur+=arr[i];
			if (s[i]=='+'){
				if (cur%2==0){
					continue;
				}
				else{
					arr[i+k]-=1;
					ans++;
					cur++;
				}

			}
			else{
				if (cur%2==1){
					continue;
				}
				else{
					arr[i+k]-=1;
					ans++;
					cur++;
				}
			}

		}
		bool poss=true;
			while (i<s.size()){
				cur+=arr[i];
				if (s[i]=='-' && cur %2==0){
					poss=false;
					break;

				}
				if (s[i]=='+' && cur %2==1){
					poss=false;
					break;
				}
				i++;
			}

			if (poss){
				cout<<ans<<endl;
			}
			else{
				cout<<"IMPOSSIBLE"<<endl;
			}

	}
	
	return 0;
}