#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<string>



#define LL long long
using namespace std;

int main(){
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
int T;
vector<bool>v;
string term;
int k;
cin>>T;
for(int i = 1 ; i<= T ;i++){
	cin>>term>>k;
	int len = term.size();
	for(int j = 0;j < len; j++){
		if(term[j] == '+')
			v.push_back(1);
		else v.push_back(0);	
	}
	
	int num = 0;
	for(int j = 0;j<= len-k;j++){
		if(v[j] == 0){
			++num;
			for(int x = 0; x<k ;x++){
				v[j+x]=v[j+x]^1;
			}
			
		}
	}
	for(int j = len -k ;j<len;j++){
		if(v[j]==0){
			num = -1;
			break;
		}
	}
	

	if(num == -1)cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
	else cout<<"Case #"<<i<<": "<<num<<endl;
	
	v.clear();
} 

return 0;
}


